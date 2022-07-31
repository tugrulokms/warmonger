from factions import *
from merchant import *

# This value is used to end a game
restart: int = 1

print("********** Welcome to The Warmonger: A New Dimension! **********")
print("")
print("In this game, you will play as a war merchant trying to keep a war in balance to profit the most!")
print("")

# When the game is first lauched or a game is ended, this part of code runs.
while(restart == 1):

    # Selection value is pre-selected here to ensure the next loop goes smoothly.
    selection: int = 1

    # Restart value is pre-selected here to ensure the next loop doesn't iterate here if current game isn't ended.
    restart = 0

    # Initialize Merchant class
    merchant = Merchant()

    # Assign factions to the merchant
    merchant.assign_factions(Orcs("Orcs", 40, 25, 40, 3),
                            Dwarves("Dwarves", 30, 20, 60, 2),
                            Elves("Elves", 30, 40, 40, 2))

    # Assign enemies to Orcs
    merchant.orcs.assign_enemies(merchant.dwarves, merchant.elves)
    # Assign enemies to Dwarves
    merchant.dwarves.assign_enemies(merchant.elves, merchant.orcs)
    # Assign enemies to Elves
    merchant.elves.assign_enemies(merchant.orcs, merchant.dwarves)

    # While in a game, this part of code runs.
    while(selection > 0):

        print("----------------------- MENU ------------------------")
        print("See the information of faction(s):\t(1)")
        print("Sell weapons or armor:\t\t\t(2)")
        print("End your turn :\t\t\t\t(3)")                
        print("End current game :\t\t\t(4)")                
        print("Quit :\t\t\t\t\t(0)")
        
        # Select action to perform
        selection = int(input("Select action: "))  

        # Quits the application if this is selected.
        if(selection == 0):
            print("Bye!")
            pass

        # Print information of all factions in the game.
        elif(selection == 1):
            merchant.orcs.print()
            merchant.dwarves.print()
            merchant.elves.print()
            print("")

        # Sell weapons or armor to the selected faction.
        elif(selection == 2):
            print("Choose one of the factions to sell equipment:")
            print("Orcs:\t\t(1)")
            print("Dwarves:\t(2)")
            print("Elves:\t\t(3)")
            print("Main menu:\t(any other input)")

            # Choose faction
            faction_selection = int(input("Choose faction: "))

            # Sell the type and amount of equipment selected in this method to the chosen faction.
            if(faction_selection == 1):
                # Sell the type and amount of equipment selected in this method to the Orcs.
                merchant.sell_selected_faction(1)
            elif(faction_selection == 2):
                # Sell the type and amount of equipment selected in this method to the Dwarves.
                merchant.sell_selected_faction(2)
            elif(faction_selection == 3):
                # Sell the type and amount of equipment selected in this method to the Elves.
                merchant.sell_selected_faction(3)
            else:
                pass

        # End your current turn(day)
        elif(selection == 3):
            
            # Alive factions performs attack and battle with remaining factions.
            if(merchant.orcs.alive == True):
                merchant.orcs.perform_attack()
            if(merchant.dwarves.alive == True):
                merchant.dwarves.perform_attack()
            if(merchant.elves.alive == True):
                merchant.elves.perform_attack()

            print("Ending turn...")

            # End turn for merchant and battling factions.
            merchant.end_turn();
            merchant.orcs.end_turn();
            merchant.dwarves.end_turn();
            merchant.elves.end_turn();

        # End the current game.
        elif(selection == 4):

            print("!!")
            print("Ending current game...")
            print("!!")

            # Selection value is set to 0 to get out of the game.
            selection = 0

            # Restart value is set to 1 to reinitialize the merchant and faction values.
            restart = 1
        
        # If another input is given
        else:
            # Go back to menu
            selection = 1
            print("Invalid command: Use commands shown to navigate through the game menu.")