
# Predefined list of daily temperatures.
temperatures = [22, 20, 19, 23, 24, 25, 21, 18, 19, 22, 20, 21, 23, 17, 16, 18, 19, 21, 24, 26, 25, 22, 21, 20, 19, 18, 17, 15, 14, 13]



# Function to calculate the average temperature. This function takes a list of temperatures and returns the average temperature. 
def calculate_average(temp_list):                                           

    # Check if the input is a list
    if not isinstance(temp_list, list):
        raise TypeError("Input should be a list of temperatures.")
    
    # Checks for an empty list and handles it by raising a ValueError.                                                                
    if not temp_list:                                                       
        raise ValueError("Temperature list is empty.")
    
    # Calculate sum of temperatures.
    total = sum(temp_list) 

    # Calculate the no. of temperature.
    count = len(temp_list) 
                                                   
    # Calculate the average temperature.
    average = total / count                                       
    return average



# Function to find the maximum temperature. This function takes a list of temperatures and returns the highest temperature.
def maximum_temperature(temp_list):

    # Checks for an empty list and handles it by raising a ValueError. 
    if not temp_list:
        raise ValueError("Temperature list is empty.")
    
    # Find the maximum temperature. Uses Python's built-in "max" function to find the highest temperature.
    maximum_temperature = max(temp_list)            
    return maximum_temperature



# Function to find the minimum temperature. This function takes a list of temperatures and returns the lowest temperature.
def minimum_temperature(temp_list):

    # Checks for an empty list and handles it by raising a ValueError. 
    if not temp_list:
        raise ValueError("Temperature list is empty.")
    
    # Find the minimum temperature. Uses Python's built-in "min" function to find the lowest temperature.
    minimum_temperature = min(temp_list)
    return minimum_temperature



# Function to count the frequency of temperature. It iterates through the list, counts the occurrence of each temperature, and finally stores these counts in a dictionary.
def count_frequency(temp_list):

    # Checks for an empty list and handles it by raising a ValueError. 
    if not temp_list:
        raise ValueError("Temperature list is empty.")
    
    # Empty dicitionary to store frequency counts.
    frequency = {}

    # Loop through each temperature in the list.
    for temp in temp_list:
        # If any element is not an int or float, a TypeError is raised with a descriptive error message.
        if not isinstance(temp, (int, float)):
            raise TypeError("All elements in the temperature list should be integers or floats.")
        
        if temp in frequency:
            frequency[temp] += 1                # If temperature is already in the dictionary, increment its count.
        else:
            frequency[temp] = 1                 # If the temperature is not in the dictionary, add it with a count of 1
    return frequency
    


# Main code execution. Displaying the result
try:
    average_temp = calculate_average(temperatures)
    print(f"Average Temperature is: {average_temp:.1f}°C")

    max_temp = maximum_temperature(temperatures)
    print(f"Maximum Temperature is: {max_temp}°C")

    min_temp = minimum_temperature(temperatures)
    print(f"Minimum Temperature is: {min_temp:.1f}°C")

    temp_frequency = count_frequency(temperatures)
    print(f"Temperature Frequency is:", temp_frequency)

# Handle ValueError exceptions
except ValueError as e:
    print(e)

# Handle TypeError exceptions
except TypeError as e:
    print(e)