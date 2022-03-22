def galopeira(word: str) -> str:
    return f'{0.01 * len(word):.2f}'


def main() -> None:
    c: int = int(input())

    for i in range(c):
        t: str = input()
        print(galopeira(t))


if __name__ == '__main__':
    main()
