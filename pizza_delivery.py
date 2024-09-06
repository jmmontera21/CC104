
pizza_type = ["Ham and Cheese", "Pepperoni", "Hawaian", "Overload"]
pizza_topping = ["More Cheese", "Onions", "Bellpepper", "Bacon", "Olives", "Vegetables"]

type_price = {"Ham and Cheese" : 60, "Pepperoni" : 80, "Hawaian" : 100, "Overload" : 140}
topping_price = {"More Cheese" : 10, "Onions" : 30, "Bellpepper" : 15, "Bacon" : 40, "Olives" : 10, "Vegetables" : 25}

subtotal = []
final_order = {}
customer_info = {}

order_pizza = True
while order_pizza == True:
    print("List of Pizza : ")
    for each_pizza in pizza_type:
        print(each_pizza)
    
    while True:
        pizza = input("Which pizza would you like to order ? ")
      #  pizza_size = input("What size of pizza? (Regular, Medium, Large, X-Large, XX-Large): ")
        if pizza in pizza_type:
            print(pizza)
            subtotal.append(type_price[pizza])
            print(subtotal)
            break
            #print("You have ordered ",pizza)
            #subtotal.append(type_price[pizza])
            #break
        else:
            print("Invalid Choice")

    order_toppings = True
    print("LIST OF TOPPINGS")
    for each_topping in pizza_topping:
        print(each_topping)
    while order_toppings == True:
        add_topping = input("Would you like to add toppings in your pizza ? (yes/no) ")
        if add_topping.lower() == "yes":
            topping = input("Which topping would you like to add on your pizza ? ")
            if topping in pizza_topping:
                final_order.setdefault(pizza,[])
                final_order[pizza].append(topping)
                print("Topping added on your order")
                subtotal.append(topping_price[topping])
                print(subtotal)
            else:
                print(topping, "is not available at the moment")
        elif add_topping.lower() == "no":
            final_order.setdefault(pizza,[])
            print(subtotal)
            break
        else:
            print("Invalid Choice")
            continue

    extra_pizza = input("Would you like to add another pizza (yes/no) ? ")
    if extra_pizza.lower() == "no":
        for key, value in final_order.items():
            print("You have ordered the following pizza ",key,"with the following toppings ",value)
        
        check_order = True
        while check_order == True:
            order_correct = input("Is your order correct (yes/no)? ")
            if order_correct.lower() == "yes":
                print("OVERALL ORDER")
                print(final_order)
                check_order = False #current loop off
                order_pizza = False #big while loop off
            elif order_correct.lower == "no":
                print(final_order)
                add_remove = input("Which pizza would you like to add or remove from an order (a/r) ?")
                if add_remove == "r":
                    to_remove = input("Which pizza would you like to remove from your order ? ")
                    del final_order[to_remove]
                    print(final_order)
                else:
                    check_order = False
            else:
                print("Invalid Choice")
    elif extra_pizza.lower() == "yes":
        continue
    else:
        print("Invalid choice of option, please type y / n") 

print("------------------------ DELIVERY INFORMATION --------------------------")
customer_info["name"] = input("Enter your name : ")
customer_info["addr"] = input("Enter your address : ")
customer_info["cp"] = input("Enter your contact number : ")
customer_info["landmark"] = input("Any specific landmark near at your place ? ")
customer_info["dist"] = input("How far are you located ? ")

print("------------------------ CUSTOMER INFORMATION FINISH --------------------------")
print("Thank you, Sir/Ma'am ",customer_info["name"], "contact number", customer_info["cp"], "located at", customer_info["addr"])
print("Nearest landmark is at", customer_info["landmark"])
print("Please wait for ", int(customer_info["dist"]) * 5, "minutes to deliver your order. We'll process your order ASAP. ")




  #if pizza_size == "Regular":
            #    print(f"You have ordered a {pizza} (Regular).")
             #   subtotal.append(type_price[pizza])
            #elif pizza_size == "Medium":
             #   print(f"You have ordered a {pizza} (Medium).")
             #   subtotal.append(type_price[pizza] * 1.5)
            #elif pizza_size == "Large":
            #    print(f"You have ordered a {pizza} (Large).")
            #    subtotal.append(type_price[pizza] * 1.75)
            #elif pizza_size == "X-Large":
            #    print(f"You have ordered a {pizza} (X-Large).")
            #    subtotal.append(type_price[pizza] * 2) 
            #elif pizza_size == "XX-Large":
            #    print(f"You have ordered a {pizza} (XX-Large).")
            #   subtotal.append(type_price[pizza] * 2.5)
            #break

