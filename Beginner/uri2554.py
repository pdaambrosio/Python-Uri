def pizza_before_bh(date: str, people: list[int]) -> str:
    if all(i == 1 for i in people):
        return date
    return 'Pizza antes de FdI'


print(pizza_before_bh('5/10/2016', [1, 1, 1, 1, 1]))
print(pizza_before_bh('5/10/2016', [1, 1, 1, 0, 1]))