def rock_paper_scissors(player1: str, player2: str, player3: str) -> str:
    dodo: str = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
    leo: str = "Iron Maiden's gonna get you, no matter how far!"
    pepper: str = "Urano perdeu algo muito precioso..."
    a_tie: str = "Putz vei, o Leo ta demorando muito pra jogar..."
    
    if player1 == 'papel' and player2 == 'papel' and player3 == 'tesoura':
        return pepper
    if player1 == 'papel' and player2 == 'pedra' and player3 == 'pedra':
        return dodo
    if player1 == 'papel' and player2 == 'tesoura' and player3 == 'papel':
        return leo
    if player1 == 'pedra' and player2 == 'papel' and player3 == 'pedra':
        return leo
    if player1 == 'pedra' and player2 == 'pedra' and player3 == 'papel':
        return pepper
    if player1 == 'pedra' and player2 == 'tesoura' and player3 == 'tesoura':
        return dodo
    if player1 == 'tesoura' and player2 == 'papel' and player3 == 'papel':
        return dodo
    if player1 == 'tesoura' and player2 == 'pedra' and player3 == 'tesoura':
        return leo
    if player1 == 'tesoura' and player2 == 'tesoura' and player3 == 'pedra':
        return pepper

    return a_tie
    

def main() -> None:
    while True:
        try:
            input_dodo: str
            input_leo: str
            input_pepper: str
            [input_dodo, input_leo, input_pepper] = input().split()
            print(rock_paper_scissors(input_dodo, input_leo, input_pepper))
        except EOFError:
            break
    

if __name__ == '__main__':
    main()
