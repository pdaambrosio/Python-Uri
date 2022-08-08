def pizza_before_bh(date: str, people: list[int]) -> str:
    if all(i == 1 for i in people):
        return date
    return 'Pizza antes de FdI'