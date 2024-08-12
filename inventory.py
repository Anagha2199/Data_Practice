inventory = [
    {"item_id":1,"item_name":"apple","item_price":50},
    {"item_id":2,"item_name":"orange","item_price":45},
    {"item_id":3,"item_name":"grape","item_price":35},
    {"item_id":4,"item_name":"watermelon","item_price":40},
    {"item_id":5,"item_name":"avocado","item_price":75},
    {"item_id":6,"item_name":"pappaya","item_price":35}
]
shopping_cart = []
def display_menu():
    print("\n\t**********Menu************\n")
    print("1. View the store")
    print("2. Purchase the item")
    print("3. Update the purchase item")
    print("4. Remove the item")
    print("5. View the purchased item list")
    print("6. Exit and generate invoice")
def print_inventory():
    for item in inventory:
        print(item)
def add_to_cart():
    purchase_item = input("please enter the item you wish to purchase: ")
    item_quantity = int(input(f"Please enter the quantity of {purchase_item} you wish to purchase: "))
    for item in inventory:
        if purchase_item.lower() == item["item_name"]:
            shopping_cart.append({"item_name":purchase_item,"item_price":item["item_price"],"quantity":item_quantity})
    #c=input("Do you want to continue? Y/N\t")
    #if c == 'N' or c == 'n':
    #    return
    print("\n**Below items successfully added to the cart**")
    for item in shopping_cart:
        print(item)

def cart_update():
    name_upd = input("Please enter the product to be updated in the cart")
    quantity_upd = int(input("Please enter the quantity to be updated in the cart"))
    for item in shopping_cart:
        if name_upd.lower() == item["item_name"]:
            item["quantity"] = quantity_upd
    print("\n**Cart updated successfully**")
    for item in shopping_cart:
        print(item)

def item_rem():
    name_rem = input("Please enter the product to be updated in the cart")
    for item in shopping_cart:
        if name_rem.lower() == item["item_name"]:
            shopping_cart.remove(item)
    print("\n**Oops! Few items removed!**")
    for item in shopping_cart:
        print(item)

while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print_inventory()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        cart_update()
    elif choice == 4:
        item_rem()
    elif choice == 5:
        for item in shopping_cart:
            print(item)
    elif choice == 6:



