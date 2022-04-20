def exam_grades(num: int) -> str:
    if num == 0:
        return 'E'
    elif num < 36:
        return 'D'
    elif num < 61:
        return 'C'
    elif num < 86:
        return 'B'
    return 'A'


def main() -> None:
    num = int(input())
    print(exam_grades(num))


if '__main__' == __name__:
    main()
