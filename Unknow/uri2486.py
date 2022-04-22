def calc_vitamin(loop: int, amount: int, item: str) -> int:
    food_list: dict = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga': 56, 'laranja':50, 'brocolis':34}
    vitamin: int = 0
    for _ in range(loop):
        vitamin = food_list[item] * amount
    return vitamin


def calc_daily_intake(calc_num: int) -> str:
    if calc_num < 110:
        return f'Mais {110 - calc_num} mg'
    if calc_num > 130:
        return f'Menos {calc_num - 130} mg'
    return f'{calc_num} mg'


def main() -> None:
    while True:
        loop: int = int(input())
        result: int = 0
        if loop == 0:
            break
        for _ in range(loop):
            intake_per_person: list = input().split()
            t: int = int(intake_per_person[0])
            n: str = ' '.join(intake_per_person[1:])
            result += calc_vitamin(loop, t, n)
        print(calc_daily_intake(result))


if __name__ == '__main__':
    main()
