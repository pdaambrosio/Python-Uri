def already_took_the_candle(hour: int, minute: int, port: int) -> str:
    occurrence_recorded: str = ('A porta abriu!' if port == 1 else 'A porta fechou!')
    return f'{hour:02}:{minute:02} - {occurrence_recorded}'


def main() -> None:
    loop: int = int(input())
    m: int
    n: int
    o: int

    for _ in range(loop):
        [m, n, o] = map(int, input().split())
        print(already_took_the_candle(m, n, o))


if __name__ == '__main__':
    main()    
