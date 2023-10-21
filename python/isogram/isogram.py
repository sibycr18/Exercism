def is_isogram(string):
    string = tuple(character.lower() for character in string if character.isalpha())
    return len(set(string)) == len(string)
