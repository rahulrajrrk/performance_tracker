"""Firestore client helper.

This module exposes a helper to obtain a cached Firestore client.  The client
is cached using `lru_cache` so that it is created only once per process.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

from google.cloud import firestore


@lru_cache(maxsize=1)
def get_firestore_client() -> firestore.Client:
    """Get a Firestore client instance.

    Returns:
        A cached `google.cloud.firestore.Client` configured to use the project
        associated with the service account credentials.
    """
    return firestore.Client()