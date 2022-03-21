def ten_thousand_years(years_past):
    if years_past <= 2014:
        return f'{2015 - years_past} D.C.'
    return f'{years_past - 2014} A.C.'


def main():
    loop = int(input())
    for _ in range(loop):
        years = int(input())
        print(ten_thousand_years(years))


main()
