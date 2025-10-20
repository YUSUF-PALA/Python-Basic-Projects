import random
import sys
import time

class characters:
    def __init__(self,name ,health,damage):
        self._name=name
        self.health=health
        self.damage=damage
    def attack(self,attacked: 'characters'):
        pass
        

class ally(characters):
    def __init__(self, name, health):
        
        super().__init__(name, health,0)
    def attack(self,attacked: 'characters'):
        damage=random.choice([15,25])
        if  damage==25:
            print("You dealt Critical Damage -25")
        attacked.health-=damage
class enemy(characters):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self,attacked: 'characters'):
        
        attacked.health-=self.damage
    
ally_obj=ally("Hero",100)
enemy_obj=enemy("Enemy",175,10)
 


print(f"{ally_obj._name} hits first ")
print("------------------------------")
while ally_obj.health>0 and enemy_obj.health>0:
    time.sleep(1.5)
    if ally_obj.health<=0:
        print("You Lost...")
        print(f"Enemy : {enemy_obj.health}")
        break
    ally_obj.attack(enemy_obj)
    if enemy_obj.health<=0:
        print("You killed him !")
        print(f"{ally_obj.health} HP remaining")
        break
    else:
        enemy_obj.attack(ally_obj)
    
    if enemy_obj.health<0 :
        enemy_obj.health=0
        print(f"Enemy : 0")
    else:
        print(f"Enemy : {enemy_obj.health}")
    if ally_obj.health<0:
        ally_obj.health=0
        print(f"You : 0")
    else:
        print(f"You : {ally_obj.health}")
    print("------------------------------")
    if ally_obj.health<=0 and enemy_obj.health>0:
        ally_obj.health==0
        print("You lost ...")
    elif enemy_obj.health<=0 and ally_obj.health>0:
        enemy_obj.health==0
        print("You killed him")
    elif ally_obj.health<=0 and enemy_obj.health<=0:
        print("You both died")
    


























   

