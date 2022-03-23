qt = int(input())

def who_is_next(number):
    for _ in range(number):
        [player1, choice_player1, player2, choice_player2] = input().split()
        [player1_number, player2_number] = map(int, input().split())

        sum_players_number = player1_number + player2_number
        result = ('PAR' if sum_players_number % 2 == 0 else 'IMPAR')

        if result == choice_player1:
            print(player1)
        elif result == choice_player2:
            print(player2)

who_is_next(qt)
