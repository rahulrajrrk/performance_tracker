import Link from 'next/link';
import { useRouter } from 'next/router';
import { signOut } from 'firebase/auth';
import { auth } from '../firebase';

/**
 * Simple navigation bar.
 *
 * Displays links based on the current URL.  A sign out button logs the user
 * out of Firebase and redirects to the login page.  For a production app
 * you would likely tailor the menu to the user's role.
 */
export default function Navbar() {
  const router = useRouter();

  const handleSignOut = async () => {
    await signOut(auth);
    router.replace('/login');
  };

  return (
    <nav
      style={{
        backgroundColor: '#f5f5f5',
        padding: '0.5rem 1rem',
        marginBottom: '1rem',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}
    >
      <div>
        <Link href="/">
          <strong>Performance Tracker</strong>
        </Link>
      </div>
      <button onClick={handleSignOut}>Sign out</button>
    </nav>
  );
}