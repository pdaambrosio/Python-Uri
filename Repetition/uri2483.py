def merry_christmaaas(index: int) -> str:
    prefix: str = "Feliz nat"
    for _ in range(index):
        prefix += "a"
    return prefix + "l!"


def main() -> None:
    index: int = int(input())
    print(merry_christmaaas(index))


if __name__ == "__main__":
    main()
