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

    def assign_factions(self, faction1: faction, faction2: faction, faction3: faction):
        self.faction1 = faction1
        self.faction2 = faction2
        self.faction3 = faction3

    @property
    def starting_weapon_points(self):
        return self.__starting_weapon_points

    @property
    def starting_armor_points(self):
        return self.__starting_armor_points

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
        if(faction._alive == False):
            print("The faction you want to sell weapons is dead!")
            return False
        elif(self.__left_weapon_points < weapon_points):
            print("You try to sell more weapons than you have in possession.")
            return False

        self.revenue(self.revenue + faction.purchase_weapons(weapon_points))
        self.left_weapon_points(self.left_weapon_points - weapon_points)
        
        print("Weapons sold!")

        return True

    def sell_armors(self, faction: faction, armor_points):
        if(faction._alive == False):
            print("The faction you want to sell armors is dead!")
            return False
        elif(self.__left_armor_points < armor_points):
            print("You try to sell more armors than you have in possession.")
            return False

        self.revenue(self.revenue + faction.purchase_armors(armor_points))
        self.left_armor_points(self.left_armor_points - armor_points)
        
        print("Armors sold!")
        
        return True

    def end_turn(self):
        self.left_weapon_points(self.starting_weapon_point())
        self.left_armor_points(self.starting_armor_point())