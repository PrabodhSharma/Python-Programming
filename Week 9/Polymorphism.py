
# Define the base class Vehicle with a common interface method 'move'
class Vehicle:
    # This method will be overridden by subclasses
    def move(self):
        # If a subclass does not implement the move method, raise an error
        raise NotImplementedError("Subclass must implement abstract method")
    
# Subclass Car inheriting from Vehicle
class Car(Vehicle):
    # It provides a specific implementation of the move method for Car
    def move(self):
        # Print how a car moves
        print("The car drives on the road")

# Subclass Bicycle inheriting from Vehicle
class Bicycle(Vehicle):
    # It provides a specific implementation of the move method for Bicycle
    def move(self):
        # Print how a bicycle moves
        print("The bicycle pedals along the path")

# Subclass Boat inheriting from Vehicle
class Boat(Vehicle):
    # It provides a specific implementation of the move method for Boat
    def move(self):
        # Print how a boat moves
        print("The boat sails on the water")