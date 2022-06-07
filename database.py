import sqlite3
from typing import List
from rich import console
from model import Cart, Category, Product, User, OrderBills

class Database():
    conn = sqlite3.connect('Ecart.db')
    c = conn.cursor()

    def __init__(self) -> None:
        self.c.execute("""CREATE TABLE IF NOT EXISTS User (
            username text,
            password text   
            )""")

        # category table for products
        self.c.execute("""CREATE TABLE IF NOT EXISTS Category (
                category text
                )""")

        # creating product table for adding products
        self.c.execute("CREATE TABLE IF NOT EXISTS Product (id integer primary key autoincrement, name text, category text, price integer, date text )")

        # creating cart 
        self.c.execute("CREATE TABLE IF NOT EXISTS Cart (id integer primary key autoincrement, username text, name text, category_name text, price integer, date text )")
        # creating table orderBills for user and admin
        self.c.execute("CREATE TABLE IF NOT EXISTS OrderBills (id integer primary key autoincrement, username text, no_of_product integer, actual_amount integer, discounted_amount integer, final_amount integer )")

        # create orderbill table
        self.c.execute("CREATE TABLE IF NOT EXISTS OrderBills (id integer primary key autoincrement, username text, no_of_product integer, actual_amount integer, discounted_amount integer, final_amount integer )")

class Action(Database):
    def insert_cart(self,cart: Cart):
        self.c.execute('select count(*) FROM Cart')
        self.c.execute("INSERT INTO Cart (username, name,category_name, price, date) VALUES (?,?,?,?,?)",(cart.username, cart.name, cart.category_name, cart.price, cart.date))
        self.conn.commit()

    def insert_category(self,cate : Category ):
        self.c.execute('select count(*) FROM Category')
        with self.conn:
            self.c.execute('INSERT INTO Category VALUES (:category)',
            {'category':cate.category})
        
    def insert_order(self,order: OrderBills):
        self.c.execute('select count(*) FROM OrderBills')
        self.c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(order.username, order.no_of_product, order.actual_amount, order.discounted_amount, order.final_amount))
        self.conn.commit()

    def addproduct(self,pro: Product):
        self.c.execute('select count(*) FROM Product')
        self.c.execute("INSERT INTO Product (name, category, price, date) VALUES (?,?,?,?)",(pro.name, pro.category, pro.price, pro.date))
        self.conn.commit()

    def get_all_cart(self,username = None) -> List[Cart]:
        self.username = username   
        if self.username is not None:
            self.c.execute(f"select * from Cart WHERE username = '{self.username}' ")
            results = self.c.fetchall()
            print(results)
            self.cart: List = []
            for result in results:
                self.cart.append(Cart(*result))
            return self.cart

        else:
            self.c.execute('select * from Cart')
            results = self.c.fetchall()
            self.cart: List = []
            for result in results:
                self.cart.append(Cart(*result))
            return self.cart

    def get_all_order(self,username = None) -> List[OrderBills]:
        self.username = username
        if self.username is not None:
            self.c.execute(f"select * from OrderBills WHERE username = '{self.username}' ")
            results = self.c.fetchall()
            self.order: List = []
            for result in results:
                self.order.append(OrderBills(*result))
            return self.order

        else:
            self.c.execute(f" select * from OrderBills ")
            results = self.c.fetchall()
            self.order: List = []
            for result in results:
                self.order.append(OrderBills(*result))
                return self.order
        
    def new_user(self,nuser: User):
        if nuser.password == nuser.repassword:
            try:
                with self.conn:
                    self.c.execute('INSERT INTO User VALUES (:username, :password)',
                    {'username':nuser.username,'password':nuser.password})

                return True
            except Exception as e:
                print(e)
                return False
        else:
            print('Password did not Match')

    def showusers(self) -> List[User]:
        self.c.execute('select * from User')
        results = self.cc.fetchall()
        self.users: List = []
        for result in results:
            self.users.append(User(*result))
        return self.users

    def showcategory(self) -> List[Category]:
        self.c.execute('select * from Category')
        results = self.c.fetchall()
        self.cate: List = []
        for result in results:
            self.cate.append(Category(*result))
        return self.cate

    def showproduct(self,categ = None) -> List[Product]:
        self.categ = categ
        if self.categ is not None:
            self.c.execute(f" select * from Product WHERE category='{self.categ}'")
            results = self.c.fetchall()
            self.pro: List = []
            for result in results:
                self.pro.append(Product(*result))
            return self.pro
        else:
            self.c.execute(f'select * from Product')
            results = self.c.fetchall()
            self.pro:List = []
            for result in results:
                self.pro.append(Product(*result))
            return self.pro





