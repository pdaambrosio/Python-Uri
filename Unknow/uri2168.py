def twilight_at_portland(corners: int, cam: list) -> None:
    for i in range(corners):
        for n in range(corners):
            if cam[i][n] + cam[i][n + 1] + cam[i + 1][n] + cam[i + 1][n + 1] < 2:
                print('U', end='')
            else:
                print('S', end='')
        print()


def main() -> None:
    n: int = int(input())
    c: list[list[int]] = [list(int(x) for x in input().split()) for i in range(n + 1)]
    twilight_at_portland(n, c)


if __name__ == '__main__':
    main()
