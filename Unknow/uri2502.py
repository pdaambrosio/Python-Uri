def desencrypt_card(loop: int, key_one: str, key_two: str) -> str:
    key_one_lower: str = key_one.lower()
    key_two_lower: str = key_two.lower()
    key_one_upper: str = key_one.upper()
    key_two_upper: str = key_two.upper()
    result: str = ''
    for _ in range(loop):
        text_encrypted: str = input()
        for caracter in text_encrypted:
            if caracter in key_one_lower:
                result += key_two_lower[key_one_lower.index(caracter)]
            elif caracter in key_two_lower:
                result += key_one_lower[key_two_lower.index(caracter)]
            elif caracter in key_one_upper:
                result += key_two_upper[key_one_upper.index(caracter)]
            elif caracter in key_two_upper:
                result += key_one_upper[key_two_upper.index(caracter)]
            else:
                result += caracter
        result += '\n'
    return f'{result}'


def main() -> None:
    while True:
        try:
            cn: list[int]
            cn = list(map(int, input().split()))
            k_one = input()
            k_two = input()
            print(desencrypt_card(cn[1], k_one, k_two))
        except EOFError:
            break


if __name__ == '__main__':
    main()
