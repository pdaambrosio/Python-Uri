def which_triangle(a: int, b: int, c: int) -> str:
    nums: list[int] = [a, b, c]
    higher_number:int = max(nums)
    minor_number:int = min(nums)
    is_triangle: int = a + b + c - higher_number - minor_number

    if higher_number >= minor_number + is_triangle:
        return 'Invalido'


    if a == b == c:
        return 'Valido-Equilatero'
    elif a == b or b == c or a == c:
        return 'Valido-Isoceles'
    else:
        return 'Valido-Escaleno'

#FIXME: fix the function is_rectangle (Wrong answer 5%)
def is_rectangle(a: int, b: int, c: int) -> str:
    if (pow(a, 2)) + (pow(b, 2)) == (pow(c, 2)):
        return 'Retangulo: S'
    return 'Retangulo: N'



def main() -> None:
    [a, b, c] = map(int, input().split())
    triangle: str = which_triangle(a, b, c)
    rectangle: str = is_rectangle(a, b, c)

    if triangle != 'Invalido':
        print(f'{triangle}\n{rectangle}')
    else:
        print(triangle)


if '__main__' == __name__:
    main()
