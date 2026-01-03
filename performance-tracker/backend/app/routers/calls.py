"""Call entry endpoints.

This router exposes endpoints for employees to create or fetch call entries
for a given date and for managers/admins to query call history of their
team.  Actual persistence is not implemented; these endpoints return
placeholder responses.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from ..auth import get_current_user
from ..models import CallEntry


router = APIRouter(prefix="/calls", tags=["calls"])


@router.post("/", summary="Create or update a daily call entry")
async def upsert_call_entry(
    entry: CallEntry, current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """Create or update the call entry for the given date.

    Employees can create or update their own entry.  Managers/admins can
    optionally specify an `employee_id` field in the payload to upsert on
    behalf of an employee.  Here we return a stubbed response only.
    """
    uid = current_user.get("uid")
    role = current_user.get("role")

    # In a real implementation, validate that only managers/admins can upsert
    # entries for other users.
    # Save the entry in Firestore with a deterministic document ID (uid_date).
    doc_id = f"{uid}_{entry.date}"
    # TODO: Write to Firestore
    return {"status": "success", "doc_id": doc_id, "data": entry.dict()}


@router.get("/", summary="List call entries for the current user")
async def list_calls(
    from_date: Optional[date] = Query(None, alias="from", description="Start date inclusive"),
    to_date: Optional[date] = Query(None, alias="to", description="End date inclusive"),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """List call entries for the authenticated user within the given date range.

    Returns a stub response.  In a full implementation this would query
    Firestore for documents with IDs between `uid_from` and `uid_to`.
    """
    uid = current_user.get("uid")
    # TODO: Query Firestore for calls between from_date and to_date
    return {
        "status": "success",
        "uid": uid,
        "from": from_date,
        "to": to_date,
        "entries": [],
    }