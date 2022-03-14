def engine_failure(num: int, rpm: list[int]) -> int:
    result: int = 0

    for i in range(1, num):
        if (rpm[i - 1]) > rpm[i]:
            result = i + 1
            break
    
    return result


def main() -> None:
    n: int = int(input())
    r: list[int] = list(map(int, input().split()))
    print(engine_failure(n, r))


if __name__ == '__main__':
    main()
