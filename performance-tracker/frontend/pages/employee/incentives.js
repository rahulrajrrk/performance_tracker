import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Employee incentives page.
 *
 * Displays a list of incentives generated from the employee’s payments.
 */
export default function EmployeeIncentives() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Incentives</h2>
        <p>
          This page will display the incentives calculated from your payments.
          Managers and admins can view incentives for their team members by
          navigating to the manager dashboards.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}