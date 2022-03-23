salary: float = float(input())
taxes: float = 0
result: str = 'R$ {:.2f}'

if salary <= 2000:
    print('Isento')
elif salary <= 3000:
    taxes = (salary - 2000) * 0.08
    print(result.format(taxes))
elif salary <= 4500:
    taxes = ((salary - 3000) * 0.18) + (1000 * 0.08)
    print(result.format(taxes))
else:
    taxes = ((salary - 4500) * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print(result.format(taxes))
