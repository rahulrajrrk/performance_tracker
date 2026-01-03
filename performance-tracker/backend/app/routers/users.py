"""User management endpoints.

This router provides endpoints for creating users and retrieving the
authenticated user's profile.  Administrative actions are restricted to
admins.  Actual persistence logic should be implemented in the service layer;
here we provide stubs for demonstration purposes.
"""

from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException

from ..auth import get_current_user
from ..models import Payment


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", summary="Retrieve current user profile")
async def get_me(current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """Return the currently authenticated user's profile.

    This endpoint simply echoes back the user record retrieved by the
    authentication dependency.  In a real application, sensitive fields
    should be stripped or mapped to a response model.
    """
    return current_user


@router.post("/", summary="Create a new user (admin only)")
async def create_user(user: Dict[str, Any], current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    """Create a new user.

    Only admins are allowed to create users.  The input `user` should
    contain at minimum an `email`, `password` and `role`.  In this stub,
    we simply validate the caller's role and return the submitted data.
    """
    if current_user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Only admins can create users")
    # TODO: Create the user in Firebase Auth and store the profile in Firestore
    return {"status": "success", "user": user}