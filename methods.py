class hero:
    # class variable
    jumlah_hero = 0
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        # instance variables
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        hero.jumlah_hero += 1
    # void function atau methods tanpa return
    def siapa(self):
        print('namaku adalah ' + self.name)
    # method dengan argumen
    def healthup(self,up):
        self.health += up
    # method dengan return
    def gethealth(self):
        return self.health

hero1 = hero("sniper",100,200,4)
hero2 = hero("mirana",100,200,4)
hero3 = hero("ucup",100,200,4)
hero4 = hero("mario",100,200,4)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)

hero1.siapa()
hero1.healthup(10)

print(hero1.health)
print(hero1.gethealth())
