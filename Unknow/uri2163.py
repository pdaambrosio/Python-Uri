def force_awakens(lines: int, columns: int) -> str:
    terrain: list[list[int]] = []

    for line in range(lines):
        terrain.append([int(x) for x in input().split()])

    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            if terrain[i][j] == 42:
                if terrain[i - 1][j - 1] == 7 and terrain[i - 1][j] == 7 and terrain[i - 1][j + 1] == 7:
                    if terrain[i][j - 1] == 7 and terrain[i][j + 1] == 7:
                        if terrain[i + 1][j - 1] == 7 and terrain[i + 1][j] == 7 and terrain[i + 1][j + 1] == 7:
                            line: int = i + 1
                            column: int = j + 1
                            return f'{line} {column}'

    return f'0 0'


def main() -> None:
    n: int
    m: int
    n, m = map(int, input().split())
    print(force_awakens(n, m))


if __name__ == '__main__':
    main()
