"""Payment entry endpoints.

This router allows employees to create payment entries and managers/admins to
view and edit payments.  Incentives are automatically created or updated
when payments are changed.  The current implementation returns stub
responses.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from ..auth import get_current_user
from ..models import Payment


router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/", summary="Create a payment entry (employees)")
async def create_payment(
    payment: Payment, current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """Create a new payment entry for the authenticated employee.

    Employees cannot edit payments once submitted.  Managers and admins can
    edit payments via the PUT endpoint below.  Incentive creation occurs
    automatically in the backend service layer.
    """
    uid = current_user.get("uid")
    # TODO: Persist to Firestore and compute incentive
    payment_id = "payment_stub_id"
    return {"status": "success", "payment_id": payment_id, "data": payment.dict()}


@router.get("/", summary="List payment entries")
async def list_payments(
    from_date: Optional[date] = Query(None, alias="from"),
    to_date: Optional[date] = Query(None, alias="to"),
    service: Optional[str] = Query(None),
    customer_type: Optional[str] = Query(None),
    employee_uid: Optional[str] = Query(None),
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """List payments filtered by date range, service, customer type and employee.

    Managers and admins can specify `employee_uid` to view payments for a team
    member.  Employees ignore the `employee_uid` parameter.
    """
    # TODO: Query Firestore with filters respecting RBAC
    return {
        "status": "success",
        "filters": {
            "from": from_date,
            "to": to_date,
            "service": service,
            "customer_type": customer_type,
            "employee_uid": employee_uid,
        },
        "payments": [],
    }


@router.put("/{payment_id}", summary="Update a payment (manager/admin)")
async def update_payment(
    payment_id: str,
    payment: Payment,
    current_user: Dict[str, Any] = Depends(get_current_user),
) -> Dict[str, Any]:
    """Update an existing payment.

    Only managers or admins are allowed to edit payments.  Employees cannot
    modify a payment once it has been created.  Incentive amounts must be
    re‑calculated when a payment is updated.
    """
    role = current_user.get("role")
    if role not in {"MANAGER", "ADMIN"}:
        raise HTTPException(status_code=403, detail="Only managers or admins can edit payments")
    # TODO: Update Firestore record and linked incentive
    return {"status": "success", "payment_id": payment_id, "data": payment.dict()}


@router.delete("/{payment_id}", summary="Delete a payment (manager/admin)")
async def delete_payment(
    payment_id: str, current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """Delete a payment and its associated incentive.

    Only managers or admins can perform deletions.  On deletion the linked
    incentive must also be removed.  Here we return a stub response.
    """
    role = current_user.get("role")
    if role not in {"MANAGER", "ADMIN"}:
        raise HTTPException(status_code=403, detail="Only managers or admins can delete payments")
    # TODO: Delete the payment and its incentive from Firestore
    return {"status": "success", "payment_id": payment_id}