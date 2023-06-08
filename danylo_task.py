class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__
class Solution:
    def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
        while fighter1.health > 0 and fighter2.health > 0:
            if first_attacker == fighter1.name:
                fighter2.health -= fighter1.damage_per_attack
                if fighter2.health <= 0:
                    return fighter1.name
                fighter1.health -= fighter2.damage_per_attack
                if fighter1.health <= 0:
                    return fighter2.name
    #            continue
            elif first_attacker == fighter2.name:
                fighter1.health -= fighter2.damage_per_attack
                if fighter1.health <= 0:
                    return fighter2.name
                fighter2.health -= fighter1.damage_per_attack
                if fighter2.health <= 0:
                    return fighter1.name
      #          continue
       

    print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))