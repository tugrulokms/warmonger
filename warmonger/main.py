from factions import *
from merchant import *

def sell_selected_faction(merchant: Merchant, faction_selection):
    print("Choose what equipment to sell:")
    print("Weapons:\t\t(1)")
    print("Armor:\t\t\t(2)")
    print("Main menu:\t\t(any other input)")

    equipment_selection = int(input())

    if(equipment_selection == 1):
        print("Enter how much weapons do you want to sell:")

        amount_selection = int(input())

        if(amount_selection > 0):
            if(faction_selection == 1):
                merchant.sell_weapons(merchant.faction1, amount_selection)
            elif(faction_selection == 2):
                merchant.sell_weapons(merchant.faction2, amount_selection)
            elif(faction_selection == 3):
                merchant.sell_weapons(merchant.faction3, amount_selection)

        else:
            print("You can't enter any non-positive value.")

    elif(equipment_selection == 2):
        print("Enter how much armors do you want to sell:")
        
        amount_selection = int(input())

        if(amount_selection > 0):
            if(faction_selection == 1):
                merchant.sell_armors(merchant.faction1, amount_selection)
            elif(faction_selection == 2):
                merchant.sell_armors(merchant.faction2, amount_selection)
            elif(faction_selection == 3):
                merchant.sell_armors(merchant.faction3, amount_selection)

        else:
            print("You can't enter any non-positive value.")

selection = 1
restart = 1

print("**********Welcome to The Warmonger: A New Dimension!**********")
print("")
print("In this game, you will play as a war merchant trying to keep a war in balance to profit the most!")
print("")
while(selection > 0):

    merchant = Merchant(10, 10)

    merchant.assign_factions(Elves("Elves", 15, 15, 35, 15),
                        Orcs("Orcs", 30, 10, 50, 10),
                        Dwarves("Dwarves", 20, 12, 60, 8))

    merchant.faction1.assign_enemies(merchant.faction2, merchant.faction3)
    merchant.faction2.assign_enemies(merchant.faction3, merchant.faction1)
    merchant.faction3.assign_enemies(merchant.faction1, merchant.faction2)

    print("----------------------- MENU ------------------------")
    print("See the information of faction(s):\t(1)")
    print("Sell weapons or armor:\t\t\t(2)")
    print("End your turn :\t\t\t\t(3)")                
    print("End current game :\t\t\t(4)")                
    print("Quit :\t\t\t\t\t(0)")

    selection = int(input())  

    if(selection == 0):
        pass
    elif(selection == 1):
        merchant.faction1.print()
        merchant.faction2.print()
        merchant.faction3.print()
        print("")
    elif(selection == 2):
        print("Choose one of the factions to sell equipment:")
        print("Elves:\t(1)")
        print("Orcs:\t(2)")
        print("Dwarves:\t(3)")
        print("Main menu:\t(any other input)")

        faction_selection = int(input())

        if(faction_selection == 1):
            sell_selected_faction(merchant, 1)
        elif(faction_selection == 2):
            sell_selected_faction(merchant, 2)
        elif(faction_selection == 3):
            sell_selected_faction(merchant, 3)
        else:
            pass
    elif(selection == 3):
        if(merchant.faction1._alive == True):
            merchant.faction1.perform_attack()
        if(merchant.faction2._alive == True):
            merchant.faction2.perform_attack()
        if(merchant.faction3._alive == True):
            merchant.faction3.perform_attack()
        print("-----------------")
        print("Ending turn...")
        print("-----------------")
        merchant.end_turn();
        merchant.faction1.end_turn();
        merchant.faction2.end_turn();
        merchant.faction3.end_turn();
    elif(selection == 4):
        restart = 1
    else:
        selection = 0
        print("Invalid command: Use commands shown to navigate through the game menu.")


