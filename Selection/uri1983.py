def highest_score(num_students):
    high_score = 0
    registration_number = 0

    while num_students != 0:
        [student_id, score] = map(float, input().split())
        if score > high_score:
            high_score = score
            registration_number = student_id
        num_students -= 1

    if high_score >= 8:
        return int(registration_number)
    return 'Minimum note not reached'


def main():
    n = int(input())
    print(highest_score(n))


main()
