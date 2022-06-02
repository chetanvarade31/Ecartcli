import typer
from rich.console import Console
from rich.table import Table
from model import Cart, Category, OrderBills, Product, User
from database import addproduct, get_all_cart, get_all_order, insert_cart, insert_category, insert_order, new_user, showcategory, showproduct, showusers
from database import conn

c = conn.cursor()
console = Console()

apps = typer.Typer()


def add_category(category: str):
    cate = Category(category)
    insert_category(cate)
    show_category()
    

def add_product(name: str,category:str,price:str,date:str):
    cate = Product(id = id,name=name,category=category,price = price ,date=date)
    addproduct(cate)
    products()
    

def add_tocart(username: str,name: str,category_name:str,price:int,date:str):
    cate = Cart(id = id,username=username,name=name,category_name=category_name,price=price,date=date)
    insert_cart(cate)
    showcart()


def add_toorder(username: str,no_of_product: int,actual_amount:int,discounted_amount:int,final_amount:int):
    cate = OrderBills(id = id,username=username,no_of_product= no_of_product,actual_amount=actual_amount,discounted_amount=discounted_amount,final_amount=final_amount)
    insert_order(cate)
    showorder()


@apps.command()
def newuser(username:str,password:str,repassword:str):
    print('User Created !!! You can Login now ')
    nuser = User(username,password,repassword)
    new_user(nuser)


def showcart(username = None):
    tasks = get_all_cart(username)
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

    for idx, cart in enumerate(tasks, start=1):
        c = get_category_color(cart)
        table.add_row(str(cart.id),cart.name,f'[{c}]{cart.username}[/{c}]',f'[{c}]{cart.category_name}[/{c}]',f'[{c}]{cart.price}[/{c}]',f'[{c}]{cart.date}[/{c}]')
    console.print(table)


def showorder(username = None):
    order = get_all_order(username = username)
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

    for idx, ord in enumerate(order, start=1):
        c = get_category_color(ord.username)   
        table.add_row(str(ord.id),ord.username,f'[{c}]{ord.no_of_product}[/{c}]',f'[{c}]{ord.actual_amount}[/{c}]', f'[{c}]{ord.discounted_amount}[/{c}]',f'[{c}]{ord.final_amount}[/{c}]')
    console.print(table)


def users():
    users = showusers()
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

    for idx, user in enumerate(users, start=1):
        c = get_category_color(user.username)
        table.add_row(str(idx), user.username, f'[{c}]{user.password}[/{c}]')
    console.print(table)


def show_category():
    cate = showcategory()
    console.print("[bold magenta]Category[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Category", min_width=20)
   
    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, cate in enumerate(cate, start=1):
        c = get_category_color(cate.category) 
        table.add_row(str(idx), cate.category)
    console.print(table)


def products(cate = None):
    tasks = showproduct(categ=cate)
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

    for idx, pro in enumerate(tasks, start=1):
        c = get_category_color(pro)
        table.add_row(str(pro.id),pro.name,f'[{c}]{pro.category}[/{c}]',f'[{c}]{pro.price}[/{c}]',f'[{c}]{pro.date}[/{c}]')
    console.print(table)


@apps.command()
def adminlogin():
    username,password = input('Enter Username and Password : ').split()
    c.execute(f"SELECT username  from User WHERE username='{username}' AND password = '{password}'")
    results = c.fetchall()
    cred = []
    for result in results:
        cred.append(result)
    if cred:
        while True:
            print('1 Add Category\n2 Add Product\n3 Check Cart\n4 Check Order\n5 Exist')
            choice = input("Enter the option name : ")

            if choice == 'Add Category':
                cate  = input('Enter the Category name : ')
                add_category(cate)
                show_category()
            elif choice == 'Add Product':
                name, category, price, date = input(" Enter 'name' 'category' 'price' 'date' : ").split()
                add_product(name,category,price,date)
                products()
            elif choice == "Check Cart":
                showcart()
            elif choice == "Check Order":
                showorder()
            elif choice == "Exist":
                break
    else:
        print("Incorrect Username and Password")


@apps.command()
def userlogin():
    username,password = input('Enter Username and Password : ').split()
    c.execute(f"SELECT username  from User WHERE username='{username}' AND password = '{password}'")
    results = c.fetchall()
    cred = []
    for result in results:
        cred.append(result)

    if cred:
        show_category()
        categ  = input('Enter the Category name : ')
        products(categ)
        choice = str(input("1 : Enter the Product ID to add in the Cart :\n2 : Type 'cart' to Show Cart :  "))
    
        if choice == "cart":
            showcart(username= username)
        else:
            c.execute(f"SELECT * from Product WHERE id = '{choice}' ")
            resu = c.fetchone()
            cart = Cart(id,username=username,category_name=resu[1],name=resu[2],price = resu[3],date= resu[4])
            insert_cart(cart=cart)
            showcart(username= username)
            
        while True:
            print('1 : Enter 1 for remove product from Cart :\n2 : Buy multiple product by Entering 2 :\n3 : Enter 3 to buy single product  : \n4 : Enter 4 For Exist :  ')
            choice1 = int(input('Enter the option : '))

            if choice1 == 1:
                choice = int(input('Enter the product id : '))
                c.execute(f" DELETE  from Cart WHERE id = '{choice}' ")
                conn.commit()
                showcart(username= username)

            elif choice1 == 2:
                choice = tuple(map(int,input("Enter id of the prodcuts using ',' separated :  ").split(',')))
                c.execute(f" SELECT SUM(price) from Cart WHERE id in {choice} ")
                resu = c.fetchall()
                p = resu[0]
                
                no_of_product = len(choice)
                price = p[0]
                total_price = p[0]
                discounted_price = 0
                if total_price  > 10000:
                    total_price -= 500
                    discounted_price += total_price
                final_price = total_price
                
                c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(username, no_of_product, price, discounted_price, final_price))
                conn.commit()
                showorder(username=username)

            elif choice1 == 3:
                choice = int(input("Enter product id to Buy :  "))
                c.execute(f" SELECT SUM(price) from Cart WHERE id = '{choice}' ")
                resu = c.fetchall()
                p = resu[0]
                
                no_of_product = 1
                price = p[0]
                total_price = p[0]
                discounted_price = 0
                if total_price  > 10000:
                    total_price -= 500
                    discounted_price += total_price
                final_price = total_price
                
                c.execute("INSERT INTO OrderBills (username, no_of_product, actual_amount, discounted_amount, final_amount) VALUES (?,?,?,?,?)",(username, no_of_product, price, discounted_price, final_price))
                conn.commit()
                showorder(username= username)


if __name__ == "__main__":
    apps()
    
    