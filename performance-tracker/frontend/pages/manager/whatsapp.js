import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Manager WhatsApp monthly payments page.
 *
 * Shows upcoming WhatsApp API monthly payments (due today and due this week)
 * and provides a form to record new monthly payments for customers.  Only
 * managers and admins can access this page.
 */
export default function ManagerWhatsApp() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>WhatsApp Monthly Payments</h2>
        <p>
          This page will show payments due today and this week.  You can also
          add new monthly payments and manage customer subscriptions.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}