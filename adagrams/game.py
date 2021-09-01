import random

def draw_letters():
    distribution = {'A': 9, 'B': 2, 'O': 8, 'C': 2, 'P': 2, 
                    'D': 4, 'Q': 1, 'E': 12, 'R': 6, 'F': 2, 
                    'S': 4, 'G': 3, 'T': 6, 'H': 2, 'U': 4, 
                    'I': 9, 'V': 2, 'J': 1, 'W': 2, 'K': 1, 
                    'X': 1, 'L': 4, 'Y': 2, 'M': 2, 'Z': 1}
    pool = []
    for ltr in distribution:
        pool.extend([ltr for i in range(distribution[ltr])])
    # Using random.sample:
    #hand = random.sample(pool, 10)
    # manual version:
    hand = []
    for i in range(10):
        rand = random.randint(0, len(pool))
        ltr = pool[rand]
        hand.append(ltr)
        pool.remove(ltr)

    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    ltr_dict = {}
    for ltr in letter_bank:
        if ltr in ltr_dict:
            ltr_dict[ltr] += 1
        else:
            ltr_dict[ltr] = 1
    for ltr in word:
        if ltr in ltr_dict and ltr_dict[ltr] > 0:
            ltr_dict[ltr] -= 1
        else:
            return False
    return True

def score_word(word):
    scores = {'A': 1, 'B': 3, 'O': 1, 'C': 3, 'P': 3, 
                'D': 2, 'Q': 10, 'E': 1, 'R': 1, 'F': 4, 
                'S': 1, 'G': 2, 'T': 1, 'H': 4, 'U': 1, 
                'I': 1, 'V': 4, 'J': 8, 'W': 4, 'K': 5, 
                'X': 8, 'L': 1, 'Y': 4, 'M': 3, 'Z': 10}
    word = word.upper()
    score = 0
    for ltr in word:
        score += scores[ltr]
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_word = word
            highest_score = score
        elif score == highest_score and len(word) > len(highest_word) and len(word) == 10:
            highest_word = word
            highest_score = score
        elif score == highest_score and len(highest_word) != 10 and len(word) < len(highest_word):
            highest_word = word
            highest_score = score
    return highest_word, highest_score