class hero:  # object
    # class variable
    jumlah = 0
    def __init__(self, inputname,inputhealth,inputpower,inputarmor):
        # instance variables
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        hero.jumlah += 1
        print("membuat hero dengan nama "+ inputname)


hero1 = hero("sniper",100,200,4)
print(hero.jumlah)
hero2 = hero("mirana",100,200,4)
print(hero.jumlah)
hero3 = hero("ucup",100,200,4)
print(hero.jumlah)
