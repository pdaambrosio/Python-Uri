def iu_di_oh(player1: list, player2: list, chosen_player1: int, chosen_player2: int, randon_attribute: int) -> str:
    player1_score: int
    player2_score: int
    [player1_score, player2_score] = player1[chosen_player1 - 1][chosen_player2 - 1], \
        player2[randon_attribute - 1][randon_attribute - 1]

    if player1_score > player2_score:
        return 'Marcos'
    elif player2_score > player1_score:
        return 'Leonardo'
    return 'Empate'

