"""WhatsApp monthly payment endpoints.

This router manages recurring WhatsApp API monthly payments.  Each customer
has a fixed due day; new payments set the next due date to the same day of
the following month (adjusting for month length).  Only managers and admins
may create or edit these records.  Stub implementations are provided.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from ..auth import get_current_user


router = APIRouter(prefix="/whatsapp", tags=["whatsapp"])


@router.post("/customers", summary="Add or update a WhatsApp monthly customer")
async def add_customer(
    customer: Dict[str, Any],
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """Create or update a WhatsApp monthly customer profile.

    Required fields in `customer`:
    - `mobile`: Unique identifier for the customer.
    - `organization_name`: Name of the organisation.
    - `customer_name`: Name of the customer.
    - `fixed_due_day`: Integer (1–31) specifying the monthly due date.

    Only managers or admins may perform this action.
    """
    role = current_user.get("role")
    if role not in {"MANAGER", "ADMIN"}:
        raise HTTPException(status_code=403, detail="Only managers or admins can manage WhatsApp customers")
    # TODO: Persist customer to Firestore
    return {"status": "success", "customer": customer}


@router.post("/monthly-payments", summary="Record a WhatsApp monthly payment")
async def add_monthly_payment(
    payment: Dict[str, Any],
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """Record a monthly payment for a WhatsApp API customer.

    Expected fields in `payment`:
    - `mobile`: Customer mobile number
    - `date_paid`: Payment date (YYYY‑MM‑DD)
    - `amount`: Payment amount
    - `card_link`: Customer card link
    - `notes`: Optional notes
    Only managers or admins may perform this action.
    """
    role = current_user.get("role")
    if role not in {"MANAGER", "ADMIN"}:
        raise HTTPException(status_code=403, detail="Only managers or admins can record WhatsApp payments")
    # TODO: Persist payment and update next due date
    return {"status": "success", "payment": payment}


@router.get("/due", summary="List upcoming WhatsApp payments due")
async def list_due_payments(
    window: str = Query("today", regex="^(today|week)$"),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """List WhatsApp payments due today or this week.

    Managers and admins see all due payments across all customers.
    """
    # TODO: Query Firestore for customers with due dates in the specified window
    return {
        "status": "success",
        "window": window,
        "due_payments": [],
    }