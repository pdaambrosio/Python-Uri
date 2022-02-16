from typing import Callable

while True:
    try:
        amnesio_password: Callable[[int], int] = lambda x: x - 1
        paper_number: int = int(input())
        print(amnesio_password(paper_number))
    except EOFError:
        break