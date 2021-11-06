character = input().upper()
matrix = [[] for num in range(12)]

sum_diagonal = 0
next_column = 11
count_for_average = 0

for line in range(12):
    for column in range(12):
        value = float(input())
        matrix[line].append(value)

for line in range(11):
    for column in range(next_column):
        sum_diagonal += matrix[line][column]
        count_for_average += 1
    next_column -= 1

average = sum_diagonal / count_for_average

print(round(sum_diagonal, 1) if character == 'S' else round(average, 1))
