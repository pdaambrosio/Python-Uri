def square_root_ten(number: int) -> str:
    equation: float = 1/6
    if number == 0:
        return f'{3:.10f}'
    
    while number >= 2:
        equation = 1/(6 + equation)
        number -= 1
    return f'{(equation + 3):.10f}'


def main():
    n: int = int(input())
    print(square_root_ten(n))


if __name__ == '__main__':
    main()
