import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Manager payments page.
 *
 * Lists all payments recorded by employees mapped to the manager with filters
 * for date range, employee and service.  Managers can edit or delete
 * payments from here.
 */
export default function ManagerPayments() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Team Payments</h2>
        <p>
          This page will provide a table of all payments made by your team
          members.  You can filter by date range, employee or service and
          edit or delete entries.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}