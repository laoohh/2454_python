import pandas as pd

PATH     = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"

CSV_DATA = "brazil_forestFires.csv"

df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',', names=('year', 'state',  'month', 'number','date', ))

dfStats = df.groupby(['state','year'])['number'].sum().reset_index()  \
        .rename(columns={'number': 'Sum of all units of burn area'})
 
print(dfStats)