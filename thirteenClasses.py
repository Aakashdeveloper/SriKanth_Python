class City:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def cityInfo(self):
        print(self.name + " is a part of "+ self.country)


out = City("London", "UK")
out.cityInfo()




    