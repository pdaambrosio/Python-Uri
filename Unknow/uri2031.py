def rock_paper_airstrike(player1, player2):
    if player1 == 'ataque':
        if player2 == 'ataque':
            return 'Aniquilacao mutua'
        return 'Jogador 1 venceu'
    elif player1 == 'papel':
        if player2 == 'ataque' or player2 == 'pedra':
            return 'Jogador 2 venceu'
        return 'Ambos venceram'
    elif player1 == 'pedra':
        if player2 == 'papel':
            return 'Jogador 1 venceu'
        if player2 == 'ataque':
            return 'Jogador 2 venceu'
        if player2 == 'pedra':
            return 'Sem ganhador'


def main():
    loop = int(input())
    while loop > 0:
        player1 = input()
        player2 = input()
        print(rock_paper_airstrike(player1, player2))
        loop -= 1


main()
