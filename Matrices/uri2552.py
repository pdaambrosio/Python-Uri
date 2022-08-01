def cheese_bread_sweeper(n_lines: int, m_columns: int) -> list:
    matrix: list = []

    for _ in range(m_columns):
        matrix.append(list(map(int, input().split())))

    for line in range(n_lines):
        for column in range(m_columns):
            if matrix[line][column] == 1:
                matrix[line][column] = 9

    count: int = 0
    for line in range(n_lines):
        for column in range(m_columns):
            if matrix[line][column] != 9:
                if line > 0 and matrix[line - 1][column] == 9:
                    count += 1
                if line < n_lines - 1 and matrix[line + 1][column] == 9:
                    count += 1
                if column > 0 and matrix[line][column - 1] == 9:
                    count += 1
                if column < m_columns - 1 and matrix[line][column + 1] == 9:
                    count += 1
                matrix[line][column] = count
                count = 0
    
    return matrix


print(cheese_bread_sweeper(4, 4))
