from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):
    def setUp(self):
        self.response=self.client.get("/")
    
    def test_url_home(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_plantilla_home(self):
        self.assertTemplateUsed(self.response,"base/home.html")
        self.assertContains(self.response,"Aplicacion")
