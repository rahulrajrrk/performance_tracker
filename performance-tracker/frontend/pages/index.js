import { useEffect } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';

/**
 * Landing page component.
 *
 * This component listens for Firebase auth state changes.  If a user is
 * authenticated it fetches the user's profile from the backend and
 * redirects them to the appropriate dashboard based on their role.  If
 * not authenticated, it redirects to the login page.
 */
export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      if (user) {
        try {
          const token = await user.getIdToken();
          const res = await axios.get(
            `${process.env.NEXT_PUBLIC_BACKEND_URL}/users/me`,
            {
              headers: { Authorization: `Bearer ${token}` },
            }
          );
          const role = res.data.role;
          if (role === 'MANAGER') {
            router.replace('/manager/dashboard');
          } else if (role === 'ADMIN') {
            router.replace('/admin/users');
          } else {
            router.replace('/employee/dashboard');
          }
        } catch (err) {
          console.error(err);
          router.replace('/login');
        }
      } else {
        router.replace('/login');
      }
    });
    return () => unsubscribe();
  }, [router]);

  return <p>Loading...</p>;
}