'''Technical Interview Week 9 - Coding Problem Solution'''
import random

LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

LETTERS = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
           'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
           'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
           'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
           'N', 'N', 'N', 'N', 'N', 'N',
           'R', 'R', 'R', 'R', 'R', 'R',
           'T', 'T', 'T', 'T', 'T', 'T',
           'L', 'L', 'L', 'L', 'U', 'U', 'U', 'U',
           'S', 'S', 'S', 'S', 'D', 'D', 'D', 'D',
           'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M',
           'P', 'P', 'F', 'F', 'H', 'H', 'V', 'V',
           'W', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

def get_word_points(word:str) -> int:
    '''Returns points for a given word based on scrabble scoring'''
    total_score = 0
    for letter in word.upper():
        total_score += LETTER_SCORES[letter]
    return total_score

def draw_players_rack() -> list[str]:
    '''Returns a list of seven letters'''
    players_rack = []
    for i in range(7):
        players_rack.append(random.choice(LETTERS))
    return players_rack

def read_dictionary() -> list[str]:
    '''Returns the dictionary as a list of words'''
    word_list = []
    with open('dictionary.txt','r',encoding='UTF-8') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    return word_list

def filter_dictionary(rack:list[str]) -> list[str]:
    '''Returns a filtered dictionary based on the player's rack'''
    filtered_words = []
    for word in read_dictionary():
        if all(letter.lower() in word for letter in rack):
            filtered_words.append(word)
    return filtered_words

def check_valid_words(rack:list[str],filtered_words:list[str]):
    '''Returns a list of valid words'''


if __name__ == "__main__":
    ...