from msilib.schema import Class
from typing import List
import typer
from rich.console import Console
from rich.table import Table
from model import Cart, Category, OrderBills, Product, User
from database import Action

console = Console()
apps = typer.Typer()
class Ecart():
    def __init__(self) -> None:
        self.ac = Action()
        self.c = self.ac.conn.cursor()

class CategoryClass(Ecart):

    def add_category(self,category: str):
        self.cate = Category(category)
        try:
            self.ac.insert_category(self.cate)
            self.show_category()
            return True

        except Exception as e:
            console.log(e)
            return False

    def show_category(self):
        self.cate = self.ac.showcategory()
        console.print("[bold magenta]Category[/bold magenta]!", "💻")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Category", min_width=20)
    
        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
            if category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, cate in enumerate(self.cate, start=1):
            c = get_category_color(cate.category) 
            table.add_row(str(idx), cate.category)
        console.print(table)
        return self.cate

class ProductClass(CategoryClass):
    def add_product(self,name: str,category:str,price:str,date:str):
        try:
            self.cate = Product(id = id,name=name,category=category,price = price ,date=date)
            self.ac.addproduct(self.cate)
            self.products()
            return True

        except Exception as e:
            console.log(e)
            return False

    def products(self,cate = None):
        self.cate = cate
        self.tasks = self.ac.showproduct(categ= self.cate)
        console.print("[bold magenta]Product[/bold magenta]!", "💻")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("name", min_width=20)
        table.add_column("category", min_width=12, justify="right")
        table.add_column("price", min_width=12, justify="right")
        table.add_column("date", min_width=12, justify="right")

        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
            if category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, pro in enumerate(self.tasks, start=1):
            c = get_category_color(pro)
            table.add_row(str(pro.id),pro.name,f'[{c}]{pro.category}[/{c}]',f'[{c}]{pro.price}[/{c}]',f'[{c}]{pro.date}[/{c}]')
        console.print(table)
        return self.tasks

class UserClass(ProductClass):

    @staticmethod
    @apps.command()
    def newuser(username:str,password:str,repassword:str):
        print('User Created !!! You can Login now ')
        nuser = User(username,password,repassword)
        obj.ac.new_user(nuser)    

    
    def users(self):
        self.users = self.ac.show_admin()
        console.print("[bold magenta]Users[/bold magenta]!", "💻")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Username", min_width=20)
        table.add_column("Password", min_width=12, justify="right")
        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
            if category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, user in enumerate(self.users, start=1):
            c = get_category_color(user.username)
            table.add_row(str(idx), user.username, f'[{c}]{user.password}[/{c}]')
        console.print(table)

    

    

    @staticmethod
    @apps.command()
    def adminlogin():
        username,password = input('Enter Username and Password : ').split()
        obj.ac.c.execute(f"SELECT username  from User WHERE username='{username}' AND password = '{password}'")
        results = obj.ac.c.fetchall()
        cred : List = []
        for result in results:
            cred.append(result)
        if cred:
            while True:
                print('1 Add Category\n2 Add Product\n3 Check Cart\n4 Check Order\n5 Exist')
                choice = input("Enter the option name : ")

                if choice == 'Add Category':
                    cate  = input('Enter the Category name : ')
                    obj.add_category(cate)
                    
                elif choice == 'Add Product':
                    name, category, price, date = input(" Enter 'name' 'category' 'price' 'date' : ").split()
                    obj.add_product(name,category,price,date)
                    
                elif choice == "Check Cart":
                    obj.showcart()
                elif choice == "Check Order":
                    obj.showorder()
                elif choice == "Exist":
                    break
        else:
            print("Incorrect Username and Password")
            
    @staticmethod
    @apps.command()
    def userlogin():
        username,password = input('Enter Username and Password : ').split()
        obj.c.execute(f"SELECT username  from User WHERE username='{username}' AND password = '{password}'")
        results = obj.c.fetchall()
        cred: List = []
        for result in results:
            cred.append(result)

        if cred:
            obj.show_category()
            categ  = input('Enter the Category name : ')
            obj.products(categ)
            choice = str(input("1 : Enter the Product ID to add in the Cart :\n2 : Type 'cart' to Show Cart :  "))
        
            if choice == "cart":
                obj.showcart(username= username)
            else:
                obj.c.execute(f"SELECT * from Product WHERE id = '{choice}' ")
                resu = obj.c.fetchone()
                cart = Cart(id,username=username,category_name=resu[2],name=resu[1],price = resu[3],date= resu[4])
                obj.ac.insert_cart(cart=cart)
                obj.showcart(username= username)
                
            while True:
                print('1 : Enter 1 for remove product from Cart :\n2 : Buy multiple product by Entering 2 :\n3 : Enter 3 to buy single product  : \n4 : Enter 4 For Exist :  ')
                choice1 = int(input('Enter the option : '))

                if choice1 == 1:
                    choice = int(input('Enter the product id : '))
                    obj.c.execute(f" DELETE  from Cart WHERE id = '{choice}' ")
                    obj.ac.conn.commit()
                    obj.showcart(username= username)

                elif choice1 == 2:
                    choice = tuple(map(int,input("Enter id of the prodcuts using ',' separated :  ").split(',')))
                    obj.c.execute(f" SELECT SUM(price) from Cart WHERE id in {choice} ")
                    resu = obj.c.fetchall()
                    p = resu[0]
                    
                    no_of_product = len(choice)
                    price = p[0]
                    total_price = p[0]
                    discounted_price = 0
                    if total_price  > 10000:
                        total_price -= 500
                        discounted_price += total_price
                    final_price = total_price
                    
                    obj.c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(username, no_of_product, price, discounted_price, final_price))
                    obj.ac.conn.commit()
                    obj.showorder(username=username)

                elif choice1 == 3:
                    choice = int(input("Enter product id to Buy :  "))
                    obj.c.execute(f" SELECT SUM(price) from Cart WHERE id = '{choice}' ")
                    resu = obj.c.fetchall()
                    p = resu[0]
                    
                    no_of_product = 1
                    price = p[0]
                    total_price = p[0]
                    discounted_price = 0
                    if total_price  > 10000:
                        total_price -= 500
                        discounted_price += total_price
                    final_price = total_price
                    
                    obj.c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(username, no_of_product, price, discounted_price, final_price))
                    obj.ac.conn.commit()
                    obj.showorder(username= obj.username)

                elif choice1 == 4:
                    break

class CartClass(ProductClass):
    def add_tocart(self,username: str,name: str,category_name:str,price:int,date:str):
        try:
            self.cate = Cart(id = id,username=username,name=name,category_name=category_name,price=price,date=date)
            self.ac.insert_cart(self.cate)
            self.showcart()
            return True

        except Exception as e:
            console.log(e)
            return False

    def showcart(self,username = None)-> List:
        self.username = username
        self.tasks = self.ac.get_all_cart(self.username)
        console.print("[bold magenta]Cart[/bold magenta]!", "💻")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("id", style="dim", width=6)
        table.add_column("Name", min_width=20)
        table.add_column("Username", min_width=20)
        table.add_column("Category", min_width=12, justify="right")
        table.add_column("Price", min_width=12, justify="right")
        table.add_column("Date", min_width=12, justify="right")

        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
            if category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, cart in enumerate(self.tasks, start=1):
            c = get_category_color(cart)
            table.add_row(str(cart.id),cart.name,f'[{c}]{cart.username}[/{c}]',f'[{c}]{cart.category_name}[/{c}]',f'[{c}]{cart.price}[/{c}]',f'[{c}]{cart.date}[/{c}]')

        console.print(table)  
        return self.tasks


class OrderClass(CartClass):
    def add_toorder(self,username: str,no_of_product: int,actual_amount:int,discounted_amount:int,final_amount:int):
        try:
            self.cate = OrderBills(id = id,username=username,no_of_product= no_of_product,actual_amount=actual_amount,discounted_amount=discounted_amount,final_amount=final_amount)
            self.ac.insert_order(self.cate)
            self.showorder()
            return True

        except Exception as e:
            console.log(e)
            return False

    def showorder(self,username = None):
        self.username = username
        self.order = self.ac.get_all_order(username = self.username)
        if self.order is  None:
            print('No order yet !!')
        else:
            console.print("[bold magenta]Bills[/bold magenta]!", "💻")

            table = Table(show_header=True, header_style="bold blue")
            table.add_column("id", style="dim", width=6)
            table.add_column("Username", min_width=20)
            table.add_column("No of Product", min_width=20)
            table.add_column("Actual Amount", min_width=12, justify="right")
            table.add_column("Discounted Amount", min_width=12, justify="right")
            table.add_column("Final Amount", min_width=12, justify="right")

            def get_category_color(category):
                COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
                if category in COLORS:
                    return COLORS[category]
                return 'white'

            for idx, ord in enumerate(self.order, start=1):
                c = get_category_color(ord.username)   
                table.add_row(str(ord.id),ord.username,f'[{c}]{ord.no_of_product}[/{c}]',f'[{c}]{ord.actual_amount}[/{c}]', f'[{c}]{ord.discounted_amount}[/{c}]',f'[{c}]{ord.final_amount}[/{c}]')
            console.print(table)
            return self.order
    

if __name__ == "__main__":
        
        obj = OrderClass()
        apps()
    


    
