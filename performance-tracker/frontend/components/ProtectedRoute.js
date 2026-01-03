import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';

/**
 * Protects a page by ensuring the user is authenticated.  If the user is not
 * authenticated they are redirected to the login page.  While the auth
 * state is being resolved a simple "Loading..." message is displayed.
 */
export default function ProtectedRoute({ children }) {
  const router = useRouter();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      if (!user) {
        router.replace('/login');
      }
      setLoading(false);
    });
    return () => unsubscribe();
  }, [router]);

  if (loading) {
    return <p>Loading...</p>;
  }
  return children;
}