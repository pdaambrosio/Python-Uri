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


def players_game(loop: int, list_questions_answer: list[str]) -> str:
    wrong_answer: list[str] = []
    for _ in range(loop):
        players_answer: list[str] = input().split()
        name: str = players_answer[0]
        question: int = int(players_answer[1])
        answer: str = players_answer[2]

        if list_questions_answer[question - 1] != answer:
            wrong_answer.append(name)

    if len(wrong_answer) == 0:
        return 'You Shall All Pass!'

    if len(wrong_answer) == loop:
        return 'None Shall Pass!'
    
    wrong_answer.sort()
    result: str = ' '.join(wrong_answer)

    return result


def main() -> None:
    while True:
        try:
            loop: int = int(input())
            list_questions_answer: list[str] = operations_game(loop)
            print(players_game(loop, list_questions_answer))
        except EOFError:
            break


if __name__ == '__main__':
    main()
