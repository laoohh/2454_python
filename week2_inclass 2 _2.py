import pandas as pd

# The data file path and file name need to be configured.
PATH     = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "phone_data.csv"
    
# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',', 
                 names=('index', 'date', 'duration', 'item', 'month','network', 
                        'network_type' ))

df2 = df.groupby(['network_type','item'])['index'].count().reset_index()  \
        .rename(columns={'duration': 'total count'})
print(df2)
