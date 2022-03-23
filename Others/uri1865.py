n = int(input())


def mjolnir(challenging):
    for _ in range(challenging):
        [name, force] = input().split()

        if name == 'Thor':
            print('Y')
        else:
            print('N')


mjolnir(n)
