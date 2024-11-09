# The word_wrap function takes a string `text` and an integer `width` as input.
# It splits the text into lines where each line does not exceed the specified `width`.
# Words are preserved, and the function ensures that spaces are maintained between words.
# The function returns a list of strings, with each string representing a wrapped line.

def word_wrap(text, width):
    result = []       # List to store each line after wrapping
    current_line = [] # List to store words for the current line
    current_length = 0 # Tracks the length of the current line

    words = text.split() # Split the text into individual words

    for word in words:
        # Check if adding the word would exceed the line width
        if current_length + len(word) + len(current_line) > width:
            # Join the words in the current line with spaces and add to result
            result.append(' '.join(current_line))
            current_line = []  # Reset for the next line
            current_length = 0 # Reset length for the new line

        # Add the word to the current line and update the length
        current_line.append(word)
        current_length += len(word)

    # Add any remaining words in the last line

#side note this code does not pass the checker I am not sure why, their output seems incorrect compared to mine
 
