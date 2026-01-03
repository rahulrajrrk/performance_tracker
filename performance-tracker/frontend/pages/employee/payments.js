import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Employee payments page.
 *
 * Allows the employee to record multiple payments and view their payment
 * history.  Incentives are generated automatically by the backend.
 */
export default function EmployeePayments() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Payments</h2>
        <p>
          A form for entering payments (customer name, mobile, new/repeat,
          service, amount, card link, notes) will be implemented here.
        </p>
        <p>
          Below the form, a table of past payments with filters by date,
          service, and customer type will appear.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}