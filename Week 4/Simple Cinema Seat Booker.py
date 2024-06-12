
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
    user_input = input("Enter your option or (type 'help' for available options): ").lower()

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

            # Check if the seat is available, if it is, book the seat
            if not seats[row][seat]:
                seats[row][seat] = True
                print("Seat booked successfully.")
            else:
                print("This seat is already booked, please select another seat.")
        except ValueError:
            print("Invalid input. Please enter numerical values for row and seat numbers.")

    # Booking summary
    elif user_input == 'summary':
        booked_count = sum(row.count(True) for row in seats)                        # For each row in the seats list, this counts the number of True values (i.e booked seats) in that row.
        available_count = sum(row.count(False) for row in seats)                    # For each row in the seats list, this counts the number of False values (i.e available seats) in that row.
        print("\nBooking Summary:")
        print(f"Total Booked Seats: {booked_count}")
        print(f"Total Available Seats: {available_count}\n")

    # Cancel booking
    elif user_input == 'cancel':
        try:
            row = int(input("Select row number (1-3) to cancel: ")) - 1
            seat = int(input("Select seat number (1-5) to cancel: ")) - 1

            # Validate the selected row and seat
            if row < 0 or row >= 3 or seat < 0 or seat >= 5:
                print("Invalid row or seat number. Please try again.")
                continue

            # Check if the seat is booked, if it is, cancel it
            if seats[row][seat]:
                seats[row][seat] = False
                print("Booking cancelled successfully.")
            else:
                print("This seat is not booked, cannot cancel.")
        except ValueError:
            print("Invalid input. Please enter numerical values for row and seat numbers.")

    # Help message
    elif user_input == 'help':
        print("\nAvailable Options:")
        print("view - View seating arrangement")
        print("book - Book a seat")
        print("summary - View booking summary")
        print("cancel - Cancel a booking")
        print("help - Display this help message")
        print("exit - Exit the booking system\n")

    else:
        print("Invalid input. Please choose one of available options from above")