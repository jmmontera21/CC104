#myOrnPlants = (["Silver Nerve Plant", "Fibre Optic Grass Plant", "Snake Plant", "String Of Pearls", "Peace Lily", "Chinese Money Plant", "Air Plant", "Water Bamboo", "Bonsai", "Bunny Ear Cactus"], ["Fertilizer", "Quality Pot", "Pebbles", "Seeds"])
Price_plants = {"Silver Nerve Plant" : 120,"Fibre Optic Grass Plant" : 100,"Snake Plant" : 150,"String Of Pearls" : 130,"Peace Lily" : 20,"Chinese Money Plant" : 40, "Air Plant" : 90,"Water Bamboo" : 100,"Bonsai" : 80,"Bunny Ear Cactus" : 120}
Price_offer = {"Fertilizer" : 30, "Quality Pot" : 50, "Pebbles" : 20, "Seeds" : 40}

subtotal = []
total_order = {}

import getpass
admin_acc = {"ornamental": "plant1234"} 

class Ornamental_plants:
    def __init__(self):
        self.Price_plants = Price_plants
        self.Price_offer = Price_offer


    def displayplants(self):
        for key,value in Price_plants.items():
            print(key, " - ", value)

    def inclusionoffer(self):
        for key,value in Price_offer.items():
            print(key, " - ", value)
    
    def addplant(self,add_plant,add_price):
        self.add_plant = add_plant
        self.add_price = add_price

        Price_plants.update({self.add_plant : self.add_price})

    def addplant1(self):
        addition = True
        while addition:
            add2_order = input("Would you like to add another ornamental plant ? (yes/no)")
            if add2_order.lower() == "yes":
                plant = input("\nEnter the name of ornamental plant: ")
                price = float(input("Enter the price of ornamental plant: "))
                orn.addplant(plant,price)
                orn.displayplants()
                continue
            elif add2_order.lower() == "no":
                print("Thank you")
                addition = False
                break
            else:
                print("Not an option.")   

    def removeplant(self,rem_plant):    
        self.rem_plant = rem_plant
        if self.rem_plant in Price_plants:
            del Price_plants[self.rem_plant]
        else:
            pass
        print("The ornamental plant has been deleted from the list")

    def remove(self):
        removal = True
        while removal:
            remove_order = input("Would you like to remove another ornamental plant ? (yes/no)")
            if remove_order.lower() == "yes":
                rem = input("\nEnter the name of ornamental plant: ")
                orn.removeplant(rem)
                orn.displayplants()
                continue
            elif remove_order.lower() == "no":
                print("Thank you")
                removal = False
                break
            else:
                print("Not an option.") 
            
    def updateplant(self, upd_name, upd_price):
        self.upd_name = upd_name
        self.upd_price = upd_price
        Price_plants.update(self.upd_price)
    
    def postplant(self):
        selling = True
        while selling:
            cs.displayplants()
            new_plant = input("What plant do you want to sell/upload in our online store ? ")
            if new_plant:
                print("You have added", new_plant, "in our online store.")
                cs.list_of_ornplants.append(new_plant)
                cs.displayplants()
                new_price = eval(input("Input the selling price of your ornamental plant : "))
                if new_price:
                    print("The price has been added beside your posted ornamental plant")
            else:
                print("Okay, thank you for your interest in selling your ornamental plant.")
            break
        selling = False

class Customer:
    #def __init__(self, name, age, address, contact_number):
    #    self.name = name
    #    self.age = age
    #    self.address = address
    #    self.contact_number = contact_number
    
    def displayplants(self):
        for key,value in Price_plants.items():
            print(key, " - ", value)

    def inclusionoffer(self):
        for key,value in Price_offer.items():
            print(key, " - ", value)

    def plantinfo(self):
        info = True
        while info:
            description = input("Would you like to know more information about the ornamental plant you want to order ? (yes/no)")
            if description == "yes":
                plant = input("Choose an ornamental plant you want to know about : ")
                if plant == "Silver Nerve Plant":
                    print("Silver nerve plant is one of the best evergreen ornamental garden plants with deep green leaves that have delicately veined leaves running throughout. That being the focal point, these vein tints can vary from white, silver to green, pink etc. The leaves are large and majestic that will drag attention, no matter their placement of display.")
                elif plant == "Fiber Optic Grass Plant":
                    print("Although, it looks like a grass, fibre optic grass plant is an ornamental plant that basically belongs to the sedge family and blooms year round in warm climates or a sunny window. The tip of the long slender blades of the plant is decked with small terminal flower heads giving a resemblance to fiber-optic novelty lamps.")
                elif plant == "Snake Plant":
                    print("Snake Plant or Mother in Law’s Tongue is one of the best ornamental plants to refresh your shady porch. The plant has robust, textured leaves in a sword like shape spiralling slightly through the length. The plant can grow upto 1 metre long and therefore, it is suggested to place it in a strong pot.")
                elif plant == "String Of Pearls":
                    print("String of pearls is a trailing succulent with delicate tendrils of round beads. If you are seeking best ornamental garden plants, this should definitely be on your list as they make a wonderful display in hanging baskets. They are drought resistant and grow several feet spilling over the edge of the plant.")
                elif plant == "Peace Lily":
                    print("Peace lily is a large flowering plant that also makes for a perfect gift for loved ones. One of the most common houseplants, it has sturdy, glossy leaves with arum shaped flamboyant white blooms. The gorgeous ornamental plant is also favoured for its air purifying traits.")
                elif plant == "Chinese Money Plant":
                    print("Chinese money plant has round coin shaped leaves and upright stems. It is a bold, decorative plant that looks stunning in short pots and grows well in bright indirect light. It is also known as the Friendship Plant.")
                elif plant == "Air Plant":
                    print("There are many varieties of air plants. They usually have grey or green blades and grow only a few inches. As the name suggests, these ornamental garden plants do not anchor themselves to the soil, you can suspend them in glass globes, bed of dry pebbles, shells, barks etc.")
                elif plant == "Water Bamboo":
                    print("Water bamboo are one of the most affordable online plants that are widely exchanged as gifts because they are believed to bring good luck, health, wealth, prosperity and positivity. Also known as lucky bamboo, they range from 2 layer to 7 layer bamboo plants.")
                elif plant == "Bonsai":
                    print("Bonsai, coming in various types, are dwarfed potted trees and growing them is considered as an art form in Chinese horticulture practice. They are a miniaturized but realistic representation of nature with textured barks, thick trunks and attractively intertwined live woods.")
                elif plant == "Bunny Ear Cactus":
                    print("Bunny ear cactus, also known as Polka Dot cactus or Angel’s Wings is a Mexican cactus with clump shaped circular pads. These ornamental garden plants are 2 to 3 feet tall succulents with short whitish brown prickles known as glochids. During summers, they are likely to produce creamy yellow flowers and globular purple fruits.")
                else:
                    print(plant," is not included in the list.")
                    continue
            elif description == "no":
                info = False
                break
            else:
                print("Invalid Choice")

    def order(self,orn_name,perpiece_price,pieces):
        self.orn_name = orn_name
        self.pieces = pieces
        self.perpiece_price = perpiece_price

        self.total = self.perpiece_price * self.pieces
        subtotal.append(self.total)

        total_order.setdefault(orn_name, [])
        total_order[self.orn_name].append(self.total)

    def buyplant3(self):
        cs_order = True
        while cs_order:
            print ("\n\t\t ------ Customer Order ------\n")
            order = input("Enter the ornamental plant you want to order: ")
            for key, value in Price_plants.items():
                if order == key in Price_plants:
                    pcs = eval(input("How many pieces ? "))
                    cs.order(key, value, pcs)
                    for key, value in Price_plants.items():
                        print ("Order Receipt: [", key, "] ", pcs, "=", value, "pesos")

                    another_order = input("Would you like to order another ornamental plant? (yes or no)")
                    if another_order == "yes":
                        continue
                    elif another_order == "no":
                        print ("Your Order Total is [", sum(subtotal), "] pesos")
                        cs_order = False
                        continue
                    else:
                        print("Invalid choice")
                        break
                                
                elif order == key not in Price_plants:
                    print ("Ornamental Plant Unavailable")
                    break

    def buyplant(self,plant):
        buying = True
        while buying:
            cs.displayplants()
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
                cs.inclusionoffer()
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
    
    def check_order(self):
        Additional = True
        while Additional:
            add_order = input("Would you like to add another ornamental plants in your order ? (yes/no)")
            if add_order.lower() == "yes":
                    cs.buyplant(Ornamental_plants)
                    cs.displayplants()
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
                            print("Proceed to option 4 to see your receipt, thank you.")
                            check_order = False 
                            Additional = False
                        elif order_correct.lower() == "no":
                            print(total_order)
                            add_remove = input("would you like to add or remove from your order (a/r) ?")
                            if add_remove == "r":
                                to_remove = input("Which ornamental plant would you like to remove from your order ? ")
                                del total_order[to_remove]
                                del total_order[subtotal]
                                print(total_order)
                            elif add_remove == "a":
                                buying = True
                                while buying:
                                    cs.displayplants()
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
                                        cs.inclusionoffer()
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
                            print("Invalid Choice")
            else:
                print("Not an option") 
                continue

    def checkout(self):
        print("===================== OFFICIAL (RECEIPT ===========================")
        print("Your total order is worth", sum(subtotal), "pesos")
        print("Thank you for ordering, Ma'am/Sir", name, age, "years old. ""Contact number is", contact_number, " and located at", address)
        print("Please wait patiently for your order. We'll deliver it as soon as possible.")
        print("--------- THANK YOU FOR ORDERING AT JMM ORNAMENTAL PLANTS STORE, VISIT AGAIN -----------")

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
                            orn = Ornamental_plants()
                            print("Choose an option : \n[1] - Show List of Ornamental Plants \n[2] - Add Ornamental Plant \n[3] - Delete Ornamental Plant \n[4] - Update List of Ornamental Plants \n[5] - Exit")
                            choice = eval(input())
                            if choice == 1:
                                print("      LIST OF AVAILABLE ORNAMENTAL PLANTS      ")
                                orn.displayplants()
                            elif choice == 2:
                                plant = input("\nEnter the name of ornamental plant: ")
                                price = float(input("Enter the price of ornamental plant: "))
                                orn.addplant(plant, price)
                                print("\n\t\tADDED to STOCKS!\n")
                                orn.displayplants()
                                orn.addplant1()
                            elif choice == 3:
                                orn.displayplants()
                                remplant = input("\nEnter the name of ornamental plant you wish to remove: ")
                                orn.removeplant(remplant)
                                orn.displayplants()
                                orn.remove()
                            elif choice == 4:
                                orn.displayplants()
                                name_upd = input("\nEnter name of ornamental plant to update: ")
                                for key, value in Price_plants.items():
                                    if name_upd == key in Price_plants:
                                        price_upd = float(input("Enter updated price: "))
                                        orn.updateplant(name_upd, {key:price_upd})
                                        print("\n\t\tPRICE UPDATED!\n")
                                        orn.displayplants()
                                        break
                                    elif name_upd == key not in Price_plants:
                                        print ("\n\t\tNo Stocks!\n")
                            elif choice == 5:
                                print("Thank you for using the admin account of the ornamental online store")
                                break
                            else:
                                print("Invalid option")
                                
                    else:
                        print ("Incorrect username or password")
                        break
        
        elif account == 2:
            print("Welcome to the Customer Account")
            #name = input("Please enter your name : ")
            #age = eval(input("Please enter your age : "))
            #address = input("Please enter your full address : ")
            #contact_number = input("Please enter your contact_number : ")
            #print("Hi there,",name,".I hope you enjoy our ornamental plants online store.")
            orn_plants2 = True
            while orn_plants2:
                cs = Customer()
                option = eval(input("\n[1] - Show Available Ornamental Plants \n[2] - Order Ornamental Plants \n[3] - Sell Your Ornamental Plants \n[4] - Receipt \n[5] - Exit \nChoose an option : "))
                if option == 1:
                    cs.displayplants()
                    cs.plantinfo()
                elif option == 2:
                    cs_order = True
                    while cs_order:
                        print ("\n\t\t ------ Customer Order ------\n")
                        order = input("Enter the ornamental plant you want to order: ")
                        for key, value in Price_plants.items():
                            if order == key in Price_plants:
                                pcs = eval(input("How many pieces ? "))
                                cs.order(key, value, pcs)
                                for key, value in Price_plants.items():
                                    print ("Order Receipt: [", key, "] ", pcs, "=", value, "pesos")

                                another_order = input("Would you like to order another ornamental plant? (yes or no)")
                                if another_order == "yes":
                                    continue
                                elif another_order == "no":
                                    print ("Your Order Total is [", sum(subtotal), "] pesos")
                                    cs_order = False
                                    orn_plants2 = False
                                    continue
                                else:
                                    print("Invalid choice")
                                    break
                                            
                            elif order == key not in Price_plants:
                                print ("Ornamental Plant Unavailable")
                                break
                    #cs.check_order()
                elif option == 3:
                    cs.postplant()
                    Additional2 = True
                    while Additional2:
                        add1_order = input("Would you like to sell/upload another ornamental plant in our online store ? (yes/no)")
                        if add1_order.lower() == "yes":
                            cs.postplant()
                            continue
                        elif add1_order.lower() == "no":
                            print("Next")
                            Additional2 = False
                            break
                        else:
                            print("Not an option.")
                elif option == 4:
                    cs.checkout()
                    ornplants2 = False
                    Loop = False
                    break
                elif option == 5:
                    Loop = False
                    break
        else:
            print("Invalid Option. Please choose between 1 and 2.")
            continue

