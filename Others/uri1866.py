c = int(input())


def bill_challenge(loop):
    for _ in range(loop):
        test_case = int(input())

        if test_case % 2 == 0:
            print(0)
        else:
            print(1)


bill_challenge(c)
