def hacker_metal_band(num_x: int, num_y: int) -> str:
    greatest_hits: dict = {0: 'PROXYCITY', 1: 'P.Y.N.G.', 2: 'DNSUEY!', 3: 'SERVERS', 4: 'HOST!', 5: 'CRIPTONIZE', 6: 'OFFLINE DAY', 7: 'SALT', 8: 'ANSWER!', 9: 'RAR?', 10: 'WIFI ANTENNAS'}
    return greatest_hits[num_x + num_y]


def main() -> None:
    n: int = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        print(hacker_metal_band(x, y))


if __name__ == '__main__':
    main()
