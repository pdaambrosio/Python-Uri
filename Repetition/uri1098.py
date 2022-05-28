value_i: int|float = 0
value_j: int|float = 1

while value_i <= 2:
    for _ in range(3):
        if value_i > 2.19:
            print('I={:.0f} J={:.0f}'.format(2, value_j))
        elif value_i == 1.0 or value_i == 0.0 or value_i > 1.8:
            print('I={:.0f} J={:.0f}'.format(value_i, value_j))
        else:
            print('I={:.1f} J={:.1f}'.format(value_i, value_j))
        value_j += 1
    value_i += 0.2
    value_j = value_i + 1
