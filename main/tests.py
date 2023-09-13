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
        # Ganti "brand.png" dengan src yang sesuai untuk gambar yang ingin Anda periksa
        self.assertContains(response, 'src="templates/logo.png"')
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

        actual_context = response.context  
        self.assertEqual(actual_context['no'], expected_context[0]['no'])
        self.assertEqual(actual_context['name'], expected_context[0]['name'])
        self.assertEqual(actual_context['description'], expected_context[0]['description'])
        self.assertEqual(actual_context['amount'], expected_context[0]['amount'])
        self.assertEqual(actual_context['price'], expected_context[0]['price'])
        
        self.assertEqual(actual_context['no'], expected_context[1]['no'])
        self.assertEqual(actual_context['name'], expected_context[1]['name'])
        self.assertEqual(actual_context['description'], expected_context[1]['description'])
        self.assertEqual(actual_context['amount'], expected_context[1]['amount'])
        self.assertEqual(actual_context['price'], expected_context[1]['price'])

        self.assertEqual(actual_context['no'], expected_context[2]['no'])
        self.assertEqual(actual_context['name'], expected_context[2]['name'])
        self.assertEqual(actual_context['description'], expected_context[2]['description'])
        self.assertEqual(actual_context['amount'], expected_context[2]['amount'])
        self.assertEqual(actual_context['price'], expected_context[2]['price'])
