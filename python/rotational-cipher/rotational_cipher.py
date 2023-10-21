def rotate(text, key):
    new_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                new_text += chr(((ord(char) + key - 65) % 26) + 65)
            else:
                new_text += chr(((ord(char) + key - 97) % 26) + 97)
        else:
            new_text += char
    return new_text
