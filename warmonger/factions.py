class faction:
    def __init__(self):
        self._name = "Default"
        self._units = 0
        self._attack_points = 0
        self._health_points = 0
        self._unit_regen_num = 0
        self._total_health = 0
        self._alive = True

    def __init__(self, _name, _units, _attack_points, _health_points, _unit_regen_num):
        self._name = _name
        self._units = int(_units)
        self._attack_points = _attack_points
        self._health_points = _health_points
        self._unit_regen_num = _unit_regen_num
        self._total_health = int(_units * _health_points)
        self._alive = True

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

    def assign_enemies(self, _enemy1: 'faction', _enemy2: 'faction'):
            self._enemy1 = _enemy1;
            self._enemy2 = _enemy2;

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

    def perform_attack(self):
        pass
    def receive_attack(self):
        pass
    def purchase_weapons(self):
        pass
    def purchase_armors(self):
        pass
    def print(self):
        if(self._alive == True):
            status = "Alive"
        elif(self._alive == False):
            status = "Defeated"

        print("Faction Name:\t\t" + self._name, 
                "Status:\t\t\t" + status,
                "Number of Units:\t{}".format(self._units),
                "Attack Point:\t\t{}".format(self._attack_points),
                "Health Point:\t\t{}".format(self._health_points),
                "Unit Regen Number:\t{}".format(self._unit_regen_num),
                "Total Faction Health:\t{}".format(self._total_health),
                sep='\n')

    def end_turn(self):

        if(self._units < 0):
            self._units = 0

        if(self._units == 0):
            self._total_health = 0
            self._alive = False

        else:
            self.units(self.units + self._unit_regen_num) 
            self._total_health(int(self._units * self._health_points))

class Orcs(faction):

    def __init__(self, _name, _units, _attack_points, _health_points, _unit_regen_num):
        super().__init__(_name, _units, _attack_points, _health_points, _unit_regen_num)

    def perform_attack(self):

        if((self.enemy1.alive == True and self.enemy2.alive == False)):
            self.enemy1.receive_attack(self, 1);
        elif((self.enemy1.alive == False and self.enemy2.alive == True)):
            self.enemy2.receive_attack(self, 1)
        elif(self.enemy1.alive == True and self.enemy2.alive == True):

            if(type(self.enemy1) == Elves):
                self.enemy1.receive_attack(self, 0.7)
                self.enemy2.receive_attack(self, 0.3)

            if(type(self.enemy1) == Dwarves):
                self.enemy1.receive_attack(self, 0.3)
                self.enemy2.receive_attack(self, 0.7)

    def receive_attack(self, attacker: faction, unit_percentage):

        damage_coefficient = 1

        if(type(attacker) == Elves):
            damage_coefficient = 0.75

        elif(type(attacker) == Dwarves):
            damage_coefficient = 0.8
 
        self.units(self.units - int(((unit_percentage * attacker._units) * attacker._attack_points * damage_coefficient) / attacker._health_points))
            
    def purchase_weapons(self, weapon_points):

        self.attack_points(self.attack_points + (2 * weapon_points)) 
        gold = 20 * weapon_points

        return gold

    def purchase_armors(self, armor_points):

        self.health_points(self.health_points + (3 * armor_points)) 
        gold = armor_points

        return gold

    def print(self):
        print('\n"Stop running, you\'ll only die tired!"\n')
        super().print()

class Dwarves(faction):

    def __init__(self, _name, _units, _attack_points, _health_points, _unit_regen_num):
        super().__init__(_name, _units, _attack_points, _health_points, _unit_regen_num)

    def perform_attack(self):
        if((self.enemy1.alive == True and self.enemy2.alive == False)):
            self.enemy1.receive_attack(self, 1);
        elif((self.enemy1.alive == False and self.enemy2.alive == True)):
            self.enemy2.receive_attack(self, 1)
        elif(self.enemy1.alive == True and self.enemy2.alive == True):
            self.enemy1.receive_attack(self, 0.5)
            self.enemy2.receive_attack(self, 0.5)

    def receive_attack(self, attacker: faction, unit_percentage):
        self.units(self.units - int(((unit_percentage * attacker._units) * attacker._attack_points) / attacker._health_points))
        
    def purchase_weapons(self, weapon_points):
        self.attack_points(self.attack_points + weapon_points)
        gold = 10 * weapon_points

        return gold

    def purchase_armors(self, armor_points):
        self.health_points(self.health_points + (2 * armor_points))
        gold = 3 * armor_points

        return gold
        
    def print(self):
        print('\n"Taste the power of our axes!"\n')
        super().print()

class Elves(faction):

    def __init__(self, _name, _units, _attack_points, _health_points, _unit_regen_num):
        super().__init__(_name, _units, _attack_points, _health_points, _unit_regen_num)

    def perform_attack(self):
        if((self.enemy1.alive == True and self._enemy2.alive == False)):
            if(type(self._enemy1) == Dwarves):
                self.attack_points(self.attack_points * 1.5)
                self.enemy1.receive_attack(self.enemy1, 1)
                self.attack_points(self.attack_points / 1.5)
            else:
                self.enemy1.receive_attack(self.enemy1, 1)
        elif((self._enemy1._alive == False and self._enemy2._alive == True)):
            if(type(self._enemy2) == Dwarves):
                self.attack_points(self.attack_points * 1.5)
                self._enemy2.receive_attack(self._enemy2, 1)
                self.attack_points(self.attack_points / 1.5)
            else:
                self._enemy2.receive_attack(self._enemy2, 1)
        elif(self._enemy1._alive == True and self._enemy2._alive == True):
            if(type(self._enemy1) == Dwarves):
                self.attack_points(self.attack_points * 1.5)
                self._enemy1.receive_attack(self._enemy1, 0.4)
                self.attack_points(self.attack_points / 1.5)

                self._enemy2.receive_attack(self._enemy2, 0.6)
            elif(type(self._enemy2) == Dwarves):
                self._enemy1.receive_attack(self._enemy1, 0.6)

                self.attack_points(self.attack_points * 1.5)
                self._enemy2.receive_attack(self._enemy2, 0.4)
                self.attack_points(self.attack_points / 1.5)

    def receive_attack(self, attacker: faction, unit_percentage):

        damage_coefficient = 1

        if(type(attacker) == Orcs):
            damage_coefficient = 1.25
        elif(type(attacker) == Dwarves):
            damage_coefficient = 0.75
        
        self.units(self.units - int(((unit_percentage * attacker._units) * attacker._attack_points * damage_coefficient) / attacker._health_points))

    def purchase_weapons(self, weapon_points):

        self.attack_points(self.health_points + (2 * weapon_points))
        gold = 15 * weapon_points

        return gold

    def purchase_armors(self, armor_points):

        self.health_points(self.health_points + (4 * armor_points))
        gold = 5 * armor_points

        return gold
        
    def print(self):
        print('\n"You cannot reach our elegance."\n')
        super().print()