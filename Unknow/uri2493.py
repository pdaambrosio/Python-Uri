def operations_game(loop: int) -> list:
    list_answer: list[str] = [' '] * loop
    for i in range(loop):
        question_game: str = input()
        format_question: str = question_game.replace('=', ' ')
        list_question: list[int] = list(map(int, format_question.split()))

        if list_question[0] + list_question[1] == list_question[2]:
            list_answer[i] = '+'
        elif list_question[0] - list_question[1] == list_question[2]:
            list_answer[i] = '-'
        elif list_question[0] * list_question[1] == list_question[2]:
            list_answer[i] = '*'
        else:
            list_answer[i] = 'I'
        
    return list_answer

print(operations_game(int(input())))
