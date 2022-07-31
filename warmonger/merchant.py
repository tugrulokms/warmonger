from factions import *

# Merchant class. Player will play as this class to maximize their profits.
class Merchant():
    def __init__(self, *args):

        # Optional constructor
        if(len(args) == 2):
            self.__starting_weapon_point = args[0]
            self.__starting_armor_point = args[1]
            self.__left_weapon_points = self.__starting_weapon_point
            self.__left_armor_points = self.__starting_armor_point
            self.__revenue = 0
        # Default constructor
        else:
            self.__starting_weapon_point = 10
            self.__starting_armor_point = 10
            self.__left_weapon_points = self.__starting_weapon_point
            self.__left_armor_points = self.__starting_armor_point
            self.__revenue = 0

    # Assign battling factions to the merchant for easy manipulation, as player should access the factions by the merchant class.
    def assign_factions(self, orcs: Orcs, dwarves: Dwarves, elves: Elves):
        self.orcs = orcs
        self.dwarves = dwarves
        self.elves = elves

    # For encapsulation purposes
    @property
    def starting_weapon_point(self):
        return self.__starting_weapon_point

    @property
    def starting_armor_point(self):
        return self.__starting_armor_point

    @property
    def left_weapon_points(self):
        return self.__left_weapon_points

    @left_weapon_points.setter
    def left_weapon_points(self, left_weapon_points):
        self.__left_weapon_points = left_weapon_points

    @property
    def left_armor_points(self):
        return self.__left_armor_points

    @left_armor_points.setter
    def left_armor_points(self, left_armor_points):
        self.__left_armor_points = left_armor_points

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        self.__revenue = revenue

    # Sell weapons to the faction chosen by player
    def sell_weapons(self, faction: faction, weapon_points):

        # Can't sell weapons to a dead faction.
        if(faction.alive == False):
            print("The faction you want to sell weapons is dead!")
            return False

        # Can't sell weapons you don't currently have.
        elif(self.left_weapon_points < weapon_points):
            print("You try to sell more weapons than you have in possession.")
            return False

        # Revenue has increased by the amount given by the chosen faction.
        self.revenue += faction.purchase_weapons(weapon_points)

        # Merchants weapon points are reduced by the weapon sold. 
        self.left_weapon_points -= weapon_points
        
        print("Weapons sold!")
        print("Weapon points left: " + str(self.left_weapon_points))

        return True

    # Sell armors to the faction chosen by player
    def sell_armors(self, faction: faction, armor_points):

        # Can't sell armors to a dead faction.
        if(faction.alive == False):
            print("The faction you want to sell armors is dead!")
            return False

        # Can't sell armors you don't currently have.
        elif(self.left_armor_points < armor_points):
            print("You try to sell more armors than you have in possession.")
            return False

        # Revenue has increased by the amount given by the chosen faction.
        self.revenue += faction.purchase_armors(armor_points)

        # Merchants armor points are reduced by the weapon sold.
        self.left_armor_points -= armor_points
        
        print("Armors sold!")
        print("Armor points left: " + str(self.left_armor_points))

        return True

    # I added this method to make the code more readable and added it here since it is for the merchant class.
    # This method helps making selling equipment process more readable in the main file.
    # faction_selection parameter is selected in the main file to determine which faction to sell equipment to.
    def sell_selected_faction(self, faction_selection):
        # Selection menu for which equipment to sell.
        print("Choose which equipment to sell:")
        print("Weapons:\t\t(1)")
        print("Armor:\t\t\t(2)")
        print("Main menu:\t\t(any other input)")

        # User chooses which equipment to sell.
        equipment_selection = int(input("Choose equipment: "))

        # User chooses weapons.
        if(equipment_selection == 1):
            print("Enter how much weapons do you want to sell:")

            # User enters an amount to determine how much weapons to sell.
            amount_selection = int(input("Enter amount: "))

            # Entered amount can't be negative
            if(amount_selection > 0):
                # If Orcs are selected in faction selection, sell weapons to Orcs by given amount.
                if(faction_selection == 1):
                    self.sell_weapons(self.orcs, amount_selection)
                # If Dwarves are selected in faction selection, sell weapons to Dwarves by given amount.
                elif(faction_selection == 2):
                    self.sell_weapons(self.dwarves, amount_selection)
                # If Elves are selected in faction selection, sell weapons to Elves by given amount.
                elif(faction_selection == 3):
                    self.sell_weapons(self.elves, amount_selection)

            else:
                print("You can't enter any non-positive value.")

        # User chooses armors.
        elif(equipment_selection == 2):
            print("Enter how much armors do you want to sell:")

             # User enters an amount to determine how much armors to sell.
            amount_selection = int(input())

            # Entered amount can't be negative
            if(amount_selection > 0):
                # If Orcs are selected in faction selection, sell armors to Orcs by given amount.
                if(faction_selection == 1):
                    self.sell_armors(self.orcs, amount_selection)
                # If Dwarves are selected in faction selection, sell weapons to Dwarves by given amount.
                elif(faction_selection == 2):
                    self.sell_armors(self.dwarves, amount_selection)
                # If Elves are selected in faction selection, sell weapons to Elves by given amount.
                elif(faction_selection == 3):
                    self.sell_armors(self.elves, amount_selection)

            else:
                print("You can't enter any non-positive value.")

    # End player turn 
    def end_turn(self):
        # Set left weapon and armor points to the started value
        self.left_weapon_points = self.starting_weapon_point
        self.left_armor_points = self.starting_armor_point
