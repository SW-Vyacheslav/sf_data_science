import pandas as pd

def get_experience(arg: str):
    splitted = arg.split()

    if len(splitted) < 4:
        return 0

    month_strings = ["месяца", "месяцев", "месяц"]

    if splitted[3] in month_strings:
        return int(splitted[2])

    year_strings = ["лет", "года", "год"]

    months = 0

    if splitted[3] in year_strings:
        months = months + int(splitted[2]) * 12

    if len(splitted) < 6:
        return months

    if splitted[5] in month_strings:
        months = months + int(splitted[4])

    return months

test_series_1 = pd.Series([
    'Опыт работы 8 лет 3 месяца',
    'Опыт работы 3 года 5 месяцев',
    'Опыт работы 1 год 9 месяцев',
    'Опыт работы 3 месяца',
    'Опыт работы 6 лет'
])

print(test_series_1.apply(get_experience))
