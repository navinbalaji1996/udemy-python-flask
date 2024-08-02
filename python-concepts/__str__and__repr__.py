from datetime import datetime


now = datetime.now()
print(now)               # 2024-08-02 15:28:31.577029
print(str(now))          # 2024-08-02 15:28:31.577029
print(repr(now))         # datetime.datetime(2024, 8, 2, 15, 28, 31, 577029)

class Car:

    def __init__(self) -> None:
        pass

    def __str__(self):
        return "Hai"
    
    def __repr__(self):
        return "Bye"

car = Car()
print(car)            # first search __str__(), then __repr__() and finally the object
print(str(car))       # __str__() will be invoked
print(car.__str__())  # __repr__() will be invoked
print(repr(car))      # __repr__() will be invoked

# __str__() is used for user friendly
# __repr__() is used for developer friendly

# when str(car) or car.__str__() is called, if __str__() is not present, it will invoke __repr__()
# But if __repr__() is not present when repr(car) is called, then the op will be object.car....