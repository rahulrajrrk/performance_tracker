import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Admin master settings page.
 *
 * Allows admins to define services, set the base percentages for each
 * incentive and configure the global incentive percentage.  Only admins can
 * access this page.
 */
export default function AdminMaster() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Master Settings</h2>
        <p>
          Use this page to define the list of services (e.g. WhatsApp API,
          RCS, Bulk SMS, Voice Calls, Email) and set the base percentage for
          incentive calculations.  You can also configure the global incentive
          percentage applicable to all services.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}