"""Incentive endpoints.

This router exposes read‑only endpoints for fetching incentives.  Incentives
are automatically created and updated when payments are saved or modified.
The current implementation returns stub responses.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, Query

from ..auth import get_current_user


router = APIRouter(prefix="/incentives", tags=["incentives"])


@router.get("/", summary="List incentives")
async def list_incentives(
    from_date: Optional[date] = Query(None, alias="from"),
    to_date: Optional[date] = Query(None, alias="to"),
    employee_uid: Optional[str] = Query(None),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """List incentives for the current user or a specified employee.

    Managers and admins can set `employee_uid` to view incentives for team
    members.  The `from` and `to` parameters restrict the date range.
    """
    role = current_user.get("role")
    # TODO: Query Firestore for incentives within range
    return {
        "status": "success",
        "filters": {
            "from": from_date,
            "to": to_date,
            "employee_uid": employee_uid,
        },
        "incentives": [],
    }