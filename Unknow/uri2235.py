def walking_in_time(a:int, b:int, c:int) -> str:
    if a - b == 0 or a - c == 0 or b - c == 0:
        return 'S'
    if a + b - c == 0 or b - c + a == 0 or c - a + b == 0:
        return 'S'
    if a - b - c == 0 or b - a - c == 0 or c - a - b == 0:
        return 'S'

    return 'N'


def main() -> None:
    a: int
    b: int
    c: int
    [a, b, c] = map(int, input().split())
    print(walking_in_time(a, b, c))


if __name__ == '__main__':
    main()
