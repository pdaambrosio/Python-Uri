data = 0
ages = []

while data >= 0:
    data = int(input())
    ages.append(data)

ages = list(filter(lambda n: n >= 0, ages))
average = sum(ages) / len(ages)

print(f'{average:.2f}')
