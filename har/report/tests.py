from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Report

class HeritageAtRiskTests(TestCase):
    def setUp(self):
        # Create two distinct users for testing security boundaries
        self.user1 = User.objects.create_user(username='user1@test.com', password='password123')
        self.user2 = User.objects.create_user(username='user2@test.com', password='password123')
        
        # Create a report owned by user1
        self.report1 = Report.objects.create(
            name="Ancient Temple",
            user=self.user1,
            latitude=10.123,
            longitude=20.456,
            altitude=100.0,
            accuracy=5.0
        )
        self.client = Client()

    ## --- Connection Logic Tests ---

    def test_connection_auto_registration(self):
        """Test that a new email/password automatically creates an account (Waypoint 4/9)."""
        response = self.client.post(reverse('connection'), {
            'email': 'newuser@test.com',
            'password': 'newpassword'
        })
        # Should redirect to reports list after auto-signup
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser@test.com').exists())

    def test_connection_invalid_password(self):
        """Test that existing user with wrong password fails."""
        response = self.client.post(reverse('connection'), {
            'email': 'user1@test.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid password")

    ## --- Security & Ownership Tests ---

    def test_view_protection_redirects_anonymous(self):
        """Test that unauthenticated users are redirected to login."""
        response = self.client.get(reverse('reports_list'))
        self.assertEqual(response.status_code, 302)

    def test_user_isolation_list(self):
        """Test that User 2 cannot see User 1's reports."""
        self.client.login(username='user2@test.com', password='password123')
        response = self.client.get(reverse('reports_list'))
        # Should NOT contain user1's report name
        self.assertNotContains(response, "Ancient Temple")

    def test_unauthorized_deletion(self):
        """Test that User 2 cannot delete User 1's report (Waypoint 9)."""
        self.client.login(username='user2@test.com', password='password123')
        # Try to delete report1 (owned by user1)
        response = self.client.get(reverse('report_delete', args=[self.report1.id]))
        # Should return 404 because of get_object_or_404(user=request.user) logic
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Report.objects.filter(id=self.report1.id).exists())

    ## --- CRUD Functional Tests ---

    def test_report_creation(self):
        """Test creating a new report correctly assigns the logged-in user."""
        self.client.login(username='user1@test.com', password='password123')
        response = self.client.post(reverse('report_create'), {
            'name': 'Old Statue',
            'latitude': 12.34,
            'longitude': 56.78,
            'altitude': 10.0,
            'accuracy': 1.0
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Report.objects.filter(name='Old Statue', user=self.user1).exists())

    def test_report_update(self):
        """Test that a user can update their own report."""
        self.client.login(username='user1@test.com', password='password123')
        response = self.client.post(reverse('report_update', args=[self.report1.id]), {
            'name': 'Updated Temple Name',
            'latitude': 10.123,
            'longitude': 20.456,
            'altitude': 100.0,
