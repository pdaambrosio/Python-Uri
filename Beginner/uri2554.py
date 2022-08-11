def pizza_before_bh(loop: int) -> str:
    result: str = ''
    for _ in range(loop):
        [n_date, d_people] = input().split(' ', 1)
        d_people = list(map(int, d_people.split()))
        
        if all(i == 1 for i in d_people):
            result = n_date
            
        if len(result) == 0:
            result = 'Pizza antes de FdI'

    return result


def main() -> None:
    while True:
        try:
            n: int
            d: int
            n, d = map(int, input().split())
            print(pizza_before_bh(d))
        except EOFError:
            break
        

if __name__ == '__main__':
    main()
