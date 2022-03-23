def mac_pronalts(prod_num, amount):
    products = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}
    total_purchased = (products.get(prod_num) * amount)

    return total_purchased


def main():
    loop = int(input())
    costumer_purchased = 0

    for _ in range(loop):
        [prod_num, prod_amount] = map(int, input().split())
        costumer_purchased += mac_pronalts(prod_num, prod_amount)

    print(f'{costumer_purchased:.2f}')


main()
