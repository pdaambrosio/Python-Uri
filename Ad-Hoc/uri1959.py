def simple_polygons(num1: int, num2: int) -> int:
    return num1 * num2


def main() -> None:
    num1: int
    num2: int
    [num1, num2] = map(int, input().split())
    print(simple_polygons(num1, num2))


if __name__ == "__main__":
    main()
