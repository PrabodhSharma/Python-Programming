
# Global variables to store the analysis metrices
word_count = 0                                                  # Variable to hold the word count
char_count_with_spaces = 0                                      # Variable to hold the character count with spaces
char_count_without_spaces = 0                                   # Variable to hold the character count without spaces
frequency_analysis = {}                                         # Empty dictionary to hold the frequency of characters
palindromes = []                                                # Empty list to hold the palindromes found in the text
readability_score = 0                                           # Variable to hold the readibility score


# User to enter block of text
text = input("Enter your text: ")


# Function to perform analysis feature
def analyze():
    global word_count, char_count_with_spaces, char_count_without_spaces, frequency_analysis, palindromes, readability_score

    # WORD COUNT
    word_count = len(text.split())
    print("Word Count: ", word_count)


    # CHARACTER COUNT                                           
    char_count_with_spaces = len(text)
    print("Character Count With Spaces: ", char_count_with_spaces)

    char_count_without_spaces = len(text.replace(" ", ""))
    print("Character Count Without Spaces: ", char_count_without_spaces)


    # PALINDROME CHECK
    words = text.split()                                        # Split the input text into a list of words
    for word in words:                                          # Check if the current word is equal to its reverse
        if word == word[::-1]:
            palindromes.append(word)                            # If it is, add the word to the global list of palindromes
    
    # Display palindromes, if any
    if palindromes:                                             
        print("Palindromes: ", palindromes)
    else:
        print("Palindromes: No Palindrome Found!")


    # FREQUENCY ANALYSIS
    for char in text:
        # frequency_analysis.get(char, 0): This retrieves the current count of the character 'char' from the dictionary. If the character is not found in the dictionary, it returns 0.
        # If the character is already in the dictionary, increment its count by 1, if not set it counts to 1
        frequency_analysis[char] = frequency_analysis.get(char, 0) + 1

    # Display frequency analysis                  
    if frequency_analysis:
        print("Frequency Analysis: ", frequency_analysis)
    else:
        print("Frequency Analysis: 0")


    # READABILITY SCORE
    total_word_lenght = 0
    for word in text.split():
        total_word_lenght += len(word)                          # Adds the length of the current word to the total word length
    
    if word_count != 0:                                         # Checks if the word count is not zero to avoid division by zero
        readability_score = total_word_lenght / word_count
    else:
        readability_score = 0

    print(f"Readability Score: {readability_score: .2f}")       # Displays readability score with two decimal places

analyze()