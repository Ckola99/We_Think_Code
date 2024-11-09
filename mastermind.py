# The mastermind function compares a guess string to a secret string and returns a dictionary 
# with counts of "correct" (characters in the exact position) and "correctish" (characters in the guess that are 
# in the secret but in a different position).

def mastermind(x, y):
    guess = x       # The guessed string.
    secret = y      # The secret string to compare against.
    
    # Dictionary to keep track of "correct" (exact matches) and "correctish" (partial matches).
    dictionary = {"correct": 0, "correctish": 0}
    
    # Lists to hold unmatched characters from the guess and secret after exact matches are removed.
    unmatched_guess = []
    unmatched_secret = []
    
    # First pass: Check for characters that match exactly (same character in the same position).
    for char in range(len(guess)):
        if guess[char] == secret[char]:
            # Count exact matches (correct position and character).
            dictionary["correct"] += 1
        else:
            # Store non-matching characters for a second pass to check for "correctish" matches.
            unmatched_guess.append(guess[char])
            unmatched_secret.append(secret[char])

    # Second pass: Check for characters that exist in both strings but are in different positions.
    for char in unmatched_guess:
        if char in unmatched_secret:
            # Count characters that are present but in different positions.
            dictionary["correctish"] += 1
            # Remove the matched character from unmatched_secret to avoid double counting.
            unmatched_secret.remove(char)

    # Return the final counts of exact and partial matches.
    return dictionary
