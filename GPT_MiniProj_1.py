class product:
    def __init__(self, name = None, quantity=0, price=0):
        self.inventory = {
            "name": name,
            "quantity": quantity,
            "price": price
            }
    
    def update_quantity(self, quantity):
        self.inventory["quantity"] = quantity
    
    def update_price(self, price):
        self.inventory["price"] = price
    
def menu():
    while True:
        answer = None
        answer1 = input(
            "What do you want to do?\n1. Add a new Item.\n2. Update the quantity of an item.\n3. Update price of an item.\n4. View all items in the inventory.\n5. Exit program.\n"
            )
        answer = answer1
        # print (answer)
        if answer == 1:
            new_item = product()
            new_item.inventory["name"] = input('Please type the name of the new item that will be added to the inventory: ')
            while not isinstance(new_item.inventory["name"], str):
                new_item.inventory["name"] = input(
                    "I'm sorry, it seems that you typed something that our system doesn't allow for names.\nOur system only allows name that include letters and numbers as name.\nPlease Try again: "
                    )
                
            print(f"Dont forget to add a quantity and price for {new_item.inventory['name']}.")
        # elif answer == 2:
        #     new
        elif answer == 5:
            print('Exiting program. See you next time.')
            break
        else:
            print('Invaled option, please try again.')

if __name__ == "__main__":
    menu()





            
