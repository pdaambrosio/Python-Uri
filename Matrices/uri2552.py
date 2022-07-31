def cheese_bread_sweeper(n_lines: int, m_columns: int) -> list:
    matrix: list = []
    result: list = []
    # count: int = 0

    for _ in range(m_columns):
        matrix.append(list(map(int, input().split())))

    for i in range(n_lines):
        count: int = 0
        result.append([])
        for j in range(m_columns):
            if matrix[i][j] == 1:
                result[i].append(9)
            elif i > 0 and matrix[i - 1][j] == 1:
                count += 1
                result[i].append(count)
            elif i < n_lines - 1 and matrix[i + 1][j] == 1:
                count += 1
                result[i].append(count)
            elif j > 0 and matrix[i][j - 1] == 1:
                count += 1
                result[i].append(count)
            elif j < m_columns - 1 and matrix[i][j + 1] == 1:
                count += 1
                result[i].append(count)
                
    
    return result


print(cheese_bread_sweeper(4, 4))
