from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def SetUp(self):
        print('aqui')
        # user_data = {
        #     'username': 'test',
        #     'email': 'test@test.com',
        #     'password':'test1234'
        # }
        # User.objects.create_user(**user_data)
        # User.objects.create_user('test', 'test@test.com', 'test12343')
        User.objects.create_user('foo', 'myemail@test.com', 'bar')

    def test_profile_exists(self):
        # exists = Profile.objects.filter(user__username='test').exists()
        # exists = Profile.objects.filter(user__username='foo').exists()
        exists = User.objects.filter(username='foo').exists()
        # self.assertEqual(exists, True)