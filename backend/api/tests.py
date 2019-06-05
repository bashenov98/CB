from django.test import TestCase
from api.models import Company, Review, ReviewManager
from django.contrib.auth.models import User
from api.serializers import ReviewSerializer, CompanySerializer
from api.views.generic_cbv import CompanyList, ReviewList
from api.views.auth import login, logout
from django.test import Client
# Create your tests here.

class CompanyTest(TestCase):
    def create_company(self, name = "test_company", bio = "test"):
        return Company.objects.create(name = name,
                                      bio=bio)

    def test_company_creation(self):
        a = self.create_company()
        self.assertTrue(isinstance(a,Company))

class AuthTest(TestCase):
    def test_login(self):
        # Get login page
        response = self.client.get('/admin/')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

        # Log the user in
        self.client.login(username='XXX', password="XXX")

        # Check response code
        response = self.client.get('/api/login')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        response = self.client.get('api/login')
        self.assertEqual(response.status_code, 200)
        # user = User.objects.create(self, username='testuser')
        # user.set_password('12345')
        # user.save()
        #
        # c = Client()
        # logged_in = c.login(username='testuser', password='12345')
        # self.assertTrue(logged_in)1

    # user = User.objects.create(username='testuser', password='12345')
    # login = self.client.login(username='homer', password='simpson')
    # self.assertTrue(login)

#
# class ReviewTest(TestCase):
#     def test_str(self):
#
#
# class ReviewManagerTest(TestCase):
#     def test_for_user(self):
#         b = Review.t
#         c = self.ReviewManager.for_user(self,b.created_by)
#         d = self.filter(created_by=b.created_by)
#         self.assertEqual(c, d)
#
# class ReviewTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create()
#     def create_review(self,
#                       title = "test_review",
#                       rating = 3,
#                       ip_address = "127.0.0.1",
#                       summary = "test",
comapny  =
#                       submissionDate = "13.12.2018",
#                       company = CompanyTest.create_company(),
#                       user = 1):
#         return Review.objects.create(title=title,
#                                      rating = rating,
#                                      ip_address = ip_address,
#                                      summary = summary,
#                                      submissionDate = submissionDate,
#                                      company = company,
#                                      user = user)
#
#     def test_review_creation(self):
#         b = self.create_review()
#         self.assertTrue(isinstance(b,Review))
# #
# class AuthTest(TestCase):
#     user = User.objects.create(username='testuser')
#     user.set_password('12345')
#     user.save()
#
#     c = Client()
#     logged_in = c.login(username='testuser', password='12345')
#     self.assertTrue(login)
#     # user = User.objects.create(username='testuser', password='12345')
#     # login = self.client.login(username='homer', password='simpson')
#     # self.assertTrue(login)