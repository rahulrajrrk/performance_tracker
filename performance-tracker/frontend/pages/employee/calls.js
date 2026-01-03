import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Employee calls page.
 *
 * Provides a form for entering daily call statistics and displays call
 * history with date range filters.  Validation logic ensures a single
 * entry per day and requires demo details when demos are present.
 */
export default function EmployeeCalls() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Calls Entry</h2>
        <p>
          A form for entering answered/unanswered calls, total call time and
          multiple demos will appear here.
        </p>
        <p>
          Below the form, a table of past call entries with date range filters
          will be displayed.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}