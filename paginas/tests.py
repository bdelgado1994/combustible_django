from django.test import SimpleTestCase
from django.urls import reverse

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        self.response=self.client.get("/pages/about")
        
    def test_url_about(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_page_content(self):
        self.assertTemplateUsed(self.response,"pages/about.html")
    # def test_exits_route (self):
    #     response=self.client.get("/pages/about")
    #     self.assertEqual(response.status_code,200)
    
    # def test_route_name_about(self):
    #     response=self.client.get(reverse("pages:about"))
    #     self.assertEqual(response.status_code,200)
    
    # def test_page_content(self):
    #     response=self.client.get(reverse("pages:about"))
    #     self.assertContains(response,"Aplicacion Elaborada con django")
