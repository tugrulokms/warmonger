from factions import *

class Merchant():
    def __init__(self):
        self.__starting_weapon_point = 10
        self.__starting_armor_point = 10
        self.__left_weapon_points = self.__starting_weapon_point
        self.__left_armor_points = self.__starting_armor_point
        self.__revenue = 0

    def __init__(self, __starting_weapon_point, __starting_armor_point):
        self.__starting_weapon_point = __starting_weapon_point
        self.__starting_armor_point = __starting_armor_point
        self.__left_weapon_points = __starting_weapon_point
        self.__left_armor_points = __starting_armor_point
        self.__revenue = 0

    def assign_factions(self, orcs: Orcs, dwarves: Dwarves, elves: Elves):
        self.orcs = orcs
        self.dwarves = dwarves
        self.elves = elves

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

    def sell_weapons(self, faction: faction, weapon_points):
        if(faction.alive == False):
            print("The faction you want to sell weapons is dead!")
            return False
        elif(self.left_weapon_points < weapon_points):
            print("You try to sell more weapons than you have in possession.")
            return False

        self.revenue += faction.purchase_weapons(weapon_points)
        self.left_weapon_points -= weapon_points
        
        print("Weapons sold!")
        print("Weapon points left: " + str(self.left_weapon_points))

        return True

    def sell_armors(self, faction: faction, armor_points):
        if(faction.alive == False):
            print("The faction you want to sell armors is dead!")
            return False
        elif(self.left_armor_points < armor_points):
            print("You try to sell more armors than you have in possession.")
            return False

        self.revenue += faction.purchase_armors(armor_points)
        self.left_armor_points -= armor_points
        
        print("Armors sold!")
        print("Armor points left: " + str(self.left_armor_points))

        return True

    
    def sell_selected_faction(self, faction_selection):
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
                    self.sell_weapons(self.orcs, amount_selection)
                elif(faction_selection == 2):
                    self.sell_weapons(self.dwarves, amount_selection)
                elif(faction_selection == 3):
                    self.sell_weapons(self.elves, amount_selection)

            else:
                print("You can't enter any non-positive value.")

        elif(equipment_selection == 2):
            print("Enter how much armors do you want to sell:")

            amount_selection = int(input())

            if(amount_selection > 0):
                if(faction_selection == 1):
                    self.sell_armors(self.orcs, amount_selection)
                elif(faction_selection == 2):
                    self.sell_armors(self.dwarves, amount_selection)
                elif(faction_selection == 3):
                    self.sell_armors(self.elves, amount_selection)

            else:
                print("You can't enter any non-positive value.")

    def end_turn(self):
        self.left_weapon_points = self.starting_weapon_point
        self.left_armor_points = self.starting_armor_point
