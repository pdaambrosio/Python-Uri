def parity(bit: str) -> str:
    extra_bit = 0
    for i in bit:
        if i == '1':
            extra_bit += 1

    return bit + str(extra_bit % 2) 


def main() -> None:
    s: str = input()
    print(parity(s))


if __name__ == '__main__':
    main()
