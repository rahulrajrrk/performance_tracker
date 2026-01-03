"""API routers package.

This package exposes individual APIRouter instances for different functional
domains.  Each router is imported in `app.main` and included on the FastAPI
application with the appropriate path prefix and dependencies.
"""

from . import users, calls, payments, incentives, analytics, whatsapp  # noqa: F401

__all__ = [
    "users",
    "calls",
    "payments",
    "incentives",
    "analytics",
    "whatsapp",
]