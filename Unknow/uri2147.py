def galopeira(word: str) -> float:
    return f'{0.01 * len(word):.2f}'


def main():
    c: int = int(input())

    for i in range(c):
        t: str = input()
        print(galopeira(t))


if __name__ == '__main__':
    main()
