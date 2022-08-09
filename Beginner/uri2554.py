def pizza_before_bh(loop: int, date: str, people: list[int]) -> str:
    if all(loop == 1 for loop in people):
        return date
    return 'Pizza antes de FdI'


def main() -> None:
    while True:
        try:
            n: int
            d: int
            [n, d] = list(map(int, input().split()))
            for _ in range(d):
                [n_date, d_people] = input().split(' ', 1)
                d_people = list(map(int, d_people.split()))
                
                if pizza_before_bh(n, n_date, d_people) == n_date:
                    print(n_date)
                    
                if pizza_before_bh(n, n_date, d_people) == 'Pizza antes de FdI':
                    print('Pizza antes de FdI')
        except EOFError:
            break
        

if __name__ == '__main__':
    main()
