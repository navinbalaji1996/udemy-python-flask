class Car:

    # class variable
    a = 2

    def __init__(self, a=a):
        self.a = a

    def display(self):
        print(self.a)

    @classmethod
    def _class_method(cls):
        return cls(12)
    
    @staticmethod
    def _static_method():
        return "Hai"


car = Car(1)
car.display()

car = Car()
car.display()

car = Car._class_method()
car.display()

print(car._static_method())