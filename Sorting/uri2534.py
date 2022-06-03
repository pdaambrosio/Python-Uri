def sorting_queries(queries: list) -> list:
    """
    Sorting queries
    """
    queries.sort(reverse=True)
    return queries


def grade_citizen(position: int, sorted_queries: list) -> int:
    """
    Grade citizen
    """
    return sorted_queries[position - 1]


def main() -> None:
    """
    Main function
    """
    while True:
        try:
            n: int
            q: int
            [n, q] = map(int, input().split())
            input_queries: list = [x for x in range(n)]

        except EOFError:
            break