def matrix(n_lines: int, m_columns: int) -> list:
    matrix: list = [[] for _ in range(n_lines)]
    
    for i in range(m_columns):
        matrix[i].append(input())
    
    return matrix

print(matrix(4, 4))
