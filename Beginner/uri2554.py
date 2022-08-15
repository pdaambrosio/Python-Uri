from typing import Union

def pizza_before_bh(loop: int) -> str:
    result: str = ''
    for _ in range(loop):
        n_date: str
        d_people: Union[str, list]
        [n_date, d_people] = input().split(' ', 1)
        d_people = list(map(int, d_people.split()))

        if len(result) == 0:
            if all(i == 1 for i in d_people):
                result = n_date

    return result if result else 'Pizza antes de FdI'


def main() -> None:
    while True:
        try:
            values_input: list[str] = input().split()
            d: int = int(values_input[1])
            print(pizza_before_bh(d))
        except EOFError:
            break
        

if __name__ == '__main__':
    main()
