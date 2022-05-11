from urllib import response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):
    def test_response_list_view(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_list_view_templet(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'snack_list.html')


# We can’t easily test SnackDetailView just yet.
# Can you figure out why?
# because that the url contains param 