def final_iudioh(player1: list, player2: list, chosen_player1: int, chosen_player2: int, randon_attribute: int) -> str:
    player1_score: int
    player2_score: int
    [player1_score, player2_score] = player1[chosen_player1 - 1][randon_attribute - 1], \
        player2[chosen_player2 - 1][randon_attribute - 1]

    if player1_score > player2_score:
        return 'Marcos'
    elif player2_score > player1_score:
        return 'Leonardo'
    return 'Empate'


def main() -> None:
    while True:
        try:
            input()
            m: int
            l: int
            [m, l] = map(int, input().split())
            marcos: list = []
            leonardo: list = []

            for _ in range(m):
                marcos.append(list(map(int, input().split())))

            for _ in range(l):
                leonardo.append(list(map(int, input().split())))
              
            cm: int
            cl: int
            [cm, cl] = map(int, input().split())
            randon: int = int(input())

            print(final_iudioh(marcos, leonardo, cm, cl, randon))
        except EOFError:
            break


if __name__ == '__main__':
    main()
