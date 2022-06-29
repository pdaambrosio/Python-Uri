def roller_coaster_restrictions(n_guests: int, minimum_height: int, maximum_height: int) -> int:
    """
    This function receives the number of guests, the minimum height of the
    roller coaster and the maximum height of the roller coaster. It returns
    the number of guests that can be accommodated in the roller coaster.
    """
    guests_allowed:int = 0
    for _ in range(n_guests):
        guest_height:int = int(input())
        if guest_height >= minimum_height and guest_height <= maximum_height:
            guests_allowed += 1
    return guests_allowed


def main() -> None:
    """
    This function receives the number of guests, the minimum height of the
    roller coaster and the maximum height of the roller coaster. It returns
    the number of guests that can be accommodated in the roller coaster.
    """
    while True:
        try:
            n_guests:int
            minimum_height:int
            maximum_height:int
            [n_guests, minimum_height, maximum_height] = map(int, input().split())
            print(roller_coaster_restrictions(n_guests, minimum_height, maximum_height))
        except EOFError:
            break


if __name__ == "__main__":
    main()
