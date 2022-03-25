def pomekons_battle(bonus: int, player1_pokemons_attack: list[int], player2_pokemons_attack: list[int]) -> str:
    [player1_ai, player1_di, player1_li] = player1_pokemons_attack
    [player2_ai, player2_di, player2_li] = player2_pokemons_attack
    player1_attack: float = (player1_ai + player1_di) / 2.0
    player2_attack: float = (player2_ai + player2_di) / 2.0

    if player1_li % 2 == 0:
        player1_attack += bonus

    if player2_li % 2 == 0:
        player2_attack += bonus

    if player1_attack > player2_attack:
        return 'Dabriel'

    if player2_attack > player1_attack:
        return 'Guarte'
    
    return 'Empate'


def main() -> None:
    game: int = int(input())
    while game > 0:
        bonus: int = int(input())
        player1_pokemons_attack: list[int] = list(map(int, input().split()))
        player2_pokemons_attack: list[int] = list(map(int, input().split()))
        print(pomekons_battle(bonus, player1_pokemons_attack, player2_pokemons_attack))
        game -= 1


if __name__ == '__main__':
    main()
