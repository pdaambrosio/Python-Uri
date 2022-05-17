def city_analogimon(rows: int, columns: int) -> int:
    matrix: list = []
    r1: list = []
    r2: list = []
    for _ in range(rows):
        values: list[int] = list(map(int, input().split()))
        matrix.append(values)

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 2:
                r1.append(row)
                r1.append(column)
            if matrix[row][column] == 1:
                r2.append(row)
                r2.append(column)

    result: int = abs(r1[0] - r2[0]) + abs(r1[1] - r2[1])

    return result


def main() -> None:
    while True:
        try:
            input_rows: int
            input_columns: int
            [input_rows, input_columns] = map(int, input().split())
            print(city_analogimon(input_rows, input_columns))
        except EOFError:
            break


if __name__ == "__main__":
    main()
