class faction:
    def __init__(self, *args):

        #   if parameters are given as shown: (name, units, attack points, health points, regen num)
        #   values will be set accordingly
        if(len(args) == 5):
            self._name = args[0]
            self._units = args[1]
            self._attack_points = args[2]
            self._health_points = args[3]
            self._unit_regen_num = args[4]
            self._total_health = int(self._units * self._health_points)
            self._alive = True

        #   if no parameter is given, a faction will have these values as default
        else:
            self._name = "Default"
            self._units = 10
            self._attack_points = 10
            self._health_points = 10
            self._unit_regen_num = 2
            self._total_health = int(self._units * self._health_points)
            self._alive = True

    # For encapsulation purposes
    @property
    def units(self):
        return self._units

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._units = units

    @property
    def attack_points(self):
        return self._attack_points

    @attack_points.setter
    def attack_points(self, attack_points):
        self._attack_points = attack_points

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, health_points):
        self._health_points = health_points

    @property
    def total_health(self):
        return self._total_health

    @total_health.setter
    def total_health(self, total_health):
        self._total_health = total_health

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

    # Assign enemies to the faction. The faction will attack to these factions.
    def assign_enemies(self, _enemy1: 'faction', _enemy2: 'faction'):
            self._enemy1 = _enemy1;
            self._enemy2 = _enemy2;

    # For encapsulation purposes
    @property
    def enemy1(self):
        return self._enemy1

    @enemy1.setter
    def enemy1(self, enemy1: 'faction'):
        self._enemy1 = enemy1

    @property
    def enemy2(self):
        return self._enemy2

    @enemy2.setter
    def enemy2(self, enemy2: 'faction'):
        self._enemy2 = enemy2

    # These methods are not defined in here, its defined in the according subclass, as the faction type dramaticly changes the way and the amount of damage performed and received. Also every faction has its own way of purchasing equipment.
    def perform_attack(self):
        pass
    def receive_attack(self):
        pass
    def purchase_weapons(self):
        pass
    def purchase_armors(self):
        pass

    # Print faction information
    def print(self):

        # Text for alive status
        if(self.alive == True):
            status = "Alive"
        elif(self.alive == False):
            status = "Defeated"

        print("Faction Name:\t\t" + self._name, 
                "Status:\t\t\t" + status,
                "Number of Units:\t{}".format(self._units),
                "Attack Point:\t\t{}".format(self._attack_points),
                "Health Point:\t\t{}".format(self._health_points),
                "Unit Regen Number:\t{}".format(self._unit_regen_num),
                "Total Faction Health:\t{}".format(self._total_health),
                sep='\n')

    # End turn, and set alive status if the faction has no health left. If it does, regen units by faction unit regen number.
    def end_turn(self):

        # Set units to 0 if the units value is negative.
        if(self._units < 0):
            self._units = 0

        # Set alive status if the faction has no health left.
        if(self._units == 0):
            self._total_health = 0
            self._alive = False

        # Regen units by faction unit regen number.
        else:
            self.units += self._unit_regen_num
            self._total_health = int(self.units * self.health_points)

# Subclass of faction class
class Orcs(faction):

    # Same as faction class
    def __init__(self, *args):
        if(len(args) == 5):
            super().__init__(args[0], args[1], args[2], args[3], args[4])
        else:
            super().__init__()

    # Orcs perform attack behaviour - defined here 
    def perform_attack(self):

        # Attack with all forces if only one faction is alive
        if((self.enemy1.alive == True and self.enemy2.alive == False)):
            # The parameter 1 is the unit percentage sent of the attacker faction
            self.enemy1.receive_attack(self, 1);
        elif((self.enemy1.alive == False and self.enemy2.alive == True)):
            self.enemy2.receive_attack(self, 1)
        # Divide forces as instructed if both factions are alive
        elif(self.enemy1.alive == True and self.enemy2.alive == True):

            if(type(self.enemy1) == Elves):
                self.enemy1.receive_attack(self, 0.7)
                self.enemy2.receive_attack(self, 0.3)

            if(type(self.enemy1) == Dwarves):
                self.enemy1.receive_attack(self, 0.3)
                self.enemy2.receive_attack(self, 0.7)

    # Orcs receive attack behaviour - defined here. Unit percentage is the percentage of units brought by the attacker faction.
    def receive_attack(self, attacker: faction, unit_percentage):

        # This damage coefficient is added because Orcs received attack is affected by the type of attacking faction.
        damage_coefficient = 1

        if(type(attacker) == Elves):
            damage_coefficient = 0.75

        elif(type(attacker) == Dwarves):
            damage_coefficient = 0.8
 
        # Reduce units by total damage received divided by health point
        self.units -= int(((unit_percentage * attacker._units) * attacker._attack_points * damage_coefficient) / attacker._health_points)
            
    # Orcs purchase weapon behaviour - defined here 
    def purchase_weapons(self, weapon_points):

        # Orcs weapon bonus
        self.attack_points += 2 * weapon_points
        # Orcs payment behaviour for weapons
        gold = 20 * weapon_points

        return gold

    # Orcs purchase armor behaviour - defined here
    def purchase_armors(self, armor_points):

        # Orcs armor bonus
        self.health_points += 3 * armor_points
        # Update total health as health points by unit has changed.
        self.total_health = self.units * self.health_points

        # Orcs payment behaviour for armors
        gold = armor_points

        return gold

    # Print faction information - same as superclass but it also prints Orcs battlecry.
    def print(self):
        print('\n"Stop running, you\'ll only die tired!"\n')
        super().print()

# Subclass of faction class
class Dwarves(faction):
    
    # Same as faction class
    def __init__(self, *args):
        if(len(args) == 5):
            super().__init__(args[0], args[1], args[2], args[3], args[4])
        else:
            super().__init__()

    # Dwarves perform attack behaviour - defined here.
    def perform_attack(self):
        # Attack with all forces if only one faction is alive
        if((self.enemy1.alive == True and self.enemy2.alive == False)):
            self.enemy1.receive_attack(self, 1);
        # Same but for other faction
        elif((self.enemy1.alive == False and self.enemy2.alive == True)):
            self.enemy2.receive_attack(self, 1)
        # Divide forces by half if both enemy factions are alive
        elif(self.enemy1.alive == True and self.enemy2.alive == True):
            self.enemy1.receive_attack(self, 0.5)
            self.enemy2.receive_attack(self, 0.5)

    # Dwarves receive attack behaviour - defined here. Unit percentage is the percentage of units brought by the attacker faction.
    def receive_attack(self, attacker: faction, unit_percentage):
        # Reduce units by total damage received divided by health point
        self.units -= int(((unit_percentage * attacker._units) * attacker._attack_points) / attacker._health_points)
        
    # Dwarves purchase weapon behaviour - defined here
    def purchase_weapons(self, weapon_points):

        # Dwarves weapon bonus
        self.attack_points += weapon_points

        # Dwarves payment behaviour for weapons
        gold = 10 * weapon_points

        return gold

    # Dwarves purchase armor behaviour - defined here
    def purchase_armors(self, armor_points):

        # Dwarves armor bonus
        self.health_points += 2 * armor_points
        # Update total health as health points by unit has changed.
        self.total_health = self.units * self.health_points

        # Dwarves payment behaviour for armors
        gold = 3 * armor_points

        return gold
        
    # Print faction information - same as superclass but it also prints Dwarves battlecry.
    def print(self):
        print('\n"Taste the power of our axes!"\n')
        super().print()

# Subclass of faction class
class Elves(faction):

    # Same as faction class
    def __init__(self, *args):
        if(len(args) == 5):
            super().__init__(args[0], args[1], args[2], args[3], args[4])
        else:
            super().__init__()

    # Elves perform attack behaviour - defined here.
    def perform_attack(self):
        # If only one enemy faction is alive attack them with all units
        if((self.enemy1.alive == True and self.enemy2.alive == False)):
            if(type(self.enemy1) == Dwarves):
                # Elves attack point increases by %150 when attacking Dwarves.
                self.attack_points(self.attack_points * 1.5)
                self.enemy1.receive_attack(self.enemy1, 1)
                self.attack_points(self.attack_points / 1.5)
            else:
                self.enemy1.receive_attack(self.enemy1, 1)

        # Same but for other faction
        elif((self.enemy1._alive == False and self._enemy2._alive == True)):
            if(type(self.enemy2) == Dwarves):
                # Same as above
                self.attack_points = self.attack_points * 1.5
                self.enemy2.receive_attack(self.enemy2, 1)
                self.attack_points = int(self.attack_points / 1.5)
            else:
                self.enemy2.receive_attack(self._enemy2, 1)

        # If both enemy factions are alive, %60 of units attack Orcs, %40 attack Dwarves
        elif(self.enemy1.alive == True and self.enemy2.alive == True):
            if(type(self.enemy1) == Dwarves):
                # Same as above
                self.attack_points = self.attack_points * 1.5
                self.enemy1.receive_attack(self._enemy1, 0.4)
                self.attack_points = int(self.attack_points / 1.5)

                self.enemy2.receive_attack(self.enemy2, 0.6)
            elif(type(self.enemy2) == Dwarves):
                self.enemy1.receive_attack(self.enemy1, 0.6)

                # Same as above
                self.attack_points = self.attack_points * 1.5
                self.enemy2.receive_attack(self.enemy2, 0.4)
                self.attack_points = int(self.attack_points / 1.5)

    # Elves receive attack behaviour - defined here. Unit percentage is the percentage of units brought by the attacker faction.
    def receive_attack(self, attacker: faction, unit_percentage):

        # This damage coefficient is added because Elves received attack is affected by the type of attacking faction.
        damage_coefficient = 1

        if(type(attacker) == Orcs):
            damage_coefficient = 1.25
        elif(type(attacker) == Dwarves):
            damage_coefficient = 0.75
        
        # Reduce units by total damage received divided by health point
        self.units -= int(((unit_percentage * attacker._units) * attacker._attack_points * damage_coefficient) / attacker._health_points)

    # Elves purchase weapon behaviour - defined here
    def purchase_weapons(self, weapon_points):

        # Elves weapon bonus
        self.attack_points += 2 * weapon_points
        
        # Elves payment behaviour for weapons
        gold = 15 * weapon_points

        return gold

    # Elves purchase armor behaviour - defined here
    def purchase_armors(self, armor_points):

        # Elves armor bonus
        self.health_points +=  4 * armor_points
        # Update total health, as health points by unit has changed.
        self.total_health = self.units * self.health_points

        # Elves payment behaviour for armors
        gold = 5 * armor_points

        return gold
        
    def print(self):
        print('\n"You cannot reach our elegance."\n')
        super().print()