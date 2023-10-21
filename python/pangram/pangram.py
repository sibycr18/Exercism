from string import ascii_lowercase

def is_pangram(sentence):
    alphabet_set = set(ascii_lowercase)
    sentence = set(sentence.lower())
    return alphabet_set.intersection(sentence) == alphabet_set
