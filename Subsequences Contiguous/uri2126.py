def searching_subsequences(seq1: str, seq2: str) -> str:
    amount: int = seq2.count(seq1)

    if amount == 0:
        return 'Nao existe subsequencia\n'
    position: int = seq2.rfind(seq1)
    return f'Qtd.Subsequencias: {amount}\nPos: {position + 1}\n'


def main():
    case: int = 1
    while True:
        try:
            n1: str = input()
            n2: str = input()
            print(f'Caso #{case}:')
            print(searching_subsequences(n1, n2))
        except EOFError:
            break

        case += 1


main()
