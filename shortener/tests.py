from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from .forms import URLShortenerForm


class URLShortenerFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = URLShortenerForm(data={"url": "http://google.com", "name":"google"})
        
        self.assertTrue(
            form.is_valid()
        )