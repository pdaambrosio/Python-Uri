def the_return_of_radar(test_case: int) -> int:
    if test_case % 2 == 0:
        return (test_case * 2) - 2
    return (test_case * 2) - 1


def main():
    while True:
        T: int = int(input())

        if T == 0:
            break

        for i in range(T):
            test: int = int(input())
            print(the_return_of_radar(test))



if __name__ == '__main__':
    main()
