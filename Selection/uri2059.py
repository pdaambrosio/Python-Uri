def odd_even_cheat(choice_player1: int, number_j1: int, number_j2: int, cheat_player1: int, accuse_player2: int) -> str:
    player_one_win: str = 'Jogador 1 ganha'
    player_two_win: str = 'Jogador 2 ganha'

    if cheat_player1 == 1 and accuse_player2 == 1:
        return player_two_win

    if cheat_player1 == 1 or accuse_player2 == 1:
        return player_one_win

    odd_even = (number_j1 + number_j2) % 2
    
    if odd_even == 0:
        if choice_player1 == 1:
            return player_one_win
        return player_two_win

    if odd_even == choice_player1:
        return player_two_win
    return player_one_win


def main() -> None:
    [p, j1, j2, r, a] = map(int, input().split())
    print(odd_even_cheat(p, j1, j2, r, a))


if __name__ == '__main__':
    main()
