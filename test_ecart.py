import unittest
from Ecart import add_category, add_tocart, newuser
from database import addproduct
from model import Product

class TestEcart(unittest.TestCase):

    def test_add_category(self):
        category = 'Electronic'
        expected_output = None
        output = add_category(category=category)
        self.assertEqual(output, expected_output)

    def test_add_to_cart(self):
        username = "chetan varade"
        name = "Mobile"
        category_name = "electronic"
        price = "4560"
        date = "23-5-2021"
        expected_output = None
        output = add_tocart(username=username, name=name, category_name=category_name, price=price, date=date)
        self.assertEqual(output, expected_output)

    def test_new_user(self):
        username = "chetanvarade"
        password = "Chetan@31"
        repassword = "Chetan@31"
        expected_output = None
        output = newuser(username=username, password=password, repassword=repassword)
        self.assertEqual(output, expected_output)

    def test_product(self):
        name = "Redmi 6A"
        category = "Electronic"
        price = "45620"
        date = "23-02-2022"
        product_obj = Product(id, name=name, category=category, price=price, date=date)
        expected_output = None
        output = addproduct(product_obj)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
