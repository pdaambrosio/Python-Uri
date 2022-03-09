def twitting(tweet: str) -> str:
    if len(tweet) <= 140:
        return 'TWEET'
    return 'MUTE'


def main() -> None:
    text: str = input()
    print(twitting(text))


if __name__ == '__main__':
    main()
