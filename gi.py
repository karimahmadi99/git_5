print("hell")

class Car:
    def __init__(self, name, model, city):
        self.name = name
        self.model = model
        self.city = city

    def too(self): 
        log = self.name + " " + self.model + " " + self.city
        return log
    
