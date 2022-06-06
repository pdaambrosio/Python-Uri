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
            input_queries: list = [int(input()) for _ in range(n)]
            sorted_queries: list = sorting_queries(input_queries)
            for _ in range(q):
                position: int = int(input())
                print(grade_citizen(position, sorted_queries))
        except EOFError:
            break


if __name__ == "__main__":
    main()
