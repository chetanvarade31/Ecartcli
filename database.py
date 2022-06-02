import sqlite3
from typing import List
from model import Cart, Category, Product, User, OrderBills

conn = sqlite3.connect('Ecart.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS User (
            username text,
            password text   
            )""")

    # category table for products
    c.execute("""CREATE TABLE IF NOT EXISTS Category (
            category text
            )""")

    # creating product table for adding products
    c.execute("CREATE TABLE IF NOT EXISTS Product (id integer primary key autoincrement, name text, category text, price integer, date text )")

    # creating cart 
    c.execute("CREATE TABLE IF NOT EXISTS Cart (id integer primary key autoincrement, username text, name text, category_name text, price integer, date text )")
    # creating table orderBills for user and admin
    c.execute("CREATE TABLE IF NOT EXISTS OrderBills (id integer primary key autoincrement, username text, no_of_product integer, actual_amount integer, discounted_amount integer, final_amount integer )")


    # c.execute("INSERT INTO User (username, password) VALUES (?,?)",("Admin",'admin@31'))
    # conn.commit()

create_table()


def insert_cart(cart: Cart):
    c.execute('select count(*) FROM Cart')
    c.execute("INSERT INTO Cart (username, category_name,name, price, date) VALUES (?,?,?,?,?)",(cart.username, cart.name, cart.category_name, cart.price, cart.date))
    conn.commit()


def insert_order(order: OrderBills):
    c.execute('select count(*) FROM OrderBills')
    c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(order.username, order.no_of_product, order.actual_amount, order.discounted_amount, order.final_amount))
    conn.commit()


def insert_category(cate : Category ):
    c.execute('select count(*) FROM Category')
    
    with conn:
        c.execute('INSERT INTO Category VALUES (:category)',
        {'category':cate.category})


def addproduct(pro: Product):
    c.execute('select count(*) FROM Product')
    c.execute("INSERT INTO Product (name, category, price, date) VALUES (?,?,?,?)",(pro.name, pro.category, pro.price, pro.date))
    conn.commit()


def get_all_cart(username = None) -> List[Cart]:
    print('hii : ',username)
    if username is not None:
        c.execute(f"select * from Cart WHERE username = '{username}' ")
        results = c.fetchall()
        print(results)
        cart: List = []
        for result in results:
            cart.append(Cart(*result))
        return cart

    else:
        c.execute('select * from Cart')
        results = c.fetchall()
        cart: List = []
        for result in results:
            cart.append(Cart(*result))
        return cart


def get_all_order(username = None) -> List[OrderBills]:
    if username is not None:
        c.execute(f"select * from OrderBills WHERE username = '{username}' ")
        results = c.fetchall()
        order: List = []
        for result in results:
            order.append(OrderBills(*result))
        return order

    else:
        c.execute(f" select * from OrderBills ")
        results = c.fetchall()
        order: List = []
        for result in results:
            order.append(OrderBills(*result))
        return order


def new_user(nuser: User):
    if nuser.password == nuser.repassword:
        with conn:
            c.execute('INSERT INTO User VALUES (:username, :password)',
            {'username':nuser.username,'password':nuser.password})
    else:
        print('Password did not Match')


def showusers() -> List[User]:
    c.execute('select * from User')
    results = c.fetchall()
    users: List = []
    for result in results:
        users.append(User(*result))
    return users


def showcategory() -> List[Category]:
    c.execute('select * from Category')
    results = c.fetchall()
    cate: List = []
    for result in results:
        cate.append(Category(*result))
    return cate


def showproduct(categ = None) -> List[Product]:
    if categ is not None:
        c.execute(f" select * from Product WHERE category='{categ}'")
        results = c.fetchall()
        pro: List = []
        for result in results:
            pro.append(Product(*result))
        return pro
    else:
        c.execute(f'select * from Product')
        results = c.fetchall()
        pro:List = []
        for result in results:
            pro.append(Product(*result))
        return pro




 