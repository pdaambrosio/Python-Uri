def fast_fibonacci(number: int) -> str:
    from math import pow, sqrt

    n1: float = pow((1 + sqrt(5)) / 2.0, number)
    n2: float = pow((1 - sqrt(5)) / 2.0, number)
    result: float = (n1 - n2) / sqrt(5)

    return f'{result:.1f}'


def main() -> None:
    n: int = int(input())
    print(fast_fibonacci(n))
    

if __name__ == '__main__':
    main()
