def votes_impeachment(number_of_playes: int, votes: list[int]) -> str:
    """
    Function that returns the number of impeachment votes
    """
    count: int = votes.count(1)
    if (count / number_of_playes) >= (2 / 3):
        return 'impeachment'
    return 'acusacao arquivada'


def main() -> None:
    """
    Main function
    """
    while True:
        try:
            n: int = int(input())
            v: list[int] = list(map(int, input().split()))
            print(votes_impeachment(n, v))
        except EOFError:
            break


if __name__ == '__main__':
    main()
