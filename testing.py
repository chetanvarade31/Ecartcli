from typing import List
import unittest
from rich import console
from Ecart import CartClass, CategoryClass, Ecart, OrderClass, ProductClass
from model import Cart, Category, OrderBills, Product, User

        
from database import Action

# Ecart.py file
  
class TestCategoryClass():
    
    ct = CategoryClass()
    category = 'headphones'
    category_obj = Category(id,category=category)

    def test_add_category(self):
        self.expected_output = True
        self.ouput = self.ct.add_category(category=self.category)
        assert self.ouput == self.expected_output

    def test_show_category(self):
        self.expected_output = 'electronic'
        self.ouput = self.ct.show_category()
        self.lst: List  = []
        for item in self.ct.show_category():
            self.lst.append(item.category)
        assert self.expected_output in self.lst

class TestProductClass():
    p = ProductClass()
    def test_add_product(self):
        self.expected_output = True
        self.ouput = self.p.add_product("redmi 5A","mobile","3560","05-06-2022")
        assert self.ouput == self.expected_output

    def test_products(self):
        self.expected_output = (1, 'vivo', 'electronic', 5669, '2-10-2021')
        self.ouput = self.p.products() 
        self.lst: List  = []
        for item in self.p.products():
            self.lst.extend([(item.id, item.name, item.category, item.price, item.date)])
        assert self.expected_output in self.lst

    

class TestCartClass():
    ec = CartClass()

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

class TestOrderClass():
    ec = OrderClass()

    def test_addtoorder(self):
        self.expected_output = True
        self.ouput = self.ec.add_toorder(username= 'Chetan',no_of_product= 1,actual_amount= 256,discounted_amount= 0,final_amount= 256)
        assert self.ouput == self.expected_output
    
   
    def test_showorder(self):
        self.expected_output = (1,'Chetan',1,8999,0,8999)
        self.lst: List = []
        for item in self.ec.showorder():
            self.lst.extend([(item.id,item.username,item.no_of_product,item.actual_amount,item.discounted_amount,item.final_amount)]) 
        assert self.expected_output in self.lst
    

class TestUserClass():
    ac = Action()

    def test_user(self):
        self.expected_output = True
        user = User(username="Test",password="test@31",repassword="test@31")
        self.output = self.ac.new_user(user)
        assert self.expected_output == self.output
    
    def test_adminlogin(self):
        self.expected_output = ('Admin','admin@31')
        self.lst: List  = []
        for item in self.ac.show_admin(username= 'Admin',password='admin@31'):
            self.lst.extend([(item[0], item[1])])
        assert self.expected_output in self.lst

# database.py file 
class TestDatabaseAction():
    
    ac = Action()
    
    def test_insert_cart(self):
        self.expected_output = True
        self.cart = Cart(id = id,username= 'Chetan',name= 'vivo',category_name= 'mobile',price= 5699,date= '08-01-2022')
        self.output = self.ac.insert_cart(cart= self.cart)
    
    def test_insert_order(self):
        self.expected_output = True
        self.order = OrderBills(id = id,username= 'Chetan',no_of_product= 2,actual_amount= 2569,discounted_amount=0,final_amount= 2569)
        self.output = self.ac.insert_order(order= self.order)
        assert self.output == self.expected_output
    
    def test_get_all_cart(self):
        self.expected_output = (3, 'tv', 'electronic', 5621, '04-05-2022')
        self.lst: List  = []
        for item in self.ac.get_all_cart():
            self.lst.extend([(item.id, item.name, item.category_name, item.price, item.date)])
        assert self.expected_output in self.lst
    
    def test_get_all_order(self):
        self.expected_output = (1, 'Chetan', 8999, 0, 8999)
        self.lst: List  = []
        for item in self.ac.get_all_order():
            self.lst.extend([(item.no_of_product, item.username, item.actual_amount, item.discounted_amount, item.final_amount)])
        assert self.expected_output in self.lst

    
