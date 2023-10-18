def response(hey_bob):
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.isspace() or hey_bob == '':
        return "Fine. Be that way!"
    if hey_bob.rstrip()[-1] == '?':
        return "Sure."
    return "Whatever."
