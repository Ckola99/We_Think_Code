# The blackjack function calculates the total value of a hand in a blackjack game, 
# considering special rules for the ace card. It returns the hand's total value, adjusting for aces 
# if the hand total exceeds 21.

def blackjack(hand):
    # Dictionary mapping card names to their respective values in blackjack.
    black_jack_dictionary = {
        "king": 10, "queen": 10, "jack": 10, "2": 2, 
        "3": 3, "4": 4, "5": 5, 
        "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "ace": 11, "1": 11  # Both "ace" and "1" represent an ace with an initial value of 11.
    }

    hand_total = 0    # Variable to store the total value of the hand.
    aces_count = 0    # Counter to track the number of aces in the hand.

    # Loop through each card in the hand to calculate the total value.
    for card in hand:
        # Convert card to a lowercase string to ensure dictionary lookup works regardless of input format.
        card_str = str(card).lower()
        
        # Get the card's value from the dictionary.
        card_value = black_jack_dictionary[card_str]
        
        # Add the card's value to the running total of the hand.
        hand_total += card_value
        
        # Check if the card is an ace (which could be represented as either "ace" or "1").
        if card_str == 'ace' or card_str == "1":
            # Increment the ace counter to handle potential value adjustment later.
            aces_count += 1

    # Adjust for aces if the hand's total value exceeds 21.
    while hand_total > 21 and aces_count:
        # If total exceeds 21, treat an ace as 1 instead of 11 by subtracting 10.
        hand_total -= 10
        # Decrease the ace count to reflect the adjustment made.
        aces_count -= 1

    # Return the final total value of the hand after all adjustments.
    return hand_total

# Example usage:
# Calculating the total for a hand containing 1, 5, 2, and 4.
blackjack([1, 5, 2, 4])
