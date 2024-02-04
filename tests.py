import unittest
import app
import currency

class CurrencyConverterTest(unittest.TestCase):

    def setUp(self):
        app.app.testing=True
        self.app=app.app.test_client()
    
    def test_home_page(self):
        response=self.app.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_conversion(self):
        result=currency.convert_currency("USD", "CAD", 200)
        self.assertIsNone(result)

if __name__=='__main__':
    unittest.main()