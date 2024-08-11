
"""
This Python script demonstrates advanced operations with lists and tuples,
covering:

- Creation and manipulation of lists
- Working with nested lists
- Creation and manipulation of tuples
- Working with nested tuples
- Employing various list and tuple methods
"""

# Task 1: Create and Manipulate Lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]


# Add 'fig' to the list's end
fruits.append("fig")


# Insert 'grape' at the second position
fruits.insert(1, "grape")


# Remove 'banana' from the list
fruits.remove("banana")


# Sort the list in alphabetical order
fruits.sort()


# Reverse the order of the list elements
fruits.reverse()


# Obtain the first three fruits using slicing
first_three_fruits = fruits[:3]


# Obtain the last three fruits using slicing
last_three_fruits = fruits[-3:]


# Check for 'cherry's presence in the list
is_cherry_in_list = "cherry" in fruits


# Get the length of the list
list_length = len(fruits)


# Unpack the first three fruits
first_fruit, second_fruit, third_fruit = fruits[:3]

print("\nTask 1 Results:")
print(f"Fruits list: {fruits}")
print(f"First three fruits: {first_fruit}, {second_fruit}, {third_fruit}")
print(f"List length: {list_length}")
print(f"Is 'cherry' in the list? {is_cherry_in_list}")




# Task 2: Work with Nested Lists
nested_fruits = [
    ["apple", "banana"],
    ["cherry", "date"],
    ["elderberry", "fig"]
]


# Access the second fruit in the first sublist
second_fruit_first_sublist = nested_fruits[0][1]


# Access the first fruit in the third sublist
first_fruit_third_sublist = nested_fruits[2][0]


# Add 'grape' to the second sublist
nested_fruits[1].append("grape")


# Remove 'date' from the second sublist
nested_fruits[1].remove("date")


# Print the entire nested list
print("\nTask 2 Results:")
print(f"Nested fruits list: {nested_fruits}")




# Task 3: Create and Manipulate Tuples
vegetables = ("carrot", "broccoli", "asparagus", "cauliflower", "corn")


# Access the third vegetable in the tuple
third_vegetable = vegetables[2]


# Get the first three vegetables using slicing
first_three_vegetables = vegetables[:3]


# Check if 'broccoli' is in the tuple
is_broccoli_in_tuple = "broccoli" in vegetables


# Find the length of the tuple
tuple_length = len(vegetables)


# Unpack the first three vegetables
first_vegetable, second_vegetable, third_vegetable = vegetables[:3]

print("\nTask 3 Results:")
print(f"Vegetables tuple: {vegetables}")
print(f"First three vegetables: {first_vegetable}, {second_vegetable}, {third_vegetable}")
print(f"Length of the tuple: {tuple_length}")
print(f"Is 'broccoli' in the tuple? {is_broccoli_in_tuple}")




# Task 4: Work with Nested Tuples
nested_vegetables = (
    ("carrot", "broccoli"),
    ("asparagus", "cauliflower"),
    ("corn", "pea")
)


# Access the first vegetable in the second sub-tuple
first_vegetable_second_subtuple = nested_vegetables[1][0]


# Access the second vegetable in the third sub-tuple
second_vegetable_third_subtuple = nested_vegetables[2][1]


# Print the entire nested tuple
print("\nTask 4 Results:")
print(f"Nested vegetables tuple: {nested_vegetables}")




# Task 5: Lists and Tuples Methods
print("\nTask 5: List and Tuple Methods")

# List methods used in this script:
# - append(): Adds an element to the list's end (Task 1).
# - insert(): Inserts an element at a specific list position (Task 1).
# - remove(): Removes the first item from the list with a specified value (Task 1).

# Additional list methods:
# - count(): Returns the number of occurrences of a specific element (shown below).
# - index(): Returns the index of the first occurrence of a specified element (shoen below).


fruits_list = ["apple", "banana", "cherry", "orange", "cherry"]

# Count the occurrences of 'cherry'
num_cherries = fruits_list.count("cherry")


# Get the index of the first 'orange'
orange_index = fruits_list.index("orange")


print(f"\nList methods:")
print(f"Number of 'cherries': {num_cherries}")
print(f"Index of the first 'orange': {orange_index}")


# Note: Tuples are immutable, so methods like append, insert, and remove
# are not applicable to them.

# Tuple methods used in this script:
# - in(): Checks if a specified element exists in the tuple (Task 3).
# - len(): Returns the length of the tuple (Task 3).
# - + (concatenation): Creates a new tuple by concatenating existing tuples (shown below).

vegetables_tuple = ("carrot", "broccoli", "asparagus")
another_vegetable_tuple = ("cauliflower", "corn")


# Concatenate the two tuples
all_vegetables = vegetables_tuple + another_vegetable_tuple

print(f"\nTuple methods:")
print(f"Combined vegetables tuple: {all_vegetables}")
