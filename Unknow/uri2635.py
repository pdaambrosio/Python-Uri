def web_search(loop_seach: int, loop_queries: int, list_search: list[str], list_queries: list[str]) -> list[str]:
    assert loop_queries == len(list_queries)
    assert loop_seach == len(list_search)
    result: list = []
    for querie in list_queries:
        count_search: int = 0
        len_search: int = 0
        for search in list_search:
            if querie == search[:len(querie)]:
                count_search += 1
                
                if len_search < len(search):
                    len_search = len(search)
                
        if count_search > 0:
            result.append(f'{count_search} {len_search}')
        else:
            result.append('-1')
        
    return result


def main() -> None:
    loop_search: int = int(input())
    list_search: list[str] = [input() for _ in range(loop_search)]
    loop_queries: int = int(input())
    list_queries: list[str] = [input() for _ in range(loop_queries)]
    result: list[str] = web_search(loop_search, loop_queries, list_search, list_queries)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
