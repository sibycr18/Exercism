def is_valid(isbn):
    isbn = isbn.replace('-', '')
    valid_characters = set(str(num) for num in range(0,10))
    valid_characters.add('X')

    # if invalid ISBN
    if len(isbn) != 10 or len(set(isbn) - valid_characters) > 0:
        return False
    
    sum = 0
    for i in range(0, 10):
        sum += 10 if isbn[i].lower() == 'x' else int(isbn[i]) * (10 - i)
    return sum % 11 == 0
