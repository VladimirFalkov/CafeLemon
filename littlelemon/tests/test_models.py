from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=8, inventory=10)
        self.assertEqual(item, "IceCream : 8")

        