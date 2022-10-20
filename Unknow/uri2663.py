def fase(n_competitor: int, k_approved: int, participants: list[int]) -> int:
    count: int = k_approved
    participants.sort(reverse=True)
    for i in range(n_competitor):
        if participants[count] == participants[k_approved - 1]:
            count += 1
    return count


def main() -> None:
    n_competitor: int = int(input())
    k_approved: int = int(input())
    participants = [int(input()) for _ in range(n_competitor)]
    print(fase(n_competitor, k_approved, participants))


if __name__ == '__main__':
    main()
