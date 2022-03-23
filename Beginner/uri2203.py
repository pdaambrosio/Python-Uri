def crowstorm_lol(list_args: list) -> str:
    from math import sqrt, pow
    [xf, yf, xi, yi, vi, r1, r2] = list(map(int, list_args))
    distance: float = sqrt(pow((xf - xi), 2) + pow((yf - yi), 2))

    if r1 + r2 >= distance + 1.5 * vi:
        return 'Y'
    return 'N'

def main() -> None:
    while True:
        try:
            list_args: list[str] = input().split()
            print(crowstorm_lol(list_args))
        except EOFError:
            break

if __name__ == '__main__':
    main()
