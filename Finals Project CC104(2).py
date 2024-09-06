import getpass
admin_acc = {"ornamental": "plant1234"} 

Ornamental_plants = ["Cactus","Sampaguita","Roses","Sunflower"]
Price_plants = {"Cactus" : 120,"Sampaguita" : 100,"Roses" : 150,"Sunflower" : 130}

Special_offer = ["Fertilizer", "Quality Pot", "Pebbles", "Seeds"]
Price_offer = {"Fertilizer" : 30, "Quality Pot" : 50, "Pebbles" : 20, "Seeds" : 40}

subtotal = []
total_order = {}
customer_info = {}
 
def displayplants():
    for each_plant in Ornamental_plants:
        print(each_plant)
def inclusionoffer():
    for each_offer in Special_offer:
        print(each_offer)
def plantinfo():
    info = True
    while info:
        description = input("Would you like to know more information about the ornamental plant you want to order ? (yes/no)")
        if description == "yes":
            plant = input("Choose an ornamental plant you want to know about : ")
            if plant == "Cactus":
                print("This is an ornamental plant")
            elif plant == "Sunflower":
                print("This is an ornamental plant")
            elif plant == "Roses":
                print("This is an ornamental plant")
            elif plant == "Sampaguita":
                print("This is an ornamental plant")
            else:
                print("Plant is not included in the list")
        elif description == "no":
            info = False
            break
        else:
            print("Invalid Choice")
def buyplant():
    buying = True
    while buying:
        displayplants()
        plant = input("Please select an ornamental plant : ")
        if plant in Ornamental_plants:
            print("You have ordered",plant)
            subtotal.append(Price_plants[plant])
            print("Your total order is worth",subtotal,"pesos.")
            Ornamental_plants.remove(plant)
            displayplants()
        else:
            print(plant,"is not included in the list")
        break
    buying = False

    inclusion = True
    while inclusion:
        additional_thing = input("Would you like to add inclusion and improve your ornamental plant ? (yes/no)")
        if additional_thing == "yes":
            inclusionoffer()
            inmaterial = input("Please select an inclusion for your ornamental plant : ")
            if inmaterial in Special_offer:
                total_order.setdefault(plant,[])
                total_order[plant].append(inmaterial)
                print("You have added",inmaterial)
                subtotal.append(Price_offer[inmaterial])
                print("Your total order is worth",subtotal,"pesos.")
            else:
                total_order.setdefault(plant,[])
                print(inmaterial,"is not included in the list")
                break
        elif additional_thing == "no":
            print("Thank for your interest in inclusion offer.")
            break
        else:
            print("Invalid choice, please type yes/no")
            continue
def buyplant2():
    newOrder = True
    #subtotal = []
    while newOrder:
    #addplant = order()
    #subtotal.append(addplant)
        newplant = input("Would you like to order another plant ? (yes/no)")
        if newplant == "yes":
            displayplants()
            add_plant = input("Which plant would you like to add on your order ? ")
            if add_plant in Ornamental_plants:
                print("You have ordered",add_plant)
                subtotal.append(Price_plants[add_plant])
                print("Your total order is worth",subtotal,"pesos.")
                Ornamental_plants.remove(add_plant)
                displayplants()
            else:
                print(add_plant,"is not included in the list")
                break
        elif newplant == "no":
            print("Thank you for ordering.")
            break
        else:
            print("Invalid choice, please type yes/no")
            continue 
#def specialoffer():
    
def postplant():
    selling = True
    while selling:
        displayplants()
        new_plant = input("What plant do you want to sell/upload in our online store ? ")
        if new_plant:
            print("You have added", new_plant, "in our online store.")
            Ornamental_plants.append(new_plant)
            displayplants()
        else:
            print("Okay, thank you for your interest in selling your ornamental plant.")
        break
    selling = False
def postplant2():
    uploadplant = True
    #subtotal = []
    while uploadplant:
        #addplant = order()
        #subtotal.append(addplant)
        addplant = input("Would you like to sell/upload another plant ? (yes/no)")
        if addplant == "yes":
            upload_plant = input("What plant would you like to sell/upload in our store ? ")
            if upload_plant:
                print("You have uploaded",upload_plant)
                Ornamental_plants.append(upload_plant)
                displayplants()
            else:
                print(upload_plant,"is not included in the list")
                break
        elif addplant == "no":
            print("Thank you for ordering.")
            break
        else:
            print("Invalid choice, please type yes/no")
            continue 
class order:
    def __init__(self):
        plant_a = buyplant()
        self.type = plant_a
        self.plant_price = Price_plants[plant_a]
        
class customer:
    def __init__(self,name,age,contact_number,address):
        self.name = name
        self.age = age
        self.contact_number = contact_number
        self.address = address
        

if __name__ == "__main__":
    print("  ****                                        ****  ")
    print(" ******                                      ****** ")
    print(" ******                                      ****** ")
    print("  ****                                        ****  ")
    print("   || >> JMM ORNAMENTAL PLANTS ONLINE STORE << ||   ")
    print("   ||                                          ||   ")
    print("   ||                                          ||   ")
    print("   ||                                          ||   ")
    print("  |==|                                        |==|  ")
    print("  |==|                                        |==|  ")

    orn_plants = True
    while orn_plants:
        option = eval(input("Choose an option :\n[1] - Show Available Ornamental Plants \n[2] - Order Ornamental Plants \n[3] - Sell Your Ornamental Plants \n[4] - Exit \n[5] - Checkout"))
        if option == 1:
            displayplants()
            plantinfo()
        elif option == 2:
            buyplant()
            #specialoffer()
            buyplant2()
        elif option == 3:
            postplant()
            postplant2()
        elif option == 4:
            print("The ornamental plants panel has stopped")
            orn_plants = False
        elif option == 5:
            customer_info["name"] = input("Enter your name : ")
            customer_info["age"] = input("Enter your age : ")
            customer_info["contact_number"] = input("Contact Number : ")
            customer_info["address"] = input("Enter your exact address : ")

            print(customer_info["name"])
            print(customer_info["age"])
            print(customer_info["contact_number"])
            print(customer_info["address"])
        #elif option == 6:
        #check order, add/remove function
        else:
            print("Invalid Choice")
            continue
    
    choice = True
    subtotal = []

Maintotal = 0 
for each_order in subtotal:
    Maintotal = Maintotal + each_order.total

print(f"Total Order Price is {Maintotal}")

