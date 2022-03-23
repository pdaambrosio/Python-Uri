while True:
    try:
        n = int(input())
        matrix = [[] for _ in range(n)]

        for line, value1 in enumerate(matrix):
            for column, value2 in enumerate(matrix):
                matrix[column].append('3')

        count = n - 1

        for i in range(n):
            matrix[i][i] = '1'
            matrix[i][count] = '2'
            count -= 1

            format_print = ''.join(matrix[i])
            print(format_print)

    except EOFError:
        break
