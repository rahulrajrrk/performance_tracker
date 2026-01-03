import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Manager analytics page.
 *
 * Shows comprehensive analytics for the manager’s team including service
 * breakdowns, day/week trends, new vs repeat customers and top customers.
 */
export default function ManagerAnalytics() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Analytics</h2>
        <p>
          Detailed charts and tables will be displayed here showing revenue
          trends, service breakdowns, new vs repeat customers and top
          customers by revenue for your team.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}