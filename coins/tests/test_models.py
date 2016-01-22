from django.test import TestCase

from .models import CatalogCoin

# models test
class CatalogCoinTest(TestCase):

    def create_catalogcoin(self, face_value=25, currency="franks"):
        return CatalogCoin.objects.create(face_value=face_value, currency=currency)

    def test_catalogcoin_creation(self):
        coin = self.create_catalogcoin()
        self.assertTrue(isinstance(w, CatalogCoin))
        self.assertEqual(coin.__unicode__(), "{} {}".(coin.face_value, coin.currency))
