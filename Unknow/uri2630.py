def greyscale(conversion: str, r: int, g: int, b:int) -> int:
    result: int = 0
    match conversion:
        case 'eye':
            result = int(r*0.30 + g*0.59 + b*0.11)
        case 'mean':
            result = int((r + g + b) / 3)
        case 'max':
            result = max(r, g, b)
        case 'min':
            result = min(r, g, b)
    return result


def main() -> None:
    loop: int = int(input())
    for i in range(loop):
        input_conversion: str = input()
        input_r: int
        input_g: int
        input_b: int
        [input_r, input_g, input_b] = map(int, input().split())
        case_result: int = greyscale(input_conversion, input_r, input_g, input_b)
        print(f'Caso #{i+1} {case_result}')
        
if __name__ == '__main__':
    main()
