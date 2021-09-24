from adagrams.hand import Hand

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

hand = Hand(LETTER_POOL)

print("Welcome to Adagrams!")
print("Let's draw some letters!")
print(f"Here is the letter bank: {hand.letter_bank}")

play = True
while play:
    word = input("Give me a word: ")
    if hand.uses_available_letters(word):
        print("Great word!")
    else:
        print("Invalid Word")

    print(hand.letter_bank)

    raw_decision = input("Would you like to make another word (W), quit (Q), or draw a new hand (H)? ")

    if raw_decision == "W":
        pass
    elif raw_decision == "Q":
        play = False
    elif raw_decision == "H":
        hand = Hand(LETTER_POOL)
        print(f"Here is the letter bank: {hand.letter_bank}")