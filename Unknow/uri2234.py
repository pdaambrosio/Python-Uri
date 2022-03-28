def hot_dogs(participants: int, dogs: int) -> str:
    return f'{participants / dogs:.2f}'


def main() -> None:
    participants: int
    dogs: int
    [participants, dogs] = map(int, input().split())
    print(hot_dogs(participants, dogs))


if __name__ == '__main__':
    main()
