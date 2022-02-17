def two_bills(buy_price: int, price_paid: int) -> bool:
    bills: list[int] = [2, 5, 10, 20, 50, 100]
    the_change: int = price_paid - buy_price
    result: bool = False

    for i, item in enumerate(bills):
        for n, item in enumerate(bills):
            if bills[i] + bills[n] == the_change:
                result = True

    return result


def main():
    while True:
        try:
            n: int
            m: int
            [n, m] = list(map(int, input().split()))

            if n == 0 or m == 0:
                break

            if two_bills(n, m):
                print('possible')
            else:
                print('impossible')
        except ValueError:
            break


if __name__ == '__main__':
    main()
