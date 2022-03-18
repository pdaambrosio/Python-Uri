def event(xp: str) -> int:
    n: int
    m: int
    [n, m] = list(map(int, xp.split()))

    if n == 0 and m == 0:
        return False
    
    return n * m


def main() -> None:
    while True:
        e: str = input()
        if event(e) == False:
            break
        
        print(event(e))


if __name__ == '__main__':
    main()
