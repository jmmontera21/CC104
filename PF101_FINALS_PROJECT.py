#John Marlon V. Montera
#BSIT - 2A

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
            if add2_order.lower() == "yes" or add2_order.lower() == "y":
                myOrnPlants.addplant()
                myOrnPlants.displayplants()
                continue
            elif add2_order.lower() == "no" or add2_order.lower() == "n":
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
            if description.lower() == "yes" or description.lower() == "y":
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
            elif description.lower() == "no" or description.lower() == "n":
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
            if additional_thing.lower() == "yes" or additional_thing.lower() == "y":
                myOrnPlants.inclusionoffer()
                inmaterial = input("Please select an inclusion for your ornamental plant : ")
                if inmaterial in self.list_of_inclusion_offer:
                    total_order.setdefault(plant,[])
                    total_order[plant].append(inmaterial)
                    print("You have added",inmaterial)
                    subtotal.append(Price_offer[inmaterial])
                    print("Your total order is worth",subtotal,"pesos.")
                    continue
                else:
                    total_order.setdefault(plant,[])
                    print(inmaterial,"is not included in the list")
                    continue
            elif additional_thing.lower() == "no" or additional_thing.lower() == "n":
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
            else:
                print("Okay, thank you for your interest in selling your ornamental plant.")
            break
        selling = False

    def check_order(self):
        Additional = True
        while Additional:
            add_order = input("Would you like to add another ornamental plants in your order ? (yes/no)")
            if add_order.lower() == "yes" or add_order.lower() == "y":
                myOrnPlants.buyplant(Ornamental_plants)
                myOrnPlants.displayplants()
                continue
            elif add_order.lower() == "no" or add_order.lower() == "n":
                for key, value in total_order.items():
                    print("You have ordered the following ornamental plant ",key,"with the following inclusion ",value)
                    print("OVERALL ORDER")
                    print(total_order)
                    print("Proceed to option 4 to see your receipt, thank you.") 
                    Additional = False
                    break
            else:
                print("Not an option") 
                continue
    
    def checkout(self):
        print("=============================================== OFFICIAL RECEIPT =========================================================")
        print("Your total order is worth", sum(subtotal), "pesos")
        print("Thank you for ordering, Ma'am/Sir", name, ".", age, "years old. ""Contact number is", contact_number, " and located at", address, ".")
        print("Nearest landmark is at", landmark, ".")
        print("Please wait for", int(distance) * 7, "minutes. We'll deliver your ornamental plant as soon as possible.")
        print("----------------------------- THANK YOU FOR ORDERING AT JMM ORNAMENTAL PLANTS STORE, VISIT AGAIN -------------------------")

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
    myOrnPlants = Ornamental_plants(["Silver Nerve Plant", "Fibre Optic Grass Plant", "Snake Plant", "String Of Pearls", "Peace Lily", "Chinese Money Plant", "Air Plant", "Water Bamboo", "Bonsai", "Bunny Ear Cactus"], ["Fertilizer", "Quality Pot", "Pebbles", "Marbles"])
    Price_plants = {"Silver Nerve Plant" : 120,"Fibre Optic Grass Plant" : 100,"Snake Plant" : 150,"String Of Pearls" : 130,"Peace Lily" : 120,"Chinese Money Plant" : 240, "Air Plant" : 290,"Water Bamboo" : 130,"Bonsai" : 200,"Bunny Ear Cactus" : 150}
    Price_offer = {"Fertilizer" : 30, "Quality Pot" : 50, "Pebbles" : 20, "Marbles" : 10}
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
                            Additional = True
                            while Additional:
                                minus_order = input("Would you like to remove another ornamental plants in the list ? (yes/no)")
                                if minus_order.lower() == "yes" or minus_order.lower() == "y":
                                    myOrnPlants.removeplant()
                                    myOrnPlants.displayplants()
                                    continue
                                elif minus_order.lower() == "no" or minus_order.lower() == "n":
                                    print("Okay, thank you.")
                                    break
                                else:
                                    print("Invalid option")
                                    continue
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
                option = eval(input("\n[1] - Show Available Ornamental Plants \n[2] - Order Ornamental Plants \n[3] - Sell Your Ornamental Plants \n[4] - Receipt \nChoose an option : "))
                if option == 1:
                    myOrnPlants.displayplants()
                    myOrnPlants.plantinfo()
                elif option == 2:
                    myOrnPlants.buyplant(Ornamental_plants)
                    myOrnPlants.check_order()
                elif option == 3:
                    myOrnPlants.postplant()
                    Additional2 = True
                    while Additional2:
                        add1_order = input("Would you like to sell/upload another ornamental plant in our online store ? (yes/no)")
                        if add1_order.lower() == "yes" or add1_order.lower() == "y":
                            myOrnPlants.postplant()
                            continue
                        elif add1_order.lower() == "no" or add1_order.lower() == "n":
                            print("Next")
                            Additional2 = False
                            break
                        else:
                            print("Not an option.")
                elif option == 4:
                    landmark = input("Any nearest landmark near at your place ? ")
                    distance = eval(input("How far is your house from our physical store (in km) ? "))
                    myOrnPlants.checkout()
                    orn_plants2 = False
                    Loop = False
                    break
        else:
            print("Invalid Option. Please choose between 1 and 2.")
            continue

