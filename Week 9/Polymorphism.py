
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


# Function to demonstrate polymorphism, accepting any Vehicle subclass object
def operate_vehicle(vehicle):
    # This will call the move method of the passed vehicle object
    vehicle.move()

# Usage of polymorphism: create a list of various vehicle objects
# vehicles list holds instances of Car, Bicycle, and Boat
vehicles = [Car(), Bicycle(), Boat()]

# Iterate through the vehicles list and operate each vehicle
for vehicle in vehicles:
    # Call the operate_vehicle function with each vehicle instance
    operate_vehicle(vehicle)