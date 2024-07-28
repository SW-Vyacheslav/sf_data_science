import pandas as pd

def create_medications(names, counts):
    return pd.Series(data = counts, index = names)

def get_percent(medications, name):
    medications_sum = sum(medications.iloc[0:3])
    return medications.loc[name] * 100 / medications_sum
