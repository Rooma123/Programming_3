#Single Responsibility Principle
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def display_users(self):
        for user in self.users:
            print(f"Username: {user.username}, Email: {user.email}")

# Usage
if __name__ == "__main__":
    user_manager = UserManager()

    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    user_manager.add_user(user1)
    user_manager.add_user(user2)

    user_manager.display_users()

    user_manager.remove_user(user1)

    print("After removing user1:")
    user_manager.display_users()

#The User class represents a user with properties like username and email. This class has a single responsibility, which is to represent a user.
#The UserMana class is responsible for managing users. It provides methods to add, remove, and display users. This class has a single responsibility, which is to manage users

############################################################################
#Open-Closed Principle (OCP) 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

# Usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    circle = Circle(3)

    calculator = AreaCalculator()
    total_area = calculator.calculate_area([rectangle, circle])

    print(f"Total area: {total_area}")

#The Shape class is an abstract base class defining a method area(). It serves as a template for different shapes.
#The Rectangle and Circle classes are concrete implementations of the Shape class. They provide their own implementations of the area() method.
#The AreaCalculator class is responsible for calculating the total area of a list of shapes. It takes a list of shapes and iterates through them, summing up their areas.
#The code adheres to the Open-Closed Principle (OCP) because:
#1)It allows for extension by creating new shapes (e.g., adding a Triangle class) without modifying existing code.
#2)The AreaCalculator class is closed for modification because it doesn't need to be changed when new shapes are added. It can work with any shape that implements the Shape interface.

#####################################################################################
#Liskov Substitution Principle (LSP)
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return f"{self.name} is flying"

class Ostrich(Bird):
    def fly(self):
        return f"{self.name} cannot fly"

# Function that expects a Bird object
def bird_activity(bird):
    return bird.fly()

# Usage
if __name__ == "__main__":
    sparrow = Sparrow("Sparrow")
    ostrich = Ostrich("Ostrich")

    print(bird_activity(sparrow))
    print(bird_activity(ostrich))

#The Bird class is an abstract base class defining a method fly(). It serves as a template for different types of birds.
#The Sparrow and Ostrich classes are concrete implementations of the Bird class. They provide their own implementations of the fly() method.
#The bird_activity() function takes a Bird object as input and calls its fly() method.
#The code adheres to the Liskov Substitution Principle (LSP) because:
#1)Objects of the derived classes (Sparrow and Ostrich) can substitute objects of the base class (Bird) without affecting the correctness of the program.
#2)Even though Ostrich cannot fly, it still provides an implementation for the fly() method.this allow to be used interchangeably with other bird objects  in contexts where flying behavior is expected

##################################################################################
#Interface Segregation Principle (ISP)
from abc import ABC, abstractmethod

# Interface for devices that can print
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

# Interface for devices that can scan
class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Interface for devices that can fax
class Fax(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

# A multifunctional printer implementing all three interfaces
class MultifunctionalPrinter(Printer, Scanner, Fax):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document")

    def send_fax(self, document):
        print(f"Sending fax: {document}")

# Usage
if __name__ == "__main__":
    printer = MultifunctionalPrinter()
    printer.print_document("Test Document")
    printer.scan_document()
    printer.send_fax("Fax Document")

#Printer, Scanner, and Fax are interfaces that define methods for printing, scanning, and faxing respectively.
#MultifunctionalPrinter implements all three interfaces. It provides concrete implementations for printing, scanning, and faxing functionalities.
#The code adheres to the Interface Segregation Principle (ISP) because:
#1)Each interface is specific to a particular functionality: printing, scanning, or faxing.
#2)Classes that implement these interfaces do not need to implement methods they don't use, avoiding unnecessary dependencies and ensuring that clients are not forced to depend on methods they do not need.

#################################################################################
#Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod

# High-level module (Policy) depending on an abstraction (Notifier)
class Policy:
    def __init__(self, notifier):
        self.notifier = notifier

    def claim_insurance(self):
        # Claim processing logic goes here
        # After processing, notify the user
        self.notifier.notify("Your insurance claim has been processed.")

# Abstraction for notifier
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Concrete implementation of notifier using email
class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Sending email notification: {message}")

# Concrete implementation of notifier using SMS
class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"Sending SMS notification: {message}")

# Usage
if __name__ == "__main__":
    email_notifier = EmailNotifier()
    policy_with_email_notification = Policy(email_notifier)
    policy_with_email_notification.claim_insurance()

    sms_notifier = SMSNotifier()
    policy_with_sms_notification = Policy(sms_notifier)
    policy_with_sms_notification.claim_insurance()

#The Policy class represents a high-level module that processes insurance claims. It depends on an abstraction (Notifier) rather than concrete implementations.
#The Notifier class is an abstraction for notifying users about claim processing.
#The EmailNotifier and SMSNotifier classes are concrete implementations of the Notifier interface, providing specific implementations for sending notifications via email and SMS respectively.
#This code adheres to the Dependency Inversion Principle (DIP) because:
#1)The Policy class depends on the abstraction (Notifier) rather than concrete implementations (EmailNotifier or SMSNotifier).
#2)Concrete implementations (EmailNotifier and SMSNotifier) depend on the same abstraction (Notifier), allowing for easy substitution of one implementation for another without modifying the Policy class.
