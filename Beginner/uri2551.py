def new_record(loop: int) -> list[int]:
    training_duration: int
    distance: int
    result: list = []
    record: float = 0
    for i in range(1, loop + 1):
        [training_duration, distance] = map(int, input().split())
        if distance / training_duration > record:
            result.append(i)
            record = distance / training_duration
    return result


def main() -> None:
    while True:
        try:
            loop: int = int(input())
            records: list[int] = new_record(loop)
            for i in records:
                print(i)
        except EOFError:
            break


if __name__ == '__main__':
    main()
    exit(0)
