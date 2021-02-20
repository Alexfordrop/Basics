class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse, Donkey):
    pass   
mule = Mule()
mule.isHorse
mule.isDonkey

print(mule.isDonkey, mule.isHorse)