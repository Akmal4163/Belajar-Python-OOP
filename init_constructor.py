class hero:  # object
    def __init__(self, inputname,inputhealth,inputpower,inputarmor):
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor


hero1 = hero("sniper",100,200,4)
hero2 = hero("mirana",100,200,4)
hero3 = hero("ucup",100,200,4)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
