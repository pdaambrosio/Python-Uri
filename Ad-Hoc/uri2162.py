def peaks_and_valleys(num: int, *args: int) -> int:
    peak: int = 1
    if num == 2 and args[0] == args[1]:
        peak = 0

    for i in range(1, num - 1):
        if not ((args[i] < args[i-1] and args[i] < args[i+1]) or (args[i] > args[i-1] and args[i] > args[i+1])):
            peak = 0

    return peak


def main():
    n: int = int(input())
    h: list[int] = [int[x] for x in input().split()]
    print(peaks_and_valleys(n, *h))


if __name__ == '__main__':
    main()
