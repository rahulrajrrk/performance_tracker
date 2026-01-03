import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Employee dashboard page.
 *
 * Displays analytics and summaries specific to the logged‑in employee.
 */
export default function EmployeeDashboard() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Employee Dashboard</h2>
        <p>
          This page will show the employee’s total calls, payments, incentives and
          other statistics for the selected month.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}