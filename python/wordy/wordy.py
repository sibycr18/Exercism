def answer(question):
    valid_operations = ["plus", "minus", "multiplied", "divided"]

    # invalid question
    if question[:7] != "What is":
        raise ValueError("unknown operation")
    
    operations_list = question[7:].rstrip('?').split()

    # removing 'by' from the operations list
    while True:
        if 'by' in operations_list:
            operations_list.remove('by')
        else:
            break

    # Exception handling
    if operations_list == []:
        raise ValueError("syntax error")
    for i in range(0, len(operations_list), 2):
        if not operations_list[i].strip('-').isnumeric():
            raise ValueError("syntax error")
    for i in range(1, len(operations_list), 2):
        if not operations_list[i].isalpha():
            raise ValueError("syntax error")
        if operations_list[i] not in valid_operations:
            raise ValueError("unknown operation")
    if len(operations_list) % 2 == 0:
        raise ValueError("syntax error")
    
    # processing operations list
    while len(operations_list) != 1:
        result = int(operations_list.pop(0))    # stores left operand before operation and the result, after calculation
        operator = operations_list.pop(0)
        right_operand = int(operations_list.pop(0))

        # calculations
        if operator == "plus":
            result += right_operand
        elif operator == "minus":
            result -= right_operand
        elif operator == "multiplied":
            result *= right_operand
        elif operator == "divided":
            result //= right_operand

        operations_list.insert(0, result) # adding result to index 1 of operations list

    return int(operations_list[0])
