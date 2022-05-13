def city_analogimon(rows: int, columns: int) -> list:
    """
    Function that returns a list with describing the city Analógimôn
    """
    matrix: list = []
    for _ in range(rows):
        values: list[int] = list(map(int, input().split()))
        matrix.append(values)
    return matrix

print(city_analogimon(4, 4))
