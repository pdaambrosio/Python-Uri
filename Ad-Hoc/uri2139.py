def days_left_until_christmas(month: str, day: str) -> str:
    from datetime import datetime

    if len(month) == 1:
        month = '0' + month
    
    if len(day) == 1:
        day = '0' + day

    date: datetime = datetime.strptime('2016' + month + day, '%Y%m%d')
    christmas_day: datetime = datetime.strptime('20161225', '%Y%m%d')
    days_left: int = (christmas_day - date).days

    if days_left == 0:
        return 'E natal!'

    if days_left == 1:
        return 'E vespera de natal!'

    if days_left < 0:
        return 'Ja passou!'
        
    return f'Faltam {days_left} dias para o natal!'


def main():
    while True:
        try:
            m: str
            d: str
            [m, d] = input().split()
            print(days_left_until_christmas(m, d))
        except EOFError:
            break


if __name__ == '__main__':
    main()
