class SecureBankAccount:
    # Initialization of the bank account with an owner's name and an starting balance
    def __init__(self, owner, starting_balance=0):
        self.owner = owner  # Set the owner's name (public attribute)
        self.__balance = starting_balance  # Set the account balance (private attribute)

    # Method to deposit money into the account
    def deposit(self, amount):
        # Check if the deposit amount is positive
        if amount > 0:
            self.__balance += amount  # Increase the balance by the deposit amount
            print(f"Deposited ${amount:.2f} successfully.")  # Print success message
        else:
            print("Deposit amount must be positive.")  # Print error message if amount is not positive

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the withdrawal amount is positive
        if amount > 0:
            # Check if there are sufficient funds in the account
            if amount <= self.__balance:
                self.__balance -= amount  # Decrease the balance by the withdrawal amount
                print(f"Withdrew ${amount:.2f} successfully.")  # Print success message
            else:
                print("Insufficient funds.")  # Print error message if funds are insufficient
        else:
            print("Withdrawal amount must be positive.")  # Print error message if amount is not positive

    # Method to safely access the current balance
    def get_balance(self):
        return self.__balance  # Return the current balance (read-only)


# Main function to interact with the SecureBankAccount
def main():
    # Get the owner's name from the user
    owner = input("Enter the owner's name: ")

    # Loop until the user provides a valid non-negative starting balance
    while True:
        # Get the starting balance from the user
        starting_balance_input = input("Enter the starting balance (default to $0.00 if not provided): ")

        # Check if the user provided a value or left it blank
        if starting_balance_input == "":
            print("No input provided. Setting balance to $0.00.")
            starting_balance = 0.00  # Set balance to zero if no input is provided
            break  # Exit the loop since a valid balance has been set

        try:
            # Attempt to convert the input to a float
            starting_balance = float(starting_balance_input)

            # Check if the starting balance is non-negative
            if starting_balance >= 0:
                break  # Exit the loop since a valid balance has been set
            else:
                # Inform the user that negative values are not allowed
                print("Starting balance cannot be negative. Please enter a non-negative value.")

        except ValueError:
            # Inform the user that the input was invalid
            print("Invalid input. Please enter a valid number.")

    # Create a new SecureBankAccount object with the provided owner and starting balance
    account = SecureBankAccount(owner, starting_balance)

    # Start an infinite loop for user interaction until the user chooses to exit
    while True:
        # Display options to the user
        print("\nChoose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == "1":
            # Attempt to get the deposit amount from the user
            try:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)  # Call the deposit method
            except ValueError:
                print("Invalid amount. Please enter a valid number.")  # Print error for invalid input

        elif choice == "2":
            # Attempt to get the withdrawal amount from the user
            try:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)  # Call the withdraw method
            except ValueError:
                print("Invalid amount. Please enter a valid number.")  # Print error for invalid input

        elif choice == "3":
            # Display the current balance
            print(f"Current balance: ${account.get_balance():.2f}")

        elif choice == "4":
            # Exit the loop and end the program
            print("Exiting...")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select a valid option.")


# Main function to start the program
if __name__ == "__main__":
    main()  # Execute the main function when the script is run
