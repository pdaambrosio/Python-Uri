def percentage(value1: int, value2: int) -> str:
    return f'{(value2 / value1) * 100:.2f} %'


def sum_values(loop: int) -> str:
    sum_service: int = 0
    sum_block: int = 0
    sum_attack: int = 0
    sum_service_successful: int = 0
    sum_block_successful: int = 0
    sum_attack_successful: int = 0

    for _ in range(loop):
        input()
        list_attempts: list[int] = list(map(int, input().split()))
        list_successful: list[int] = list(map(int, input().split()))
        [service_attempts, block_attempts, attack_attempts] = list_attempts
        [service_successful, block_successful, attack_successful] = list_successful
        sum_service += service_attempts
        sum_block += block_attempts
        sum_attack += attack_attempts
        sum_service_successful += service_successful
        sum_block_successful += block_successful
        sum_attack_successful += attack_successful

    return f'Pontos de Saque: {percentage(sum_service, sum_service_successful)}.\n' \
           f'Pontos de Bloqueio: {percentage(sum_block, sum_block_successful)}.\n' \
           f'Pontos de Ataque: {percentage(sum_attack, sum_attack_successful)}.'


def main() -> None:
    loop: int = int(input())
    print(sum_values(loop))


if __name__ == '__main__':
    main()
