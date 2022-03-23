def lengths(a, b, c):
    if abs((b - c)) < a < (b + c) and abs((a - c)) < b < (a + c) and abs((a - b)) < c < (a + b):
        return True
    return False


def triangle(a, b, c, d):
    if lengths(a, b, c) or lengths(a, b, d) or lengths(a, c, d) or lengths(b, c, d):
        return 'S'
    return 'N'


def main():
    [a, b, c, d] = map(int, input().split())
    print(triangle(a, b, c, d))


if __name__ == '__main__':
    main()
