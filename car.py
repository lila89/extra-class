class Car():
    def __init__(self,modelname,year,price):
        self.modelname = modelname
        self.year = year
        self.price = price
honda = Car('city',2017,10000000)
tata = Car('bolt', 33333,198888)
#honda.modelname ='city'
#honda.year= 2018
#honda.price = 1110000000

print(honda.__dict__)
print(tata.__dict__)