from rest_framework.test import APITestCase

from store.models import Product

class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        product_attrs = {
            'name': 'New Product', 
            'description': 'description',
            'price': 12.0,
            'sale_start':'12:01 PM 28 July 2022',      
            'sale_end':'12:01 PM 28 July 2022',      
        }
        response = self.client.post('/api/v1/products/new', product_attrs)
        if (response.status_code != 201):
            print(response.data)
        print('count',initial_product_count)
        self.assertEqual(
            Product.objects.count(), initial_product_count+1
        )
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(response.data['current_price'], product_attrs['price'])
        for attr, expected_value in product_attrs.items():
            self.assertEqual(response.data[attr], expected_value)