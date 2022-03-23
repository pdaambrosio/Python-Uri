character = input().upper()
matrix = [[] for _ in range(12)]

sum_center = 0
next_column = 1
end_column = 11
count_for_average = 0

for line in range(12):
    for column in range(12):
        value = float(input())
        matrix[line].append(value)

for line in range(5):
    for column in range(next_column, end_column):
        sum_center += matrix[line][column]
        count_for_average += 1
    next_column += 1
    end_column -= 1

average = sum_center / count_for_average

print(round(sum_center, 1) if character == 'S' else round(average, 1))
