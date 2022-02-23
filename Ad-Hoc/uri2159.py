def approximate_number_primes(num: int) -> float:
    from math import log
    return f'{num / log(num):.1f} {1.25506 * (num / log(num)):.1f}'


def main():
    n: int = int(input())
    print(approximate_number_primes(n))


if __name__ == '__main__':
    main()
