import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# funcion a testear
def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert  calculate_total([]) == 0
    
def test_calculate_total_with_single_product():
    product = [
        {
            "name" : "Pasta",
            "price" : 8
        }
    ]
    assert calculate_total(product) == 8
    

def test_calculate_total_with_multiple_products():
    product = [
        {
            "name" : "Pasta",
            "price" : 8
        },
        {
            "name" : "Arroz",
            "price" : 5
        },
        {
            "name" : "Frijol",
            "price" : 2
        }
    ]
    assert calculate_total(product) == 15

def is_api_available(url,key):
    url = f"{url}{key}/latest/COP"
    response = requests.get(url)
    return True if response.status_code == 200 else False

def money_conversion(money_from, money_to, mount, url, key):
    url = f"{url}{key}/pair/{money_from}/{money_to}/{mount}"
    response = requests.get(url)
    return response.json()['conversion_result']

load_dotenv("./.env")   

api_key = os.getenv("api_key_currency")
url_base = os.getenv("url_base")
pprint(money_conversion("COP", "USD",2000, url_base, api_key))