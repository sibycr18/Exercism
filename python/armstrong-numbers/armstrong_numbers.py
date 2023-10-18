def is_armstrong_number(number):
    no_of_digits = len(str(number))
    return number == sum(int(digit) ** no_of_digits for digit in str(number))
