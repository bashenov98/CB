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


class ReviewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create()

    def test_to_str(TestCase):
