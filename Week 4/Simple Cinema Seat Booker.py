
# Initialize the seating arrangement
seats = [[False] * 5 for _ in range(3)]                                     # initializes a nested list called seats. [[False] * 5 for _ in range(3)] creates a list with 3 sub-lists (representing rows). Each sub-list contains 5 False values (representing seats). 'False' indicates that the seat is not booked. 

# Welcome message
print("Welcome to the Simple Cinema Seat Booker!")

# Displaying options
print("\nAvailable Options:")
print("view - View seating arrangement")
print("book - Book a seat")
print("summary - View booking summary")
print("cancel - Cancel a booking")
print("help - Display this help message")
print("exit - Exit the booking system\n")

# Start the booking process
while (True):
    user_input = input("Enter your option (type 'help' for available options): ").lower()

    if user_input == 'exit':
        break

    # View seating arrangement
    elif user_input == 'view':
        for row_index, row in enumerate(seats):
            row_display = ' '.join(['Booked' if seat else 'Available' for seat in row])
            print(f"Row {row_index + 1}: {row_display}")
    
    # Book a seat
    elif user_input == 'book':
        try:
            row = int(input("Select row number (1-3): ")) - 1
            seat = int(input("Select seat number (1-5): ")) - 1
            
            # Validate the selected row and seat
            if row < 0 or row >= 3 or seat < 0 or seat >= 5:                                 
                print("Invalid row or seat number. Please try again.")
                continue

            # Check if the seat is available, if it is book the seat
            if not seats[row][seat]:
                seats[row][seat] = True
                print("Seat booked successfully.")
            else:
                print("This seat is already booked, please select another seat.")
        except ValueError:
            print("Invalid input. Please enter numerical values for row and seat numbers.")