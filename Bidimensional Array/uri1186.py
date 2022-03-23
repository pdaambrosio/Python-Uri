character = input().upper()
matrix = [[] for _ in range(12)]

sum_diagonal = 0
next_column = 0
count_for_average = 0

for line in range(12):
    for column in range(12):
        value = float(input())
        matrix[line].append(value)

for line in reversed(range(12)):
    next_column += 1
    for column in range(next_column, 12):
        sum_diagonal += matrix[line][column]
        count_for_average += 1

average = sum_diagonal / count_for_average

print(round(sum_diagonal, 1) if character == 'S' else round(average, 1))
