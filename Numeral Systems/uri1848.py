def three_eyed_lottery():
    for _ in range(3):
        sum_blink = 0

        while True:
            blink = input()
            if blink != 'caw caw':
                blink = ('0' if s == '-' else '1' for s in blink)
                blink_output = int(''.join(blink), 2)
                sum_blink += blink_output
            else:
                print(sum_blink)
                break

three_eyed_lottery()
