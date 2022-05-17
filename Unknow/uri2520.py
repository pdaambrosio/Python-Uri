def city_analogimon(rows: int, columns: int) -> list:
    r1: int = 0
    r2: int = 0
    r3: int = 0
    r4: int = 0

    for row in rows:
        for column in columns:
            pass 


def main() -> None:
    rows: int
    columns: int
    [rows, columns ]= map(int, input().split())
    print(city_analogimon(rows, columns))


if __name__ == "__main__":
    main()
