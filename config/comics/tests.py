from django.test import TestCase, Client

class ComicViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_settings_view_status_code(self):
        response = self.client.get('/settings/')
        self.assertEqual(response.status_code, 200)