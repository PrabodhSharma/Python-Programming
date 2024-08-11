
# Task 1: Locate Items in List/Tuples with the in Operator

# List of favorite fruits and a tuple of favorite vegetables
favorite_fruits = ['apple', 'banana', 'mango', 'strawberry']
favorite_vegetables = ('carrot', 'broccoli', 'spinach', 'tomato')

def check_item_in_list(item, lst):
    """Check if a given item is in the list."""
    return item in lst

def check_item_in_tuple(item, tup):
    """Check if a given item is in the tuple."""
    return item in tup

# Demonstration of the use of the above functions
print("Task 1:")
print(f"Is 'apple' in favorite fruits? {check_item_in_list('apple', favorite_fruits)}")
print(f"Is 'potato' in favorite vegetables? {check_item_in_tuple('potato', favorite_vegetables)}")



# Task 2: Use Slicing to Extract a Subset of List/Tuple/String

# List of favorite movies and a string with a sentence about favorite hobby.
favorite_movies = ['Inception', 'The Matrix', 'Interstellar', 'The Godfather', 'Pulp Fiction']
hobby_sentence = "I enjoy playing guitar and composing music in my free time."

def slice_list(lst):
    """Extract the first three items from the list."""
    return lst[:3]

def slice_string(s):
    """Extract the first ten characters from the string."""
    return s[:10]

# Demonstration of the use of the above functions
print("\nTask 2:")
print(f"First three favorite movies: {slice_list(favorite_movies)}")
print(f"First ten characters of hobby sentence: {slice_string(hobby_sentence)}")



# Task 3: Use List Methods and Built-in Functions

numbers = [5, 2, 8, 1, 9, 3, 7]

def process_numbers(lst, num_to_add, num_to_remove):
    """Process the list of numbers with various operations."""
    lst.append(num_to_add)                                          # Append a new number
    if num_to_remove in lst:
        lst.remove(num_to_remove)                                   # Remove a specified number
    lst.sort()                                                      # Sort the list in ascending order
    lst.reverse()                                                   # Reverse the list
    return lst

# Demonstration of the use of the above function
print("\nTask 3:")
print(f"Original numbers: {numbers}")
processed_numbers = process_numbers(numbers.copy(), 6, 2)
print(f"Processed numbers: {processed_numbers}")



# Task 4: In-Class Activity as Homework

favorite_books = ['To Kill a Mockingbird', '1984', 'Pride and Prejudice', 
                  'The Great Gatsby', 'The Catcher in the Rye']

def process_books(books):
    """Process the list of books with various operations."""
    # Slice the list to get the middle three books
    middle_three = books[1:4]
    
    # Add two new books to the list
    books.append("The Hobbit")
    books.append("Harry Potter and the Sorcerer's Stone")
    
    # Remove the first book from the list
    books.pop(0)
    
    # Sort the list alphabetically
    books.sort()
    
    # Convert all book titles to uppercase using list comprehension
    uppercase_books = [book.upper() for book in books]
    
    return middle_three, books, uppercase_books

# Demonstration of the use of the above function
print("\nTask 4:")
middle_books, updated_books, uppercase_books = process_books(favorite_books.copy())
print(f"Middle three books: {middle_books}")
print(f"Updated book list: {updated_books}")
print(f"Uppercase book titles: {uppercase_books}")