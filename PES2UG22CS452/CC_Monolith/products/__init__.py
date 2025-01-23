from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict):
        """
        Class method to create a Product instance from a dictionary.
        """
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty']
        )


def list_products() -> list[Product]:
    """
    Fetches all products from the database and returns them as a list of Product instances.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """
    Fetches a single product by its ID and returns it as a Product instance.
    """
    product_data = dao.get_product(product_id)
    if product_data is None:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product: dict):
    """
    Adds a new product to the database.
    """
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product.keys()):
        raise ValueError(f"Product data must include keys: {required_keys}")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product by its ID.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    if dao.get_product(product_id) is None:
        raise ValueError(f"Product with ID {product_id} not found.")
    dao.update_qty(product_id, qty)

