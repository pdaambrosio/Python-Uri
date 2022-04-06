def diving_competition(name: str, difficulty: float, scores: list[float]) -> str:
    final_score = sum(sorted(scores)[1:6]) * difficulty
    return f'{name} {final_score:.2f}'


def main() -> None:
    loop: int = int(input())
    for _ in range(loop):
        name = input()
        difficulty = float(input())
        scores = list(map(float, input().split()))
        print(diving_competition(name, difficulty, scores))


if '__main__' == __name__:
    main()
