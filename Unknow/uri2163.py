n: int
m: int
n, m = map(int, input().split())

def force_awakens(lines, columns):
    terrain: list[list[int]] = []
    
    for line in range(lines):
        terrain.append([int(x) for x in input().split()])

    for line, column in enumerate(terrain):
        if 42 in column:
            if column.index(42) + 1 == 7:
                return '0 0'
            else:
                return f'{line + 1} {column.index(42) + 1}'

print(force_awakens(n, m))

# TODO: Test the function with other values and create the main function for execution