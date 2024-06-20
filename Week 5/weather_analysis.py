
# Predefined list of daily temperatures.
temperatures = [22, 20, 19, 23, 24, 25, 21, 18, 19, 22, 20, 21, 23, 17, 16, 18, 19, 21, 24, 26, 25, 22, 21, 20, 19, 18, 17, 15, 14, 13]


# Function to calculate the average temperature. This function takes a list of temperatures and returns the average temperature. 
def calculate_average(temp_list):                                           

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