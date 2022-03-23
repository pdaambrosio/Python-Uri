def closing_tabs(num_tabs: int, num_actions: int) -> int:
    for _ in range(num_actions):
        action: str = input()
        if action == 'fechou':
            num_tabs += 1
        else:
            num_tabs -= 1
    return num_tabs


if __name__ == '__main__':
    N: int
    M: int
    N, M = list(map(int, input().split()))
    print(closing_tabs(N, M))
