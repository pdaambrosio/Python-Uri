def force_awakens(lines: int, columns: int) -> str:
    terrain: list[list[int]] = []

    for line in range(lines):
        terrain.append([int(x) for x in input().split()])

    l: int = 0
    c: int = 0

    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            if terrain[i][j] == 42:
                if terrain[i - 1][j - 1] == 7 and terrain[i - 1][j] == 7 and terrain[i - 1][j + 1] == 7:
                    if terrain[i][j - 1] == 7 and terrain[i][j + 1] == 7:
                        if terrain[i + 1][j - 1] == 7 and terrain[i + 1][j] == 7 and terrain[i + 1][j + 1] == 7:
                            l = i + 1
                            c = j + 1
                            return f'{c} {l}'
        return f'{c} {l}'


def main() -> None:
    n: int
    m: int
    n, m = map(int, input().split())
    print(force_awakens(n, m))


if __name__ == '__main__':
    main()


# TODO: Wrong answer (30%)
