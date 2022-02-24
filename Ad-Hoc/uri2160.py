def main():
    from typing import Callable
    name_form: Callable[[int], str] = lambda x: 'YES' if len(x) <= 80 else 'NO'
    l: str = input()
    print(name_form(l))


if __name__ == '__main__':
    main()
