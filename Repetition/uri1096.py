value_i: int = 1
value_j: int = 7

while value_i <= 9:
    while value_j >= 5:
        print('I={} J={}'.format(value_i, value_j))
        value_j -= 1
    value_i += 2
    value_j = 7
