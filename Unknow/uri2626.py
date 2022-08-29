def rock_paper_scissors(player1: str, player2: str, player3: str) -> str:
    dodo: str = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
    leo: str = "Iron Maiden's gonna get you, no matter how far!"
    pepper: str = "Urano perdeu algo muito precioso..."
    a_tie: str = "Putz vei, o Leo ta demorando muito pra jogar..."
    
    if player1 == 'papel' and player2 == 'papel' and player3 == 'tesoura':
        return pepper
    elif player1 == 'papel' and player2 == 'pedra' and player3 == 'pedra':
        return dodo
    elif player1 == 'papel' and player2 == 'tesoura' and player3 == 'papel':
        return leo
    elif player1 == 'pedra' and player2 == 'papel' and player3 == 'pedra':
        return leo
    elif player1 == 'pedra' and player2 == 'pedra' and player3 == 'papel':
        return pepper
    elif player1 == 'pedra' and player2 == 'tesoura' and player3 == 'tesoura':
        return dodo
    elif player1 == 'tesoura' and player2 == 'papel' and player3 == 'papel':
        return dodo
    elif player1 == 'tesoura' and player2 == 'pedra' and player3 == 'tesoura':
        return leo
    elif player1 == 'tesoura' and player2 == 'tesoura' and player3 == 'pedra':
        return pepper
    else:
        return a_tie