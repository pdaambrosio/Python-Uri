def fast_fibonacci(number: int) -> str:
    import math

    n1: float = math.pow((1 + math.sqrt(5)) / 2.0, number)
    n2: float = math.pow((1 - math.sqrt(5)) / 2.0, number)
    result: float = (n1 - n2) / math.sqrt(5)

    return f'{result:.1f}'


def main() -> None:
    n: int = int(input())
    print(fast_fibonacci(n))
    

if __name__ == '__main__':
    main()
