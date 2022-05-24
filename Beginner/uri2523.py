def wills_message(alphabet: str, number_bulbs: int, bulbs_on: list[int]) -> str:
    result: str = ''
    if number_bulbs == len(bulbs_on):
        for number in bulbs_on:
            for index, letter in enumerate(alphabet):
                if index + 1 == number:
                    result += letter
    return result


def main() -> None:
    while True:
        try:
            input_alphabet: str = input()
            input_number_bulbs: int = int(input())
            input_bulbs_on: list[int] = list(map(int, input().split()))
            print(wills_message(input_alphabet, input_number_bulbs, input_bulbs_on))
        except EOFError:
            break

if __name__ == '__main__':
    main()
