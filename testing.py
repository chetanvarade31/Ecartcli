

from typing import List

from rich import console
from Ecart import Ecart
from model import Category, Product, User

        
from database import Action

# Ecart.py file
class TestEcart():
    ec = Ecart()
    category = 'headphones'
    category_obj = Category(category=category)

    def test_add_category(self):
        self.expected_output = True
        self.ouput = self.ec.add_category(category=self.category)
        assert self.ouput == self.expected_output

    def test_add_product(self):
        self.expected_output = True
        self.ouput = self.ec.add_product("redmi 5A","mobile","3560","05-06-2022")
        assert self.ouput == self.expected_output
 
    def test_add_tocart(self):
        self.expected_output = True
        self.ouput = self.ec.add_tocart("Chetan","redmi 5A","mobile",3560,"05-06-2022")
        assert self.ouput == self.expected_output

    def test_showcart(self):
        self.expected_output = (3,"Chetan","tv","electronic",5621,"04-05-2022")
        self.lst: List = []
        for item in self.ec.showcart():
            self.lst.extend([(item.id,item.username,item.name,item.category_name,item.price,item.date)]) 
        assert self.expected_output in self.lst
    
    def test_show_category(self):
        self.expected_output = 'electronic'
        self.ouput = self.ec.show_category()
        self.lst: List  = []
        for item in self.ec.show_category():
            self.lst.append(item.category)
        assert self.expected_output in self.lst

    def test_products(self):
        self.expected_output = (1, 'tv', 'electronic', 5621, '04-05-2022')
        self.ouput = self.ec.products() 
        self.lst: List  = []
        for item in self.ec.products():
            self.lst.extend([(item.id, item.name, item.category, item.price, item.date)])
        print(self.lst)
        assert self.expected_output in self.lst


# database.py file 
class TestDatabaseAction():
    ac = Action()
    def test_get_all_cart(self):
        self.expected_output = (3, 'tv', 'electronic', 5621, '04-05-2022')
        self.lst: List  = []
        for item in self.ac.get_all_cart():
            self.lst.extend([(item.id, item.name, item.category_name, item.price, item.date)])
        print(self.lst)
        assert self.expected_output in self.lst

    def test_new_user(self):
        self.expected_output = True
        user = User(username="Test",password="test@31",repassword="test@31")
        self.output = self.ac.new_user(user)
        assert self.expected_output == self.output