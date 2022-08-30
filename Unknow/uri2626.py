def rock_paper_scissors(player1: str, player2: str, player3: str) -> str:
    dodo: str = "Os atributos dos monstros vao ser inteligencia, sabedoria..."
    leo: str = "Iron Maiden's gonna get you, no matter how far!"
    pepper: str = "Urano perdeu algo muito precioso..."
    a_tie: str = "Putz vei, o Leo ta demorando muito pra jogar..."
    states: list[str] = ['Rock','Paper','Scissors']
    
    if player2 == 'pedra' and player3 == 'pedra':
        if player1 == 'papel':
            return dodo
    if player2 == 'tesoura' and player3 == 'tesoura':
        if player1 == 'pedra':
            return dodo
    if player2 == 'papel' and player3 == 'papel':
        if player1 == 'tesoura':
            return dodo
    
    if player1 == 'papel' and player2 == 'papel':
        if player3 == 'tesoura':
            return pepper
    if player1 == 'pedra' and player2 == 'pedra':
        if player3 == 'papel':
            return pepper
    if player1 == 'tesoura' and player2 == 'tesoura':
        if player3 == 'pedra':
            return pepper

    if player1 == 'papel' and player3 == 'papel':
        if player2 == 'tesoura':
            return leo
    if player1 == 'pedra' and player3 == 'pedra':
        if player2 == 'papel':
            return leo
    if player1 == 'tesoura' and player3 == 'tesoura':
        if player2 == 'pedra':
            return leo

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
