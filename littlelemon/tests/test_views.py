from django.test import TestCase
from restaurant.views import *

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream",price=8,inventory=10)