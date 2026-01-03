import Navbar from './Navbar';

/**
 * Layout component that wraps pages with a navigation bar and main content area.
 */
export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main style={{ padding: '1rem' }}>{children}</main>
    </>
  );
}