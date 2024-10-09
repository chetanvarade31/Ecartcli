from Ecart import add_category, add_tocart, newuser, showorder
from database import addproduct, get_all_order, insert_category
from model import Category, Product

def test_add_category():
    category = 'Electronic'
    expected_output = None
    ouput = add_category(category=category)
    assert ouput == expected_output


def test_add_to_cart():
    username, name, category_name, price, date = "chetan varade","Mobile", "electronic", "4560","23-5-2021"
    expected_output = None
    output = add_tocart(username= username, name= name, category_name= category_name, price= price, date= date)
    assert output == expected_output


def test_new_user():
    username, password, repassword = "chetanvarade","Chetan@31","Chetan@31"
    expected_output = None
    output = newuser(username=username, password=password, repassword= repassword)
    assert output == expected_output


def test_show_order():
    expected_output = None
    output = showorder(username=None)
    assert output == expected_output


def test_product():
    name, category, price, date = "Redmi 6A", "Electronic", "45620","23-02-2022"
    product_obj = Product(id,name=name, category= category, price= price, date= date)
    expected_output = None
    output = addproduct(product_obj)
    assert output == expected_output


def test_get_all_order():
    expected_output = type(list())
    output = get_all_order(username= None)
    assert type(output) == expected_output


def test_insert_category():
    category = 'cloth'
    category_obj = Category(category=category)
    expected_output = None
    output = insert_category(category_obj)
    assert output == expected_output

