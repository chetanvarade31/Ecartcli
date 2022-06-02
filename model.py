class Cart():
    def __init__(self,id ,username,name, category_name, price, date):
        self.id = id
        self.username = username
        self.name = name
        self.category_name = category_name
        self.price = price 
        self.date = date

    def __repr__(self) -> str:
        return f"({self.id},{self.username},{self.name}, {self.category_name}, {self.price}, {self.date})"


class User():
    def __init__(self,username, password,repassword = None):
        self.username = username
        self.password = password
        self.repassword = repassword

    def __repr__(self) -> str:
        return f"({self.username},{self.password},{self.repassword})"

class Category():
    def __init__(self,category):
        self.category = category
       

    def __repr__(self) -> str:
        return f"({self.category})"



class Product():
    def __init__(self,id,name, category, price, date):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.date = date

    def __repr__(self) -> str:
        return f"({self.id},{self.name},{self.category},{self.price},{self.date})"

class OrderBills():
    def __init__(self,id,username, no_of_product, actual_amount, discounted_amount, final_amount):
        self.id = id
        self.username = username
        self.no_of_product = no_of_product
        self.actual_amount = actual_amount
        self.discounted_amount = discounted_amount
        self.final_amount = final_amount

    def __repr__(self) -> str:
        return f"({self.id},{self.username},{self.no_of_product},{self.actual_amount},{self.discounted_amount},{self.final_amount})"