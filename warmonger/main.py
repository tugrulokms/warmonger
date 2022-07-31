from factions import *
from merchant import *

restart = int(1)

print("**********Welcome to The Warmonger: A New Dimension!**********")
print("")
print("In this game, you will play as a war merchant trying to keep a war in balance to profit the most!")
print("")

while(restart == 1):

    selection = int(1)
    restart = 0

    merchant = Merchant(10, 10)

    merchant.assign_factions(Elves("Elves", 15, 15, 35, 3),
                            Orcs("Orcs", 30, 10, 50, 5),
                            Dwarves("Dwarves", 20, 12, 60, 2))

    merchant.orcs.assign_enemies(merchant.dwarves, merchant.elves)
    merchant.dwarves.assign_enemies(merchant.elves, merchant.orcs)
    merchant.elves.assign_enemies(merchant.orcs, merchant.dwarves)

    while(selection > 0):

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
            merchant.orcs.print()
            merchant.dwarves.print()
            merchant.elves.print()
            print("")
        elif(selection == 2):
            print("Choose one of the factions to sell equipment:")
            print("Elves:\t\t(1)")
            print("Orcs:\t\t(2)")
            print("Dwarves:\t(3)")
            print("Main menu:\t(any other input)")

            faction_selection = int(input())

            if(faction_selection == 1):
                merchant.sell_selected_faction(1)
            elif(faction_selection == 2):
                merchant.sell_selected_faction(2)
            elif(faction_selection == 3):
                merchant.sell_selected_faction(3)
            else:
                pass
        elif(selection == 3):
            if(merchant.orcs.alive == True):
                merchant.orcs.perform_attack()
            if(merchant.dwarves.alive == True):
                merchant.dwarves.perform_attack()
            if(merchant.elves.alive == True):
                merchant.elves.perform_attack()

            print("Ending turn...")

            merchant.end_turn();
            merchant.orcs.end_turn();
            merchant.dwarves.end_turn();
            merchant.elves.end_turn();

        elif(selection == 4):

            print("Ending current game...")

            selection = 0
            restart = 1
        else:
            selection = 1
            print("Invalid command: Use commands shown to navigate through the game menu.")