def square_root(number: int) -> float:
    result: int = 2
    if number == 0:
        return result
    
    result += 1 / square_root(number - 1)
    return result


def main() -> None:
    n: int = int(input())
    x: float = square_root(n) - 1
    print(f'{x:.10f}')


if __name__ == '__main__':
    main()
