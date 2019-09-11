### Three tools for understanding strange objects

- **type()** (what is this thing?)


- **dir()** (what can  i do with this?)


- **help()** (tell me more!)


```python

# blackjack_hand_greater_than

#def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

def hand_total(hand):
    """ Helper function to calculate the total points of a black hand
    """
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0 
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards(e.g. '7') to ints
            total += int(card)

    # At this point, total is the sum of this hand's card's *not counting aces*.

    # Add aces, counting them as 1 for now. this is the smallest total we can make from this hand
    total += aces
    # 'Upgrade' aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        total += 10
        #aces -= 1  测试后此句可有可无，不影响结果。
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)

```