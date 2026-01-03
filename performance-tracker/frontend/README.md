# Frontend (Next.js)

This directory contains the Next.js front‑end for the performance tracker.  The
application uses Firebase Authentication on the client side and communicates
with the FastAPI backend via REST endpoints.  Routing is role aware: after
login the user is directed to the correct dashboard based on their role.

## Structure

```
frontend/
├── pages/              # Next.js pages
│   ├── index.js        # Redirects to login or dashboard
│   ├── login.js        # Sign in / sign up page
│   ├── employee/
│   │   ├── dashboard.js
│   │   ├── calls.js
│   │   ├── payments.js
│   │   └── incentives.js
│   ├── manager/
│   │   ├── dashboard.js
│   │   ├── payments.js
│   │   ├── analytics.js
│   │   └── whatsapp.js
│   └── admin/
│       ├── users.js
│       └── master.js
├── components/         # Reusable UI components
│   ├── Layout.js
│   ├── Navbar.js
│   └── ProtectedRoute.js
├── firebase.js         # Firebase client setup
├── package.json        # Frontend dependencies and scripts
└── .gitignore
```

## Getting started

1. Install dependencies:

   ```sh
   npm install
   ```

2. Create a `.env.local` file with your Firebase configuration.  It should
   define the following variables:

   ```env
   NEXT_PUBLIC_FIREBASE_API_KEY=...        
   NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
   NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
   NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=...
   NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
   NEXT_PUBLIC_FIREBASE_APP_ID=...
   NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
   ```

   Replace the values with your Firebase project settings and the URL of
   your running FastAPI backend.  Do not commit this file to the repository.

3. Start the development server:

   ```sh
   npm run dev
   ```

4. Open `http://localhost:3000` in your browser to view the application.

The pages in this scaffold currently display placeholders.  You can build
out each page using your preferred React component library or Tailwind CSS.
