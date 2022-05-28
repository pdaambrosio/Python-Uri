def calc_api(loop: int) -> str:
    m: int = 0
    result: int = 0
    for _ in range(loop):
        n: int
        c: int
        [n, c] = map(int, input().split())
        m += c
        result += n * c
    api: float = result / (m * 100)
    return f'{api:.4f}'


def main() -> None:
    while True:
        try:
            loop: int = int(input())
            print(calc_api(loop))
        except EOFError:
            break


if __name__ == "__main__":
    main()