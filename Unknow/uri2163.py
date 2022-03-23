def force_awakens(lines: int, columns: int) -> str:
    terrain: list[list[int]] = []

    for line in range(lines):
        lightsaber_pattern: list[int] = list(map(int, input().split()))
        terrain.append(lightsaber_pattern)

    for line in range(1, lines - 1):
        for column in range(1, columns - 1):
            if terrain[line][column] == 42:
                if terrain[line - 1][column - 1] == 7 and terrain[line - 1][column] == 7 and terrain[line - 1][column + 1] == 7:
                    if terrain[line][column - 1] == 7 and terrain[line][column + 1] == 7:
                        if terrain[line + 1][column - 1] == 7 and terrain[line + 1][column] == 7 and terrain[line + 1][column + 1] == 7:
                            result_line: int = line + 1
                            result_column: int = column + 1
                            return f'{result_line} {result_column}'

    return f'0 0'


def main() -> None:
    n: int
    m: int
    n, m = map(int, input().split())
    print(force_awakens(n, m))


if __name__ == '__main__':
    main()
