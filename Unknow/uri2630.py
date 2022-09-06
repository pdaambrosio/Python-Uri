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
