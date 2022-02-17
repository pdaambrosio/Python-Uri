def game_check(num1, num2, jump):
        return abs(num1 - num2) > jump
        

def main():
    [frog_jump, pipes] = map(int, input().split())
    h_pipes = list(map(int, input().split()))

    for i in range(pipes - 1):
        game = game_check(h_pipes[i], h_pipes[i + 1], frog_jump)
        if game == True:
            print('GAME OVER')
            break
    
    if game == False:
        print('YOU WIN')


main()
