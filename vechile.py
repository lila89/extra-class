class fruits:
    def __init__(self,name):
        self.name = name
        if name == "green apple":
            self.healty = True
        else:
            self.healthy = False
        self.different_taste = True
        self.from_plant = True

class apple(fruits):    
    def ishealty(self):
        return self.ishealthy

apple_name =str(input("enter the type of apple :"))
apple = apple(apple_name)
if apple.ishealthy():
    print(apple.name,"is healthy")
else:
    print(apple.name,"is not healthy")

