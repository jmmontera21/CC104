available_burger = ["Hamburger", "Cheeseburger", "Ham and Egg", "Overload", "Veggieburger"]
available_topping = ["Cheese", "Lettuce", "Bacon", "Patty", "Egg", "Tomato"]

burger_prices = {"Hamburger" : 30, "Cheeseburger" : 40, "Ham and Egg" : 35, "Overload" : 60, "Veggieburger" : 25}
topping_prices = {"Cheese" : 10, "Lettuce" : 15, "Bacon" : 25, "Patty" : 20, "Egg" : 10, "Tomato" : 5}

subtotal = []
final_order = {}
customer_info = {}

order_burger = True
while order_burger:
    print("-------------- List of Available Burgers ---------------")
    for each_burger in available_burger:
        print(each_burger)
        
    while True:
        burger = input("Which burger would you like to order ? ")
        if burger in available_burger:
            print("You have ordered", burger)
            subtotal.append(burger_prices[burger])
            print(subtotal)
            break
        else:
            print("Invalid Choice")

    order_toppings = True
    print("------------- List of Available Toppings --------------")
    for each_topping in available_topping:
        print(each_topping)
    while order_toppings:
        add_topping = input("Would you like to add toppings on your burger ? (yes/no)")
        if add_topping == "yes":
            topping = input("Which topping would you like to add on your burger ? ")
            if topping in available_topping:
                final_order.setdefault(burger,[])
                final_order[burger].append(topping)
                print("Topping has been added on your burger")
                subtotal.append(topping_prices[topping])
                print(subtotal)
            else:
                print(topping,"is not available at the moment")
        elif add_topping == "no":
            final_order.setdefault(burger,[])
            print(subtotal)
            break
        else:
            print("Invalid Choice")
            continue

    extra_burger = input("Would you like to add another burger ? (yes/no)")
    if extra_burger == "no":
        for key, value in final_order.items():
            print("You have ordered ",key, "with the following toppings",value)

        confirm_order = True
        while confirm_order:
            order_correct = input("Is your order correct ? (yes/no) ")
            if order_correct == "yes":
                print(final_order)
                confirm_order = False
                order_burger = False
            elif order_correct == "no":
                print(final_order)
                add_remove = input("Which burger would you like to add or remove from an order (a/r) ?")
                if add_remove == "r":
                    remove = input("Which burger would you like to remove ? ")
                    del final_order[remove]
                    print(final_order)
                else:
                    confirm_order = False

            else:
                print("Invalid Choice")
    elif extra_burger == "yes":
        continue
    else:
        print("Invalid Choice")

print()
