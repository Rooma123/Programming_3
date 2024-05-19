#Structural Design Pattern

#Facade Pattern
#Description: The Facade pattern provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use, hiding its complexities. It's like a simplified interface to a complex system.
#the code
class Amplifier:
    def on(self):
        print("Amplifier is turned on")
    def off(self):
        print("Amplifier is turned off")

class DVDPlayer:
    def on(self):
        print("DVDPlayer is turned on")
    def off(self):
        print("DVDPlayer is turned off")
    def play(self,movie):
        print("playing movie",movie)
    def stop(self):
        print("movie stopped")

class TV:
    def on(self):
        print("TV is turned on")
    def off(self):
        print("TV is turned off")

class HomeTheaterFacade:
    def __init__(self) :
        self.amplifier=Amplifier()
        self.dvdplayer=DVDPlayer()
        self.tv=TV()

    def watch_movie(self,movie):
        self.amplifier.on()
        self.dvdplayer.on()
        self.tv.on()
        self.dvdplayer.play(movie)

    def stop_movie(self):
        self.amplifier.off()
        self.dvdplayer.off()
        self.tv.off()
        self.dvdplayer.stop()

    def main(self):
        self.watch_movie("doctor slump")
        self.stop_movie()

if __name__ == "__main__":
    homeTheaterFacade = HomeTheaterFacade()
    homeTheaterFacade.main()


#Flyweight Pattern
#Description: The Flyweight pattern is used to minimize memory usage and improve performance by sharing as much data as possible with similar objects. It's particularly useful when you need to create a large number of similar objects, as it reduces the memory footprint by sharing common parts between objects.
class Color:
    def __init__(self,name):
        self.name=name

class ColorFactory:
    colors={}
    def get_color (name):
        if name not in ColorFactory.colors:
            ColorFactory.colors[name]=Color(name)

if __name__ == "__main__":
    color_data=("red","green","red")
    color_family_objects=[]
    for i in color_data :
        color_family_objects.append(i)
    for i in color_family_objects:
        print("id="+str(id(i)))


###################################################################################################
#Behavioral Design pattern

#Memento Pattern
#Description: The Memento pattern captures and externalizes an object's internal state without violating encapsulation, so that the object can be restored to this state later. It's useful for implementing undo mechanisms or for providing checkpoints in applications.

class TextEditor:
    def __init__(self,content) :
        self.content=content

    def get_content(self):
        return self.content
    def set_content(self,content):
        self.content=content
    def save(self):
        return Memento(self.content)
    def restore(self, memento):
        self.content = memento.get_content()
    def __str__(self):
        return self.content
   

class Memento:
    def __init__(self,content):
        self.content=content
    def get_content(self):
        return self.content
    
if __name__ == "__main__":
    texteditor=TextEditor("initial text")
    saved_state=texteditor.save()
    texteditor.set_content("another text")
    texteditor.restore(saved_state)
    print(texteditor)

################################################################################################
#Creational Design Pattern

#Factory Pattern
#Description: The Factory pattern is used to create objects without specifying the exact class of object that will be created. It defines an interface for creating objects, but allows subclasses to alter the type of objects that will be created. This pattern promotes loose coupling by abstracting the object creation process.

class Vehicle:
    def move(self):
        pass
class Car (Vehicle):
    def move(self):
        print("car is driving") 

class Bicycle (Vehicle):
    def move(self):
        print("Bicycle is cycle") 

class Motocycle (Vehicle):
    def move(self):
        print("Motocycle is riding") 

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bicycle":
            return Bicycle()
        elif vehicle_type == "Motocycle":
            return Motocycle()
        else:
            print("invalid vehicle")

factory=VehicleFactory()
car=factory.create_vehicle("car")
print(car.move())


#Builder Pattern
#Description: The Builder pattern is used to construct complex objects step by step. It separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It's particularly useful when you need to create objects with many optional parameters or configurations.

class House:
    def __init__(self,floors,bedrooms,bathrooms) :
        self.floors=floors
        self.bedrooms=bedrooms
        self.bathrooms=bathrooms

    def __str__(self) -> str:
        return f"House:{self.floors } floors,{self.bedrooms } bedrooms,{self.bathrooms } bathrooms"

class Builder:
    def __init__(self) -> None:
        self.house=None

    def set_floors(self,floors):
        self.house=House(floors,None,None)
    def set_bedrooms(self,bedrooms):
        if self.house:
            self.house.bedrooms=bedrooms

    def set_bathrooms(self,bathrooms):
        if self.house:
            self.house.bathrooms=bathrooms

    def get_house(self):
        return self.house
    
builder=Builder()
builder.set_floors(3)
builder.set_bedrooms(5)
builder.set_bathrooms(3)
house=builder.get_house()
print(house)




#Singleton Pattern
#Description: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It's commonly used for logging, database connections, caches, and thread pools, where only one instance should exist to control access and resource usage.

class Logger:
    instance=None
    def __init__(self) -> None:
        pass
    def get_instance():
        if Logger .instance is None:
            Logger.instance=Logger()
        return Logger.instance
    
    def log(self,message):
        print(message)

logger1=Logger.get_instance()
logger2=Logger.get_instance()

print(logger1 is logger2)
logger1.log("kkkkkkkkkkkk")





##########################################################################################################

    