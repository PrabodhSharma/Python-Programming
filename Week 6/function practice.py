
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
    for i in range(2, int(number**0.5) +1):                     # Iterate from 2 to the square root of the number.
        if number % i == 0:                                     # If number is divisible by any i, it's not prime.
            return False
    return True                                                 # If no divisors found, the number is prime.

def check_prime(number):

    """
    This function calls "is_prime" to check if the number is prime.
    :parameter number: The number to check
    :return: A message indicating if the number is prime or not
    """

    if is_prime(number):
        return f"{number} is a prime number."
    else:
        return f"{number} is not a prime number."