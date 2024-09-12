class Types:
    def __init__(self, name):
        self.name = name
        self.subtypes = {}
    
    def add_subtype(self, subtype_name):
        if subtype_name not in self.subtypes:
            self.subtypes[subtype_name] = Subtypes(subtype_name)
        else:
            print(f"Subtype '{subtype_name}' already exists under '{self.name}'.")

    def add_product(self, subtype_name, product):
        if subtype_name in self.subtypes:
            self.subtypes[subtype_name].add_product(product)
        else:
            print(f"Subtype '{subtype_name}' does not exist in '{self.name}'. Please create it first.")
    
    def display_types(self):
        print(f"Type: {self.name}")
        for subtype_name, subtype in self.subtypes.items():
            print(f"  Subtype: {subtype_name}")
            subtype.display_products()

class Subtypes:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def display_products(self):
        for product in self.products:
            product.display_product_details()

class Product:
    def __init__(self, name, weight, price, type_obj, subtype_obj):
        self.name = name
        self.weight = weight
        self.price = price
        self.type_obj = type_obj
        self.subtype_obj = subtype_obj
    
    def display_product_details(self):
        print(f"    Product: {self.name}")
        print(f"    Weight: {self.weight} kg")
        print(f"    Price: ${self.price}")
        print(f"    Type: {self.type_obj.name}")
        print(f"    Subtype: {self.subtype_obj.name}")
        
# Example Usage

# Create the main types
food = Types("Food")
cleaning = Types("Cleaning Supplies")

# Add subtypes
food.add_subtype("Meat")
food.add_subtype("Red Meat")
cleaning.add_subtype("Windex")

# Create products
cow_meat = Product(name="Cow Meat", weight=5, price=50, type_obj=food, subtype_obj=food.subtypes["Red Meat"])
windex_ype = Product(name="Windex Ype", weight=100, price=10, type_obj=cleaning, subtype_obj=cleaning.subtypes["Windex"])

# Add the products to the appropriate subtypes
food.add_product("Red Meat", cow_meat)
cleaning.add_product("Windex", windex_ype)

# Display the hierarchy
food.display_types()
cleaning.display_types()
