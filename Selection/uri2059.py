def odd_even_cheat(choice_player1, number_j1, number_j2, cheat_player1, accuse_player2):
    if cheat_player1 == 1 and accuse_player2 == 1:
        return 'Jogador 2 ganha!'
    elif cheat_player1 == 1 or accuse_player2 == 1:
        return 'Jogador 1 ganha!'

    odd_even = (number_j1 + number_j2) % 2
    
    if odd_even == 0:
        if choice_player1 == 1:
            return 'Jogador 1 ganha!'
        else:
            return 'Jogador 2 ganha!'
    elif odd_even == choice_player1:
        return 'Jogador 2 ganha!'
    return 'Jogador 1 ganha!'


def main():
    [p, j1, j2, r, a] = map(int, input().split())
    print(odd_even_cheat(p, j1, j2, r, a))


main()
