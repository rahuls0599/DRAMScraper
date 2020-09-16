import numpy as np
import pandas as pd

df_all_time = pd.read_csv("DxSpotPrice.csv")
df_all_time['Dimension'] = "All Time"

for column in list(df_all_time.columns):
    if (column != 'Date' and column != 'Category' and column != 'Dimension'):
        first_value = float(df_all_time.loc[df_all_time[column].first_valid_index(), column])
        df_all_time[column+"Normalised"] = df_all_time[column] / first_value

#print(df_all_time)
df_all_time.to_csv("DxSpotPriceNormalisedAllTime.csv", index=False)

df_3_months = pd.read_csv("DxSpotPrice.csv")
df_3_months['Dimension'] = "Three Months"

for column in list(df_3_months.columns):
    if(column != 'Date' and column != 'Category' and column != 'Dimension'):

        df_3_months[column+"Normalised3"] = df_3_months[column] / first_value