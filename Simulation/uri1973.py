def star_trek(number_star, number_sheep):
    number_sheep = list(number_sheep)
    total_attacks = sum(number_sheep)
    attacked_stars = [0 for _ in range(number_star)]
    loop = 0

    while loop >= 0 and loop < number_star:
        side_test = number_sheep[loop] % 2
        
        if number_sheep[loop] > 0:
            number_sheep[loop] -= 1
            attacked_stars[loop] = 1
            total_attacks -= 1
        
        if side_test:
            loop += 1
        else:
            loop -= 1

    attacked_stars = attacked_stars.count(1)

    return f'{attacked_stars} {total_attacks}'



def main():
    n = int(input())
    x = map(int, input().split())

    print(star_trek(n, x))

main()
