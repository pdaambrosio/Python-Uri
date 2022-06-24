def kage_bunshin_no_jutsu(copies_of_ninja: int) -> int:
    result: int = 0
    while copies_of_ninja > 1:
      copies_of_ninja = copies_of_ninja // 2
      result += 1
    return result


def main() -> None:
    while True:
        try:
            n: int = int(input())
            print(kage_bunshin_no_jutsu(n))
        except EOFError:
            break


if __name__ == '__main__':
    main()
