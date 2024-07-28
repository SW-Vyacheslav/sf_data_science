import pandas as pd

def create_companyDF(income, expenses, years):
    return pd.DataFrame({ "Income": income, "Expenses": expenses },
                        index = years)

def get_profit(df, year):
    if year not in df.index:
        return None

    data = df.loc[year]

    return data.iloc[0] - data.iloc[1]
