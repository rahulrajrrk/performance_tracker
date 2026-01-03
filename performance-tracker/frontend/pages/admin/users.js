import Layout from '../../components/Layout';
import ProtectedRoute from '../../components/ProtectedRoute';

/**
 * Admin user management page.
 *
 * Allows the administrator to create users (email, password, role) and
 * assign employees to managers.  Only admins can access this page.
 */
export default function AdminUsers() {
  return (
    <ProtectedRoute>
      <Layout>
        <h2>User Management</h2>
        <p>
          This page will provide forms to create new users and assign them
          roles (Employee, Manager, Admin).  Admins can also map employees
          to managers and remap existing relationships.
        </p>
      </Layout>
    </ProtectedRoute>
  );
}