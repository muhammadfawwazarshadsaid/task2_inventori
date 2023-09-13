from django.test import TestCase, Client

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_image_element_exists(self):
        response = Client().get('/main/')
        self.assertContains(response, '<img')
        
    def test_main_context_structure(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

        # Memeriksa struktur konteks yang diharapkan
        expected_context = [
            {
                'no': 1,
                'name': 'Kandang Kucing',
                'description': "Kandang kucing dengan anti karat dan anti bau",
                'amount': 5,
                'price': 74000,
            },
            {
                'no': 2,
                'name': 'Pasir 200g',
                'description': "Pasir putih anti lengket",
                'amount': 91,
                'price': 10000,
            },
            {
                'no': 3,
                'name': 'Royal Candi 1kg',
                'description': "Makanan kucing berkualitas premium",
                'amount': 241,
                'price': 240000,
            }
        ]

        actual_context = response.context['items']
        self.assertEqual(len(actual_context), len(expected_context))

        for i in range(len(expected_context)):
            self.assertEqual(actual_context[i]['no'], expected_context[i]['no'])
            self.assertEqual(actual_context[i]['name'], expected_context[i]['name'])
            self.assertEqual(actual_context[i]['description'], expected_context[i]['description'])
            self.assertEqual(actual_context[i]['amount'], expected_context[i]['amount'])
            self.assertEqual(actual_context[i]['price'], expected_context[i]['price'])