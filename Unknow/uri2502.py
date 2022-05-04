def deciphering_encrypted_card(number_of_letters: int, loop: int, key_one: str, key_two: str):
    key_one_lower: str = key_one.lower()
    key_two_lower: str = key_two.lower()
    key_one_upper: str = key_one.upper()
    key_two_upper: str = key_two.upper()
    for _ in range(loop):
        text_encrypted: str = input()
        for caracter in text_encrypted:
            if caracter in key_one_lower:
                return f'{key_two_lower[key_one_lower.index(caracter)]}\b'
            elif caracter in key_two_lower:
                return f'{key_one_lower[key_two_lower.index(caracter)]}\b'

            if caracter in key_one_upper:
                return f'{key_two_upper[key_one_upper.index(caracter)]}\b'
            elif caracter in key_two_upper:
                return f'{key_one_upper[key_two_upper.index(caracter)]}\b'
            
            return f'{caracter}\b'


def main() -> None:
    while True:
        try:
            c: int
            n: int
            [c, n] = map(int, input().split())
            k_one = input()
            k_two = input()
            print(deciphering_encrypted_card(c, n, k_one, k_two))
        except EOFError:
            break


if __name__ == '__main__':
    main()
