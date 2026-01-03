# Backend (FastAPI)

This directory contains the FastAPI application responsible for serving the APIs used by the performance tracker.  The backend interfaces with Firebase Authentication for user identity and Firestore for persistent storage.

## Structure

```
backend/
├── app/
│   ├── main.py        # Application entrypoint
│   ├── auth.py        # Firebase authentication utilities
│   ├── firestore.py    # Firestore client helper
│   ├── models.py       # Pydantic models / schemas
│   └── routers/        # API routers split by domain
│       ├── __init__.py
│       ├── users.py
│       ├── calls.py
│       ├── payments.py
│       ├── incentives.py
│       ├── analytics.py
│       └── whatsapp.py
├── requirements.txt    # Python dependencies
└── Dockerfile          # Container configuration for deployment (optional)
```

## Running locally

Create a virtual environment and install dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the development server:

```sh
uvicorn app.main:app --reload --port 8000
```

This will run the API on `http://localhost:8000`.

## Environment Configuration

The backend uses the Google Cloud Firestore client and Firebase Admin SDK.  You must provide service account credentials via environment variables or a credentials file to allow the backend to verify Firebase ID tokens and read/write data.  See `app/auth.py` and `app/firestore.py` for details.
