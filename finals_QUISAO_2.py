#Quisao, Deriel Edzel D.
#BSIT - 2A

import getpass

#Pharmacy Accounts
admin_acc = {"admin": "FMP4301"}
pharm_acc = {"pharm": "fullmetal"}

#Medicines
meds_price = {"Paracetamol - 500mg": 1.50, "Ascorbic Acid - 100mg": 1.50, "Ascorbic Acid - 500mg": 2, "Aspirin - 80mg": 4,
                "Amoxicillin - 250mg": 2.50, "Amoxicillin - 500mg": 2.70, "Amlodipine - 10mg": 1.75, "Amlodipine - 5mg": 0.75,
                "Cetirizine - 10mg": 2, "Ibuprofen - 200mg": 2.25, "Ibuprofen - 400mg": 2, "Mefenamic Acid - 500mg": 2.75}

#Containers
med_search = {}
meds_order = {}
subtotal = []


class Pharmacist:
    def __init__(self):
        print("\n\t\t----- Full Metal Pharmacy Stocks -----\n")
        self.meds_price = meds_price
        
    def ShowStocks(self):
        print ("\n\t\t----- Available Stocks -----\n")
        for key, value in meds_price.items():
            print (key, " [", value, "pesos per piece ]")

    def AddMeds(self, add_med, add_price):
        self.add_med = add_med
        self.add_price = add_price

        meds_price.update({self.add_med : self.add_price})

    def RemStocks(self, rem_med):
        self.rem_med = rem_med
        if self.rem_med in meds_price:
            del meds_price[self.rem_med]
        else:
            pass
    
    def UpdateStocks(self, update_name, update_price):
        self.update_name = update_name
        self.update_price = update_price

        meds_price.update(self.update_price)

class Customer:
    def ShowMeds(self):
        print("\n")
        for key, value in meds_price.items():
            print (key, " [", value, "pesos per piece ]")

    def MedsOrder(self, med_name, piece_price, med_quan):
        self.med_name = med_name
        self.med_quan = med_quan
        self.piece_price = piece_price

        self.Total = self.piece_price * self.med_quan
        subtotal.append(self.Total)

        meds_order.setdefault(med_name, [])
        meds_order[self.med_name].append(self.Total)


def MainMenu():
    print ("\t\t ------ Welcome to FullMetal Pharmacy ------\n")
    print ("1 [Admin Account]\n2 [Pharmacist Account]\n3 [Customer Account]")

def PharmacistMenu():
    print ("1 [Show Stocks]\n2 [Add to Stocks]\n3 [Remove from Stocks]\n4 [Edit Stock Price]\n5 [Back to Main Menu]")

def CustomerMenu():
    print ("1 [Show Available Medicine]\n2 [Search Medicine]\n3 [Order Medicine]\n4 [Back to Main Menu]")

def AdminMenu():
    print ("1 [Edit Pharmacy Account/s]\n2 [Back to Main Menu]")


def Main():
    show_menu = True
    while show_menu == True:
        MainMenu()
        user_choice = input("\nWhich user would you be?\n-----> ")
        if user_choice == "1":
            print ("\n\t\t ------ Admin Account ------\n")
            print ("Enter your LOGIN CREDENTIALS...\n")
            admin_user = input("USERNAME: ")
            admin_pass = getpass.getpass("PASSWORD: ")
            for key, value in admin_acc.items():
                if admin_user == key and admin_pass == value:
                    print ("\t\t\nLOGIN SUCCESSFUL\n")
                    while True:
                        AdminMenu()
                        admin_choice1 = input("\nWhat would you like to do?\n-----> ")
                        if admin_choice1 == "1":
                            print ("1 [Show Account/s]\n2 [Add Account]\n3 [Delete Account]\n4 [Return]")
                            admin_choice2 = input("\nWhat would you like to do?\n-----> ")

                            if admin_choice2 == "1":
                                for key, value in pharm_acc.items():
                                    print ("\nUsername:", key,"\nPassword:", value, "\n")
                            elif admin_choice2 == "2":
                                print ("Enter CREDENTIALS to ADD...\n")
                                add_user = input("USERNAME: ")
                                add_pass = input("PASSWORD: ")
                                pharm_acc.update({add_user :add_pass})
                                print (">>>>> ACCOUNT SUCCESFULLY ADDED <<<<<\n")
                            elif admin_choice2 == "3":
                                print ("Enter CREDENTIALS to DELETE...\n")
                                del_user = input("USERNAME: ")
                                del pharm_acc[del_user]
                                print ("")
                            elif admin_choice2 == "4":
                                print ("\n>>>>> RETURN <<<<<\n")
                                continue
                            else:
                                print ("\n*****Invalid Input*****\n")
                        elif admin_choice1 == "2":
                            print ("\n>>>>> Back to MAIN MENU <<<<<\n")
                            break
                        else:
                            print ("\n*****Invalid Input*****\n")
                else:
                    print ("\n*****Incorrect username or password*****\n")


        elif user_choice == "2":
            pharm_menu = True
            while pharm_menu == True:
                print ("\n\t\t ------ Pharmacist Account ------\n")
                print ("Enter your LOGIN CREDENTIALS...\n")
                pharm_user = input("USERNAME: ")
                pharm_pass = getpass.getpass("PASSWORD: ")
                for key, value in pharm_acc.items():
                    if pharm_user == key and pharm_pass == value:
                        print ("\n\t\tLOGIN SUCCESSFUL\n")
                        while True:
                            pharm = Pharmacist()
                            PharmacistMenu()
                            pharm_choice = input("\nWhat would you like to do?\n-----> ")
                            if pharm_choice == "1":
                                pharm.ShowStocks()
                            elif pharm_choice == "2":
                                med = input("\nEnter Medicine name: ")
                                price = float(input("Enter Medicine price: "))
                                pharm.AddMeds(med, price)
                                print("\n\t\tADDED to STOCKS!\n")
                            elif pharm_choice == "3":
                                rem = input("\nEnter Medicine to remove: ")
                                pharm.RemStocks(rem)
                            elif pharm_choice == "4":
                                name_upd = input("\nEnter name of medicine to update: ")
                                for key, value in meds_price.items():
                                    if name_upd == key in meds_price:
                                        price_upd = float(input("Enter updated price: "))
                                        pharm.UpdateStocks(name_upd, {key:price_upd})
                                        print("\n\t\tPRICE UPDATED!\n")
                                        break
                                    elif name_upd == key not in meds_price:
                                        print ("\n\t\tNo Stocks!\n")
                            elif pharm_choice == "5":
                                print ("\n>>>>> Back to MAIN MENU <<<<<\n")
                                pharm_menu = False
                                break
                    else:
                        print ("\n\t\tIncorrect username or password\n")
                        pharm_menu = False
                        break

        elif user_choice == "3":
            custom_menu = True
            while custom_menu == True:
                print ("\n\t\t ------ Customer Interface ------\n")
                custom = Customer()
                CustomerMenu()
                custom_choice = input("\nWhat would you like to do?\n-----> ")
                if custom_choice == "1":
                    custom.ShowMeds()
                    continue
                elif custom_choice == "2":
                    custom_search = input("\nEnter the Medicine name to Search:\nEx: Paracetamol - 500mg\t\t-----> ")
                    for key, value in meds_price.items():
                        if custom_search == key in meds_price:
                            print ("\n\t\tMedicine Found!\n", key, " [", value, "pesos per piece ]\n")
                            break
                        elif custom_search != key in meds_price:
                            print ("\n\t\tSearching Medicine...")
                        else:
                            print ("\n\t\tMedicine Unavailable\n")
                elif custom_choice == "3":
                    custom_order = True
                    while custom_order == True:
                        print ("\n\t\t ------ Customer Order ------\n")
                        enter_name = input("\nPlease enter your name to order: ")
                        order = input("Enter the medicine you want to order:\nEx: Paracetamol - 500mg\t\t-----> ")
                        for key, value in meds_price.items():
                            if order == key in meds_price:
                                quantity = eval(input("How many pieces?\n----->  "))
                                custom.MedsOrder(key, value, quantity)
                                print ("\nFor", enter_name, "...")
                                for key, value in meds_order.items():
                                    print ("\nOrder Receipt:\n[", key, "] x", quantity, "\n=", value, "pesos")

                                another_order = input("\nWould you like to order another medicine? [yes or no]\n-----> ")
                                if another_order == "yes":
                                    continue
                                else:
                                    print ("\n\t\tYour Order Total is [", sum(subtotal), "] pesos")
                                    print ("\n\t\t ------ THANK YOU FOR YOUR PATRONAGE ------")
                                    print ("\n\t\t     ------ Please visit us again ------\n\n")
                                    custom_order = False
                                    custom_menu = False
                                    continue
                             
                            elif order == key not in meds_price:
                                print ("\n\t\tMedicine Unavailable\n")
                                break
                
                elif custom_choice == "4":
                    print ("\n>>>>> Back to MAIN MENU <<<<<\n")
                    custom_menu = False
                    break
        else:
            print ("\n*****Invalid Input*****\n")
            continue                       

if __name__ == "__main__":
    Main()