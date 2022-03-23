while True:
    try:
        n = int(input())
        one = n // 3
        three = n - 1

        matrix = [[] for _ in range(n)]

        for line in range(n):
            for column in range(n):
                if line == column:
                    matrix[line].append(2)
                else:
                    matrix[line].append(0)
                
                if column == three:
                    matrix[line][three] = 3
                
            three -= 1

        for line in range(one, (n - one)):
            for column in range(one, (n - one)):
                matrix[line][column] = 1

                if line == (n // 2) and column == (n // 2):
                    matrix[line][column] = 4

        for line in range(n):
            for column in range(n):
              print(matrix[line][column], end='')
            
            print()
        print()

    except EOFError:
        break
