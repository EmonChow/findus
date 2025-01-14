from django.test import TestCase
from authentication.models import *


from django.test import TestCase
from authentication.models import Permission

class PermissionTestCase(TestCase):
    def setUp(self):
        self.permission = Permission.objects.create(
            
            name='TEST',  # TODO: Set appropriate test value
            
            created_at=None,  # TODO: Set appropriate test value
            
            updated_at=None,  # TODO: Set appropriate test value
            
            created_by=None,  # TODO: Set appropriate test value
            
            updated_by=None,  # TODO: Set appropriate test value
            
        )

    def test_create_permission(self):
        self.assertIsInstance(self.permission, Permission)

    def test_str_permission(self):
        self.assertEqual(str(self.permission), 'TEST')  # TODO: Update expected string representation


from django.test import TestCase
from authentication.models import Role

class RoleTestCase(TestCase):
    def setUp(self):
        self.role = Role.objects.create(
            
            name='TEST',  # TODO: Set appropriate test value
            
            created_at=None,  # TODO: Set appropriate test value
            
            updated_at=None,  # TODO: Set appropriate test value
            
            created_by=None,  # TODO: Set appropriate test value
            
            updated_by=None,  # TODO: Set appropriate test value
            
        )

    def test_create_role(self):
        self.assertIsInstance(self.role, Role)

    def test_str_role(self):
        self.assertEqual(str(self.role), 'TEST')  # TODO: Update expected string representation


from django.test import TestCase
from authentication.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            
            password='TEST',  # TODO: Set appropriate test value
            
            last_login=None,  # TODO: Set appropriate test value
            
            first_name=None,  # TODO: Set appropriate test value
            
            last_name=None,  # TODO: Set appropriate test value
            
            username=None,  # TODO: Set appropriate test value
            
            email=None,  # TODO: Set appropriate test value
            
            gender='male',  # TODO: Set appropriate test value
            
            user_type='TEST',  # TODO: Set appropriate test value
            
            date_of_birth=None,  # TODO: Set appropriate test value
            
            is_active=True,  # TODO: Set appropriate test value
            
            is_admin=False,  # TODO: Set appropriate test value
            
            role=None,  # TODO: Set appropriate test value
            
            primary_phone=None,  # TODO: Set appropriate test value
            
            secondary_phone=None,  # TODO: Set appropriate test value
            
            image=None,  # TODO: Set appropriate test value
            
            created_at=None,  # TODO: Set appropriate test value
            
            updated_at=None,  # TODO: Set appropriate test value
            
            deleted_at=None,  # TODO: Set appropriate test value
            
            created_by=None,  # TODO: Set appropriate test value
            
            updated_by=None,  # TODO: Set appropriate test value
            
        )

    def test_create_user(self):
        self.assertIsInstance(self.user, User)

    def test_str_user(self):
        self.assertEqual(str(self.user), '')  # TODO: Update expected string representation


from django.test import TestCase
from authentication.models import LoginHistory

class LoginHistoryTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="testuser",
            email="testuser@example.com",
            first_name="Test",
            last_name="User"
        )
        self.loginhistory = LoginHistory.objects.create(
            
            user=self.test_user,  # TODO: Set appropriate test value
            
            ip_address=None,  # TODO: Set appropriate test value
            
            mac_address=None,  # TODO: Set appropriate test value
            
            g_location_info=None,  # TODO: Set appropriate test value
            
            is_device_blocked=False,  # TODO: Set appropriate test value
            
            login_time=None,  # TODO: Set appropriate test value
            
            logout_time=None,  # TODO: Set appropriate test value
            
            status=None,  # TODO: Set appropriate test value
            
            created_at=None,  # TODO: Set appropriate test value
            
            updated_at=None,  # TODO: Set appropriate test value
            
            created_by=None,  # TODO: Set appropriate test value
            
            updated_by=None,  # TODO: Set appropriate test value
            
        )

    def test_create_loginhistory(self):
        self.assertIsInstance(self.loginhistory, LoginHistory)

    def test_str_loginhistory(self):
        self.assertEqual(str(self.loginhistory), f'{self.test_user}')  # TODO: Update expected string representation


from django.test import TestCase
from authentication.models import ActivityLog

class ActivityLogTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="testuser",
            email="testuser@example.com",
            first_name="Test",
            last_name="User"
        )

        self.activitylog = ActivityLog.objects.create(
            
            activity_by=self.test_user,  # TODO: Set appropriate test value
            
            comment=None,  # TODO: Set appropriate test value
            
            created_at=None,  # TODO: Set appropriate test value
            
        )

    def test_create_activitylog(self):
        self.assertIsInstance(self.activitylog, ActivityLog)

    def test_str_activitylog(self):
        expected_str = f"{self.test_user}"
        self.assertEqual(str(self.activitylog), expected_str)
