// Firebase client initialization
//
// This module initialises the Firebase app using environment variables defined
// in `.env.local`.  It exports the Firebase Auth instance for use across
// pages and components.

import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

// Firebase configuration pulled from environment variables.  These variables
// must be defined in `.env.local` and prefixed with `NEXT_PUBLIC_` so that
// they are exposed to the browser at build time.
const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID
};

// Initialize Firebase app and export the Auth instance
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

export default app;