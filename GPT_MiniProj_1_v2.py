# from keyboard import read_key
import os

class Product:
    num_prods = 0
    def __init__(self, name = None, quantity=0, price=0):
        self.inventory = {
            "name": name,
            "quantity": quantity,
            "price": price
            }
    
    def __repr__(self):
        return f"\n{self.inventory['name']}, {self.inventory['quantity']}, {self.inventory['price']}"
    1
    def update_quantity(self, quantity):
        self.inventory["quantity"] = quantity
    
    def update_price(self, price):
        self.inventory["price"] = price

def find_products(prod_name, all_prods):
    for prod in all_prods:
        if prod.inventory['name'].lower() == prod_name.lower():
            return prod
    return None

#How to add product to our inventory
def menu_1():
    new_prod = input('Please type the name of the new item that will be added to the inventory: ')
    while not new_prod.isalpha():
        new_prod = input(
            "I'm sorry, it seems that you typed something that our system doesn't allow for names.\nOur system only allows name that include letters and numbers as name.\nPlease Try again: "
            )
        
    #check if product is already on the system
    
    new_prod = Product(name = new_prod[0].upper()+new_prod[1:])
    all_products.append(new_prod)    
    #reminder to add quantity and price
    print(f"Product: {new_prod.inventory['name']} added.")    
    print(f"Dont forget to add a quantity and price for {new_prod.inventory['name']}.")

#Changing quantity to our product
def menu_2():   
    product1 = input('Whats the product that you want to change the quantity: ')
    prod_update = find_products(product1, all_products)
    if prod_update:
        print(f"{prod_update.inventory['name']} found")
        while True:
            prod_quant = input('Now, go ahead and type the new quantity for it: ')
            if prod_quant.isnumeric() and int(prod_quant) > 0:
                prod_update.inventory['quantity'] = int(prod_quant)
                print(f"Updated quantity of {product1} to {prod_update.inventory['quantity']}")
                break
            print("You didn’t type a valid positive number, try again.")
    else:        
        print("Sorry, product isn't on stock, you either typed it incorrectly or you have to go back to the main menu and add it")      

#Changing price of a product  
def menu_3():
    product1 = input('Whats the product that you want to change the price: ')
    prod_update = find_products(product1, all_products)
    if prod_update:
        print(f"{prod_update.inventory['name']} found")
        while True:
            prod_price = input('Now, go ahead and type the new price for it: ')
            if prod_price.isnumeric() and int(prod_price) > 0:
                prod_update.inventory['price'] = int(prod_price)
                print(f"Updated quantity of {product1} to {prod_update.inventory['price']:.2f}")
                break
            print("You didn’t type a valid positive number, try again.")
    else:        
        print("Sorry, product isn't on stock, you either typed it incorrectly or you have to go back to the main menu and add it")  
    
#Show all items that are inventory with their respective prices and quantities
def menu_4():
    print("Here is a list of all products that we have: ")
    num_prod = 1
    for prod in all_products:
        print(f"{num_prod}. {prod.inventory['name']} | Quantity: {prod.inventory['quantity']} | Price: ${prod.inventory['price']}\n")
        num_prod += 1

#Main menu    
def menu():
    while True:        
        answer = input(
            "What do you want to do?\n1. Add a new Item.\n2. Update the quantity of an item.\n3. Update price of an item.\n4. View all items in the inventory.\n5. Exit program.\n"
            )
        #Waiting user to type a key, only 1 key is valid
        # answer = read_key()
        if answer == '1':
            os.system('cls')
            menu_1()
                            
        elif answer == '2':
            os.system('cls')
            menu_2()
           
        elif answer =='3':
            os.system('cls')
            menu_3()

        elif answer == '4':
            os.system('cls')
            menu_4()

        elif answer == '5':
            os.system('cls')
            print('Exiting program. See you next time.')
            break
        else:
            print('Invaled option, please try again.')
            os.system('cls')

if __name__ == "__main__":
    all_products = []
    menu()
    





            
