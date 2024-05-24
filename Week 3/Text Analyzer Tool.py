
# Global variables to store the analysis metrices
word_count = 0                                                  # Variable to hold the word count
char_count_with_spaces = 0                                      # Variable to hold the character count with spaces
char_count_without_spaces = 0                                   # Variable to hold the character count without spaces
frequency_analysis = {}                                         # Empty dictionary to hold the frequency of characters
palindromes = []                                                # Empty list to hold the palindromes found in the text
readibility_score = 0                                           # Variable to hold the readibility score


# User to enter block of text
text = input("Enter your text: ")


# Function to perform analysis feature
def analysis():
    global word_count, char_count_with_spaces, char_count_without_spaces, frequency_analysis, palindromes, readibility_score

    # Word count
    word_count = len(text.split())
    print("Word Count: ", word_count)

    # Character count                                           
    char_count_with_spaces = len(text)
    print("Character Count With Spaces: ", char_count_with_spaces)

    char_count_without_spaces = len(text.replace(" ", ""))
    print("Character Count Without Spaces: ", char_count_without_spaces)

    # Palindrome check
    words = text.split()                                        # Split the input text into a list of words
    for word in words:                                          # Check if the current word is equal to its reverse
        if word == word[::-1]:
            palindromes.append(word)                            # If it is, add the word to the global list of palindromes
    
    # Display palindromes, if any
    if palindromes:                                             
        print("Palindromes: ", palindromes)
    else:
        print("Palindromes: No Palindrome Found!")
analysis()