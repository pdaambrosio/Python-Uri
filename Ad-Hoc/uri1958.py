def scientific_notation(number):
    from decimal import Decimal

    if Decimal(number) >= 0 and '-' != number[0]:
        print('+', end='')

    number = Decimal(number)
    print('%.4E' % number)


def main():
    value = input()
    scientific_notation(value)


if __name__ == '__main__':
    main()
