
# 1. Void function to display a menu.
def display_menu():

    """
    This function displays the menu options to the user.
    """

    print("Menu:")
    print("1. Calculate the area of rectangle")
    print("2. Check if a number is prime")
    print("3. Exit")


# 2. Value-returning function to calculate the area of rectangle.
def calculate_area(length, width):

    """
    This function calculates the area of rectangle.
    :parameter length: Length of rectangle
    :parameter width: Width of rectangle
    :return: Area of rectangle
    """

    return length * width


# 3. A function that calls another function to determine if a number is prime.
def is_prime(number):

    """
    This function checks if a number is prime.
    :parameter: The number to check
    :return: True if the number is prime, False otherwise
    """

    if number <= 1:                                             # If number is 1 or less, it's not prime.
        return False
    for i in range(2, int(number**0.5) +1):    

        """
        This loop starts with "i = 2" and goes up to the square root of the number.
        number**0.5: calculates the square root of number.
        int(number**0.5): converts the square root to an integer (floor value).
        Adding 1 ensures the loop includes the integer value of the square root itself.
        """
        
        if number % i == 0:                                     # If number is divisible by any i, it's not prime.
            return False
    return True                                                 # If no divisors found, the number is prime.

def check_prime(number):

    """
    This function calls "is_prime" to check if the number is prime.
    :parameter number: The number to check
    :return: A message indicating if the number is prime or not
    """

    if is_prime(number):                                       # Call is_prime to check if number is prime.
        return f"{number} is a prime number."                  # Return message if the number is prime.
    else:
        return f"{number} is not a prime number."              # Return message if the number is not prime.
    

# Main program structure
def main():

    """
    This allows the user to choose an option, perform the task, and display the results.
    """

    while True:                                                # Loop to keep the program running until user decides to exit.
        display_menu()                                         # Display the menu options to the user.
        option = input("Enter your option (1-3): ")            # Get user input/choice.

        # If user chooses option 1
        if option == "1":                                      
            
            # Handle area calculation.
            try:
                # Get the length and width of the rectangle of the user.
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))

                # Calculate the area using "calculate_area" function.
                area = calculate_area(length, width)

                # Print the calculated area.
                print(f"Area of rectangle is: {area:.2f}")

            # Handle invalid inputs for length and width.
            except ValueError:
                print("Invalid input. Please enter numeric values for length and width")

        
        # If user chooses option 2
        elif option == "2":                                    

            # Handle prime number check
            try:
                # Get the number to check from the user.
                number = int(input("Enter a number to check if it is a prime: "))

                # Check if the number is prime using "check_prime" funciton
                result = check_prime(number)

                # Print the result
                print(result)

            # Handle invalid inputs for number.
            except ValueError:
                print("Invalid input. Please enter the integer value.")


        # If user chooses option 3
        elif option == "3":                                   

            # Exit the program
            print("Exiting the program...")
            break                                             # Break the loop to exit.


        # If user enters an invalid option/choice.
        else:

            # Handle invalid menu option
            print("Invalid option. Please choose the correct option from 1 to 3.")

if __name__ == "__main__":                                   # It is used to check if a script is being run directly or being imported. If the script is run directly, value of __name__ is set to "__main__" and the code block under this condition is executed.
    main()                                                   # Call the main function to start the program.
