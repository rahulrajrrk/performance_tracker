"""FastAPI application entrypoint.

This module constructs the FastAPI application, configures CORS, and
registers all API routers.  The authentication dependency provided in
`app.auth` ensures that every request is accompanied by a valid Firebase
identity token.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, calls, payments, incentives, analytics, whatsapp


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="Performance Tracker API", version="0.1.0")

    # CORS configuration – adjust origins as needed for the Next.js front‑end
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Health check endpoint
    @app.get("/", summary="Health check")
    async def root() -> dict[str, str]:
        return {"status": "ok"}

    # Register API routers
    app.include_router(users.router)
    app.include_router(calls.router)
    app.include_router(payments.router)
    app.include_router(incentives.router)
    app.include_router(analytics.router)
    app.include_router(whatsapp.router)

    return app


app = create_app()