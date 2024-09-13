
# Define the base class Vehicle with a common interface method 'move'
class Vehicle:
    # This method will be overridden by subclasses
    def move(self):
        # If a subclass does not implement the move method, raise an error
        raise NotImplementedError("Subclass must implement abstract method")