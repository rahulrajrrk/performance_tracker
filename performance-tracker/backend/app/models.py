"""Pydantic models for API schemas.

The models defined here describe the shape of the data exchanged between the
client and the API.  These are used as request bodies for creating and
updating records as well as response models returned by the API.
"""

from __future__ import annotations

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field, constr


class Demo(BaseModel):
    """Represents a single demo conducted during a day."""

    demo_time_minutes: int = Field(..., ge=1, description="Duration of the demo in minutes")
    demo_card_link: constr(strip_whitespace=True) = Field(
        ..., description="URL or identifier for the demo card"
    )
    notes: Optional[str] = Field(None, description="Optional notes about the demo")


class CallEntry(BaseModel):
    """Represents a daily call entry for an employee."""

    date: date = Field(..., description="Date of the calls entry (YYYY‑MM‑DD)")
    answered_calls: int = Field(..., ge=0, description="Number of calls answered")
    unanswered_calls: int = Field(..., ge=0, description="Number of calls unanswered")
    total_call_time_minutes: int = Field(..., ge=0, description="Total call time in minutes")
    demos: List[Demo] = Field(default_factory=list, description="List of demos conducted on that date")

    class Config:
        # Allow population by field name for nested objects
        orm_mode = True


class Payment(BaseModel):
    """Represents a payment entry."""

    date: date = Field(..., description="Date of the payment (YYYY‑MM‑DD)")
    customer_name: str = Field(..., description="Name of the customer")
    mobile: str = Field(..., description="Customer's mobile number")
    organization_name: Optional[str] = Field(None, description="Name of the customer's organisation")
    customer_type: constr(to_lower=True) = Field(
        ..., regex="^(new|repeat)$", description="Indicates whether the customer is new or repeat"
    )
    service: str = Field(..., description="Service taken (WhatsApp API, RCS, Bulk SMS, Voice Calls, Email)")
    product_type: str = Field(..., description="Product type (same as service for now)")
    amount_paid: float = Field(..., gt=0, description="Amount paid by the customer")
    customer_card_link: constr(strip_whitespace=True) = Field(
        ..., description="URL or identifier for the customer card"
    )
    notes: Optional[str] = Field(None, description="Optional notes about the payment")


class Incentive(BaseModel):
    """Represents an incentive derived from a payment."""

    payment_id: str = Field(..., description="Identifier of the corresponding payment")
    date: date = Field(..., description="Date of the payment (same as the payment date)")
    service: str = Field(..., description="Service that generated the incentive")
    amount_paid: float = Field(..., gt=0, description="Amount paid that triggers the incentive")
    base_percent: float = Field(..., gt=0, description="Service‑specific base percentage")
    global_percent: float = Field(..., gt=0, description="Global incentive percentage")
    incentive_amount: float = Field(..., gt=0, description="Calculated incentive amount")