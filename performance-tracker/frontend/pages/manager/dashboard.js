import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Manager dashboard page.
 *
 * Displays separate statistics for the manager’s own performance and their
 * team’s performance.  Provides quick access to payments and analytics.
 */
export default function ManagerDashboard() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Manager Dashboard</h2>
        <p>
          This page will display your personal metrics and a summary of your
          team’s calls, payments and incentives.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}