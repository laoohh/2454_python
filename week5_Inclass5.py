#Example 1: Creating a Database
import pandas as pd
from   sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:\\OneDrive_old\\OneDrive\\BCIT\\2454 Python\\DataSet\\"
CSV_DATA = "brazil_forestFires.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',',
                 names=('year', 'state',  'month', 'number','date', ))
print(df.tail())

# Create the database at the specified path.
DB_FILE    = 'forestFire22222.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

# Store data in database in a table named 'brazilForest'.
df.to_sql(name='brazilForest', con=connection, if_exists='replace', index=False)


# Example 2: Reading from a Sqlite Database
import pymysql

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf


# Get DataFrame contents for 'Rio' and 'Sao Paulo' only.
sql = "SELECT * FROM " + "brazilForest" \
      + " WHERE state = 'Rio' OR state='Sao Paulo' " \
      + " ORDER BY date"

newDf = showQueryResult(sql, connection)
print(newDf.tail())


# Exercise 3
import pandas as pd
from   sqlalchemy import create_engine
import pymysql

# The data file path and file name need to be configured.
PATH     = "C:\\OneDrive_old\\OneDrive\\BCIT\\2454 Python\\DataSet\\"

# Create the database at the specified path.
DB_FILE    = 'ramenReviews.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf


# Get DataFrame contents
sql = "SELECT * FROM " + "Review"

newDf = showQueryResult(sql, connection)
print(newDf)


# Example 4: Inserting Data Into MySQL
import pandas as pd
from   sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:\\datasets\\"
CSV_DATA = "brazil_forestFires.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',',
                 names=('year', 'state',  'month', 'number','date', ))
print(df.tail(2))

import pymysql
# My user name is ‘root’ and my password is an empty string ‘’.
dbStr = "mysql+pymysql://root:@localhost/brazilFires?host=localhost?port=3306"
engine      = create_engine(dbStr, echo=False)
connection  = engine.connect()

try:
    # Store data in database in a table named 'brazilForest'.
    df.to_sql(name='brazilForest', con=connection,
              if_exists='replace', index=False)
except:
    print("The table already exists.")
    print("If you want, you can use 'append' to add data.")



# Example 6: Reading from and to Excel
import openpyxl
import pandas as pd

PATH        = "C:\\OneDrive_old\\OneDrive\\BCIT\\2454 Python\\DataSet\\"
FILE_NAME   = "Tides.xlsx"
df          = pd.read_excel(PATH + FILE_NAME, sheet_name='Sheet1')
df.to_excel(PATH + "NewFile.xlsx", sheet_name='Sheet1')
print (df)






