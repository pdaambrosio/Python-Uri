character = input().upper()
matrix = [[] for _ in range(12)]

sum_left = 0
next_column = 0
count_for_average = 0

for line in range(12):
    for column in range(12):
        value = float(input())
        matrix[line].append(value)

for line in range(11):
    for column in range(0, next_column):
        sum_left += matrix[line][column]
        count_for_average += 1

    if line < 5:
        next_column += 1

    if line > 5:
        next_column -= 1

average = sum_left / count_for_average

print(round(sum_left, 1) if character == 'S' else round(average, 1))
