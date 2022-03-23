column = int(input())
character = input()
matrix = [[] for _ in range(12)]

sum_column = 0

for lines in range(12):
    for columns in range(12):
        value = float(input())
        matrix[lines].append(value)

for i in range(12):
    sum_column += matrix[i][column]

average = sum_column / 12

print(round(sum_column, 1) if character.upper() == 'S' else round(average, 1))
