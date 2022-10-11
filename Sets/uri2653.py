from itertools import count


def types_jewelry(jewelrys: list[str]) -> int:
    return len(set(jewelrys))


def main() -> None:
    jewelrys = []
    for _ in count():
        try:
            jewelrys.append(input())
        except EOFError:
            break
    print(types_jewelry(jewelrys))


if __name__ == "__main__":
    main()
