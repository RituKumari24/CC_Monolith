import json

import products
from cart import dao
from products import Product
from typing import List


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        # Safely load the Cart data
        contents = [products.get_product(product_id) for product_id in data['contents']]
        return Cart(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> List[Product]:
    # Retrieve the cart details from the database
    cart_details = dao.get_cart(username)
    
    if not cart_details:
        return []
    
    # Extract and process the contents from the cart details
    all_products = [
        products.get_product(product_id) 
        for cart_detail in cart_details 
        for product_id in cart_detail['contents']
    ]
    return all_products


def add_to_cart(username: str, product_id: int):
    # Directly add product to cart
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    # Remove product from cart
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    # Delete the entire cart
    dao.delete_cart(username)



