def i_am_toorg(question: str) -> str:
    if question:
        return 'I am Toorg!'


def main() -> None:
    loop: int = int(input())
    for _ in range(loop):
        input_question: str = input()
        print(i_am_toorg(input_question))
    

if __name__ == '__main__':
    main()
