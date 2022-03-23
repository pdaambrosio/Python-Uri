def identifying_tea(tea, answer):
    return answer.count(tea)


def main():
    tea_type = int(input())
    contestant_answer = list(map(int, input().split()))
    print(identifying_tea(tea_type, contestant_answer))


if __name__ == '__main__':
    main()
