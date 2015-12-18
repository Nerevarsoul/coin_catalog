from django.test import TestCase

from django.contrib.auth.models import User


# Create your tests here.
class SharedTestModule(object):
    def create_user(self):
        self.user = User.objects.create_user('zeus', 'zeus@localhost', 'zeus')

    def login_client(self, username='zeus', password='zeus'):
        self.client.login(username=username, password=password)
