"""Firebase authentication utilities.

This module provides helper functions to verify Firebase ID tokens and to
retrieve the authenticated user's profile.  The FastAPI dependency
`get_current_user` can be used in API endpoints to ensure the caller is
authenticated and to access the caller's identity.
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Any, Dict, Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import firebase_admin
from firebase_admin import auth as firebase_auth, credentials

from .firestore import get_firestore_client


# Bearer token security scheme for FastAPI
_bearer_scheme = HTTPBearer(auto_error=False)


@lru_cache(maxsize=1)
def _initialize_firebase_app() -> firebase_admin.App:
    """Initialise the Firebase app if not already initialised.

    Firebase Admin SDK requires initialization with credentials.  The
    credentials may be provided via the `GOOGLE_APPLICATION_CREDENTIALS`
    environment variable or a service account JSON key file path.  If the
    application has already been initialised elsewhere, this function simply
    returns the existing app.
    """
    if not firebase_admin._apps:
        cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not cred_path or not os.path.isfile(cred_path):
            raise RuntimeError(
                "Firebase credentials not found. Set GOOGLE_APPLICATION_CREDENTIALS to a service account JSON file."
            )
        cred = credentials.Certificate(cred_path)
        return firebase_admin.initialize_app(cred)
    # If already initialised, return the default app
    return firebase_admin.get_app()


def verify_id_token(id_token: str) -> Dict[str, Any]:
    """Verify a Firebase ID token and return the decoded claims.

    Args:
        id_token: The JWT provided by the client.

    Returns:
        The decoded token if verification succeeds.

    Raises:
        HTTPException: If the token is invalid or verification fails.
    """
    _initialize_firebase_app()
    try:
        decoded = firebase_auth.verify_id_token(id_token)
        return decoded
    except Exception as exc:
        raise HTTPException(status_code=401, detail=f"Invalid authentication token: {exc}") from exc


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(_bearer_scheme),
) -> Dict[str, Any]:
    """FastAPI dependency to validate the caller's Firebase ID token.

    If the request does not contain valid credentials, a 401 error is raised.

    Returns:
        A dictionary representing the Firebase user and associated profile from Firestore.
    """
    if credentials is None:
        raise HTTPException(status_code=401, detail="Missing authentication credentials")
    token = credentials.credentials
    decoded = verify_id_token(token)

    uid: str = decoded.get("uid")
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token: missing UID")

    # Optionally fetch the user's profile from Firestore
    db = get_firestore_client()
    user_doc = db.collection("users").document(uid).get()
    profile: Dict[str, Any] = user_doc.to_dict() if user_doc.exists else {}
    profile.setdefault("uid", uid)

    # Attach roles/claims if defined in custom claims or Firestore
    # Firebase custom claims may contain role information; if not, fall back to Firestore
    role = decoded.get("role") or profile.get("role")
    if role:
        profile["role"] = role
    return profile