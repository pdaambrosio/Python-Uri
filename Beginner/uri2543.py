def ufpr_gaming(loop: int, student_id: int) -> int:
    result: int = 0
    for _ in range(loop):
      gameplay: list = list(map(int, input().split()))
      if student_id == gameplay[0] and gameplay[1] == 0:
          result += 1
    return result


def main() -> None:
    while True:
        try:
          loop: int
          student_id: int
          [loop, student_id] = map(int, input().split())
          print(ufpr_gaming(loop, student_id))
        except EOFError:
            break


if __name__ == '__main__':
    main()
