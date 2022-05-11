def batmain(villain: str) -> str:
    if villain == 'Superman':
        return 'Why So Serious?'
    return 'Y'


def main() -> None:
    t: int = int(input())
    for _ in range(t):
        villain: str = input()
        print(batmain(villain))


if '__main__' == __name__:
    main()
