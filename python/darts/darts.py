def score(x, y):
    target_area = x ** 2 + y ** 2
    if target_area <= 1:
        return 10
    if target_area <= 5 ** 2:
        return 5
    if target_area <= 10 ** 2:
        return 1
    return 0
