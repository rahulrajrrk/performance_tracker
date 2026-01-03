# Performance Tracker Web Application

This repository contains the code for a **performance tracking** application for staff, managers and administrators.  It is split into a **Next.js** front‑end and a **FastAPI** back‑end and uses **Firebase Authentication** and **Firestore** for authentication and data storage.

## Overview

### Features

* **Role based dashboards**
  * Employees see only their own calls, payments, incentives and analytics.
  * Managers see their own data separately from their team’s data with aggregate analytics and payment views.
  * Admins have full control including the ability to create users, assign roles and remap employees to managers.
* **Call entry**
  * One record per employee per day.
  * Supports multiple demos per day with validation (if demos are entered, both the time and the link are required).
* **Payments & incentives**
  * Payments can be entered for multiple customers per day.
  * Incentives are automatically generated/updated based on the service’s base percentage and a global incentive percentage.
  * Managers and admins can edit payments; employees cannot edit a payment once it has been submitted.
* **WhatsApp monthly tracking**
  * Centralised tracking of recurring WhatsApp API monthly payments.
  * Each customer has a fixed due day (e.g. 5th of the month); if the month has fewer days, the due date is rolled to the last day.
  * Managers and admins can see upcoming payments due today and this week.
* **Analytics**
  * Service‑wise breakdown of revenue.
  * Daily and weekly revenue trends.
  * New vs repeat customer analysis.
  * Top customers by revenue (grouped by mobile number).
  * Team totals and drill‑down to individual employee performance.

### Repository Structure

```
performance‑tracker/
├── backend/          # FastAPI application for APIs and business logic
│   ├── app/
│   │   ├── main.py   # FastAPI entrypoint
│   │   ├── auth.py   # Firebase token verification utilities
│   │   ├── firestore.py   # Helper for interacting with Firestore
│   │   ├── models.py       # Pydantic models / schemas
│   │   └── routers/        # API routers (users, calls, payments, incentives, analytics, whatsapp)
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Setup instructions for the backend
├── frontend/         # Next.js application for the user interface
│   ├── pages/
│   │   ├── index.js        # Landing page / login redirect
│   │   ├── login.js        # Authentication page
│   │   ├── employee/
│   │   │   ├── dashboard.js
│   │   │   ├── calls.js
│   │   │   ├── payments.js
│   │   │   └── incentives.js
│   │   ├── manager/
│   │   │   ├── dashboard.js
│   │   │   ├── payments.js
│   │   │   ├── analytics.js
│   │   │   └── whatsapp.js
│   │   └── admin/
│   │       ├── users.js
│   │       └── master.js
│   ├── components/    # Shared UI components
│   │   ├── Layout.js
│   │   ├── Navbar.js
│   │   └── ProtectedRoute.js
│   ├── firebase.js    # Firebase client configuration
│   ├── package.json   # Frontend dependencies and scripts
│   └── README.md      # Setup instructions for the frontend
├── .gitignore
└── README.md          # This file
```

## Development

### Prerequisites

* Node.js (16.x or later) and npm or yarn for the Next.js front‑end.
* Python 3.10+ and pip for the FastAPI back‑end.
* A Google Cloud project with Firebase Authentication and Firestore enabled.
* A GitHub repository with appropriate access rights; this repo is intended to be linked to such a remote repository.

### Local setup

1. Clone this repository and change into the project directory:

   ```sh
   git clone <your‑repo‑url>
   cd performance‑tracker
   ```

2. **Front‑end**

   ```sh
   cd frontend
   npm install
   npm run dev
   ```

   This starts the Next.js development server on `http://localhost:3000`.

3. **Back‑end**

   ```sh
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

   This starts the FastAPI server on `http://localhost:8000`.

### Deployment

Deployment to Google Cloud Run can be performed using the provided `Dockerfile` and `requirements.txt` in the `backend` directory. The front‑end can be deployed to Vercel, Firebase Hosting or any static hosting platform that supports Next.js.  See the `backend/README.md` and `frontend/README.md` for more details.

## License

This project is provided as‑is for demonstration purposes and is not intended for production use without appropriate hardening, testing and security review.