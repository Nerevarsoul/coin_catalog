from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexTests(TestCase):

    def test_index_page(self):
        url = reverse("index")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
