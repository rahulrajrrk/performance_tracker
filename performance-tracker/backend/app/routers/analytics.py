"""Analytics endpoints.

This router provides aggregated reporting endpoints used by the dashboards.
The endpoints are protected and return stubbed responses; actual
implementations would perform Firestore queries and aggregations or export
data to BigQuery for analysis.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from ..auth import get_current_user


router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/overview", summary="Overall analytics overview")
async def get_overview(
    from_date: Optional[date] = Query(None, alias="from"),
    to_date: Optional[date] = Query(None, alias="to"),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """Return high‑level analytics for the authenticated user or team.

    The exact metrics returned depend on the user's role.  For employees the
    statistics are limited to their own performance; managers and admins
    receive aggregated team statistics.  In this stub we return a static
    structure.
    """
    role = current_user.get("role")
    return {
        "status": "success",
        "role": role,
        "from": from_date,
        "to": to_date,
        "data": {
            "total_calls": 0,
            "total_answered": 0,
            "total_unanswered": 0,
            "total_payments": 0,
            "total_incentives": 0,
            "service_breakdown": {},
        },
    }


@router.get("/top-customers", summary="Top customers by revenue")
async def top_customers(
    limit: int = Query(10, ge=1, le=100),
    from_date: Optional[date] = Query(None, alias="from"),
    to_date: Optional[date] = Query(None, alias="to"),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """Return the top customers ranked by revenue.

    The results are grouped by mobile number.  In a real implementation this
    would require either Firestore aggregation (which is limited) or an
    export to BigQuery.  Here we return a stubbed list.
    """
    return {
        "status": "success",
        "limit": limit,
        "from": from_date,
        "to": to_date,
        "customers": [],
    }