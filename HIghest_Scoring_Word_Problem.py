# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.

def high(x):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    points = range(1, 27)
    dict = {}
    counter = 0
    for letter in letters:
        dict[letter] = points[counter]
        counter += 1
    word_list = x.split(' ')
    print(word_list)
    highest_score = 0
    highest_scoring_string = ''
    for word in word_list:
        new_word_score = 0
        for letter in word:
            new_word_score += dict[letter]
        if new_word_score > highest_score:
            highest_score = new_word_score
            highest_scoring_string = word
    return highest_scoring_string
