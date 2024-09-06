subtotal = []
total_order = {}

import getpass
admin_acc = {"ornamental": "plant1234"} 

class Ornamental_plants:
    def __init__(self,list_of_ornplants,list_of_inclusion_offer):
        self.list_of_ornplants = list_of_ornplants
        self.list_of_inclusion_offer = list_of_inclusion_offer


    def displayplants(self):
        for each_plant in self.list_of_ornplants:
            print("               ",each_plant,"                   ")

    def inclusionoffer(self):
        for each_inclusion in self.list_of_inclusion_offer:
            print("               ",each_inclusion,"                   ")

    def addplant(self):
        name_plant = input("Which plant would you like to add ? ")
        self.list_of_ornplants.append(name_plant)
        print(name_plant,"has been added from the list")

    def addplant1(self):
        addition = True
        while addition:
            add2_order = input("Would you like to add another ornamental plant ? (yes/no)")
            if add2_order.lower() == "yes":
                myOrnPlants.addplant()
                myOrnPlants.displayplants()
                continue
            elif add2_order.lower() == "no":
                print("Thank you")
                addition = False
                break
            else:
                print("Not an option.")   

    def removeplant(self):    
        myOrnPlants.displayplants()
        name_plant = input("Which plant would you like to delete ? ")
        self.list_of_ornplants.remove(name_plant)
        print("The ornamental plant has been deleted from the list")

    def plantinfo(self):
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
    
    def buyplant(self,plant):
        buying = True
        while buying:
            myOrnPlants.displayplants()
            plant = input("Please select an ornamental plant you want to order : ")
            if plant in self.list_of_ornplants:
                print("You have ordered",plant)
                subtotal.append(Price_plants[plant])
                print("Your total order is worth",subtotal,"pesos.")
                break
            else:
                print(plant,"is not included in the list")
                continue
        buying = False

        inclusion = True
        while inclusion:
            additional_thing = input("Would you like to add inclusion and improve your ornamental plant ? (yes/no)")
            if additional_thing == "yes":
                myOrnPlants.inclusionoffer()
                inmaterial = input("Please select an inclusion for your ornamental plant : ")
                if inmaterial in self.list_of_inclusion_offer:
                    total_order.setdefault(plant,[])
                    total_order[plant].append(inmaterial)
                    print("You have added",inmaterial)
                    subtotal.append(Price_offer[inmaterial])
                    print("Your total order is worth",subtotal,"pesos.")
                    break
                else:
                    total_order.setdefault(plant,[])
                    print(inmaterial,"is not included in the list")
                    continue
            elif additional_thing == "no":
                print("Thank for your interest in inclusion offer.")
                break
            else:
                print("Invalid choice, please type yes/no")
                continue
    
    def postplant(self):
        selling = True
        while selling:
            myOrnPlants.displayplants()
            new_plant = input("What plant do you want to sell/upload in our online store ? ")
            if new_plant:
                print("You have added", new_plant, "in our online store.")
                myOrnPlants.list_of_ornplants.append(new_plant)
                myOrnPlants.displayplants()
                new_price = eval(input("Input the selling price of your ornamental plant : "))
                if new_price:
                    print("The price has been added beside your posted ornamental plant")
            else:
                print("Okay, thank you for your interest in selling your ornamental plant.")
            break
        selling = False

    def checkout(self):
        print("===================== OFFICIAL (RECEIPT ===========================")
        print("Your total order is worth", sum(subtotal), "pesos")
        print("Thank you for ordering, Ma'am/Sir", name, age, "years old. ""Contact number is", contact_number, " and located at", address)
        print("Please wait patiently for your order. We'll deliver it as soon as possible.")
        print("--------- THANK YOU FOR ORDERING AT JMM ORNAMENTAL PLANTS STORE, VISIT AGAIN -----------")

class Customer:
    def __init__(self, name, age, address, contact_number):
        self.name = name
        self.age = age
        self.address = address
        self.contact_number = contact_number


if __name__ == ("__main__"):
    print("  ****                                                   ****  ")
    print(" ******                                                 ****** ")
    print(" ******                                                 ****** ")
    print("  ****                                                   ****  ")
    print("   ||     >> WELCOME TO JMM ORNAMENTAL PLANTS STORE <<    ||   ")
    print("   ||                                                     ||   ")
    print("   ||                                                     ||   ")
    print("   ||                                                     ||   ")
    print("  |==|                                                   |==|  ")
    print("  |==|                                                   |==|  ")
    myOrnPlants = Ornamental_plants(["Cactus", "Sunflower", "Sampaguita", "Roses"], ["Fertilizer", "Quality Pot", "Pebbles", "Seeds"])
    Price_plants = {"Cactus" : 120,"Sampaguita" : 100,"Roses" : 150,"Sunflower" : 130}
    Price_offer = {"Fertilizer" : 30, "Quality Pot" : 50, "Pebbles" : 20, "Seeds" : 40}
    Loop = True
    while Loop:
        print("Choose an option : \n[1] - Owner Account \n[2] - Customer Account")
        account = eval(input())
        if account == 1:  
                print("Welcome to the Owner Account")
                print("Enter your LOGIN CREDENTIALS : ")
                usn = input("Enter your username : ")
                pwd = getpass.getpass("Enter your password : ")
                for key, value in admin_acc.items():
                    if usn == key and pwd == value:
                        print("LOGIN SUCCESSFUL")
                        while True:
                            print("Choose an option : \n[1] - Show List of Ornamental Plants \n[2] - Add Ornamental Plant \n[3] - Delete Ornamental Plant \n[4] - Exit")
                            choice = eval(input())
                            if choice == 1:
                                print("      LIST OF AVAILABLE ORNAMENTAL PLANTS      ")
                                myOrnPlants.displayplants()
                            elif choice == 2:
                                myOrnPlants.addplant()
                                myOrnPlants.displayplants()
                                myOrnPlants.addplant1()
                            elif choice == 3:
                                myOrnPlants.removeplant()
                                myOrnPlants.displayplants()
                            elif choice == 4:
                                print("Thank you for using the admin account of the ornamental online store")
                                break
                                
                    else:
                        print ("Incorrect username or password")
                        break
        
        elif account == 2:
            print("Welcome to the Customer Account")
            name = input("Please enter your name : ")
            age = eval(input("Please enter your age : "))
            address = input("Please enter your full address : ")
            contact_number = input("Please enter your contact_number : ")
            print("Hi there,",name,".I hope you enjoy our ornamental plants online store.")
            orn_plants2 = True
            while orn_plants2:
                option = eval(input("\n[1] - Show Available Ornamental Plants \n[2] - Order Ornamental Plants \n[3] - Sell Your Ornamental Plants \n[4] - Receipt \n[5] - Exit \nChoose an option : "))
                if option == 1:
                    myOrnPlants.displayplants()
                    myOrnPlants.plantinfo()
                elif option == 2:
                    myOrnPlants.buyplant(Ornamental_plants)
                    Additional = True
                    while Additional:
                        add_order = input("Would you like to add another ornamental plants in your order ? (yes/no)")
                        if add_order.lower() == "yes":
                            myOrnPlants.buyplant(Ornamental_plants)
                            myOrnPlants.displayplants()
                            continue
                        elif add_order.lower() == "no":
                            check_order = True
                            for key, value in total_order.items():
                                print("You have ordered the following ornamental plant ",key,"with the following inclusion ",value)
                            while check_order == True:
                                order_correct = input("Is your order correct (yes/no)? ")
                                if order_correct.lower() == "yes":
                                    print("OVERALL ORDER")
                                    print(total_order)
                                    check_order = False 
                                    Additional = False
                                elif order_correct.lower() == "no":
                                    print(total_order)
                                    add_remove = input("What would you like to add or remove from your order (a/r) ?")
                                    if add_remove == "r":
                                        to_remove = input("Which ornamental plant would you like to remove from your order ? ")
                                        del total_order[to_remove]
                                        print(total_order)
                                    elif add_remove == "a":
                                        buying = True
                                        while buying:
                                            myOrnPlants.displayplants()
                                            to_add = input("Which ornamental plant would you like to add to your order ? ")
                                            if to_add in self.list_of_ornplants:
                                                print("You have ordered",to_add)
                                                subtotal.append(Price_plants[to_add])
                                                print("Your total order is worth",subtotal,"pesos.")
                                                break
                                            else:
                                                print(to_add,"is not included in the list")
                                                continue
                                        buying = False

                                        inclusion = True
                                        while inclusion:
                                            additional_thing = input("Would you like to add inclusion and improve your ornamental plant ? (yes/no)")
                                            if additional_thing == "yes":
                                                myOrnPlants.inclusionoffer()
                                                inmaterial = input("Please select an inclusion for your ornamental plant : ")
                                                if inmaterial in self.list_of_inclusion_offer:
                                                    total_order.setdefault(to_add,[])
                                                    total_order[to_add].append(inmaterial)
                                                    print("You have added",inmaterial)
                                                    subtotal.append(Price_offer[inmaterial])
                                                    print("Your total order is worth",subtotal,"pesos.")
                                                    break
                                                else:
                                                    total_order.setdefault(to_add,[])
                                                    print(inmaterial,"is not included in the list")
                                                    continue
                                            elif additional_thing == "no":
                                                print("Thank for your interest in inclusion offer.")
                                                break
                                            else:
                                                print("Invalid choice, please type yes/no")
                                                continue
                                                                    else:
                                                                        check_order = False
                                                                else:
                                                                    print("Invalid Choice")
                                                        else:
                                                            print("Not an option") 
                                                            continue
                elif option == 3:
                    myOrnPlants.postplant()
                    Additional2 = True
                    while Additional2:
                        add1_order = input("Would you like to sell/upload another ornamental plant in our online store ? (yes/no)")
                        if add1_order.lower() == "yes":
                            myOrnPlants.postplant()
                            continue
                        elif add1_order.lower() == "no":
                            print("Next")
                            Additional2 = False
                            break
                        else:
                            print("Not an option.")
                elif option == 4:
                    myOrnPlants.checkout()
                    ornplants2 = False
                    Loop = False
                    break
                elif option == 5:
                    Loop = False
                    break
        else:
            print("Invalid Option. Please choose between 1 and 2.")
            continue

