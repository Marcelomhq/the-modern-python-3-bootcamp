class types:
    def __init__(self, name):
        self.name = name
        self.subtypes = {}
        types_list.append(self.name)

    def add_subtypes(self, subtypes):
        if subtypes not in self.subtypes:
            self.subtypes[subtypes] = Subtypes(subtypes)

    def add_product(self, subtypes_name, product):
        if subtypes_name in self.subtypes:
            self.subtypes[subtypes_name].add_product(product)
        else:
            print(f"Subcategory '{subtypes_name}' does not exist. Please create it first.")
    
    def display_types(self):
        for n in types_list:
            print (n)
    

class Subtypes:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Product:
    def __init__(self, name, weight, price, types, subtypes):
        self.name = name
        self.weight = weight
        self.price = price
        self.types = types
        self.subtypes = subtypes

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Category: {self.types}")
        print(f"Subcategory: {self.subtypes}")
        print(f"Weight: {self.weight} kg")
        print(f"Price: ${self.price}")

types_list = []
# Example Usage

# Create the main category
food = types("Food")
cleaning = types('Cleaning Supplies')

# Add subcategories
food.add_subtypes("Meat")
food.add_subtypes("Red Meat")
cleaning.add_subtypes("Windex")

# Create a product with category and subcategory references
cow_meat = Product(name="Cow Meat", weight=5, price=5, types="Food", subtypes="Red Meat")
windex_ype = Product(name = "Windex Ype", weight = 100, price = 10, types = cleaning, subtypes=cleaning.subtypes["Windex"])

# Add the product to the appropriate subcategory
food.add_product("Red Meat", cow_meat)

# Display product details
# cow_meat.display_product_details()
windex_ype.display_product_details()

food.display_types()
