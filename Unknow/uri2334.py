def little_ducks(ducks: int) -> int:
    if ducks == 0:
        return 0
    return ducks - 1


def main() -> None:
    while True:
        p: int = int(input())
        if p == -1:
            break
        print(little_ducks(p))


if '__main__' == __name__:
    main()
