#Test for the order api

import unittest
import json
from flaskEx import app

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'[]\n')

    def test_post_order(self):
        response = self.app.post('/orders', data=json.dumps(dict(
            order_id=1,
            customer_name='John Doe',
            order_date='2020-01-01',
            items=[
                dict(
                    product_id=1,
                    quantity=2
                )
            ]
        )), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, b'Order created\n')

    def test_get_order(self):
        response = self.app.get('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"customer_name":"John Doe","items":[{"product_id":1,"quantity":2}],"order_date":"2020-01-01","order_id":1}\n')

    def test_put_order(self):
        response = self.app.put('/orders/1', data=json.dumps(dict(
            order_id=1,
            customer_name='John Doe',
            order_date='2020-01-01',
            items=[
                dict(
                    product_id=1,
                    quantity=3
                )
            ]
        )), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Order updated\n')

    def test_delete_order(self):
        response = self.app.delete('/orders/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Order deleted\n')

if __name__ == '__main__':
    unittest.main()
