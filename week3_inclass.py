# exercises 1
# This function performs division. It does not print anything.
def convertStringToFloat(numerator, denominator):
    try:
        return float(numerator)/float(denominator)
    except:
        return None


def showResult(result):
    if (result != None):
        print("The value is " + str(result))
    else:
        print("An error occurred during the division.")


result = convertStringToFloat(15, 5)
showResult(result)

print("")
result = convertStringToFloat(15, 0)
showResult(result)

print("")
result = convertStringToFloat(21, 3)
showResult(result)

print("")
result = convertStringToFloat("abc", 3)
showResult(result)

print("")
result = convertStringToFloat(21, "abc")
showResult(result)


# Example 3
def displayContent(x):
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.

a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))



# Exercise 5
import numpy as np
import matplotlib.pyplot as plt

years       = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
colorado    = [5029196,5029316,5048281,5121771,5193721,5270482,5351218,5452107,
               5540921,5615902,5695564]
connecticut = [3574097,3574147,3579125,3588023,3594395,3594915,3594783,3587509,
               3578674,3573880,3572665]
delaware    = [897934,897934,899595,907316,915188,923638,932596,941413,949216,
               957078,967171]

# red dashes, blue squares and green triangles
plt.plot(years, colorado, "--", color='red', label="Colorado")
plt.plot(years,connecticut, "s", color='blue', label="Connecticut")
plt.plot(years,delaware, "--", color='blue', label="delaware")

# legend
# https://matplotlib.org/users/legend_guide.html
plt.ylim(ymin=0)  # Set's y axis start to 0.
plt.legend(loc='upper left')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title('Population by State')

plt.show()



# Exercise 6
import matplotlib.pyplot as plt

pounds  = [120, 110, 160]
inches  = [50, 48, 68]

plt.scatter(pounds, inches, color='orange', label='Students Region A')

# Add a legend, axis labels, and title.
plt.legend()
plt.xlabel("Weight (pounds)")
plt.ylabel("Height (inches)")
plt.title('Height vs. Weight for Students Region A')

plt.show()



# Exercise 7
import matplotlib.pyplot as plt

poundsA  = [120, 110, 160]
inchesA  = [50, 48, 68]
poundsB  = [121, 108, 150, 121, 121, 146]
inchesB  = [49, 45, 85, 46, 50, 85]

plt.scatter(poundsA, inchesA, color='orange', label='Students Region A')
plt.scatter(poundsB, inchesB, color='green', label='Students Region B')

# Add a legend, axis labels, and title.
plt.legend()
plt.xlabel("Weight (pounds)")
plt.ylabel("Height (inches)")
plt.title('Height vs. Weight for Students Region A and B')

plt.show()



import matplotlib.pyplot as plt

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

plt.bar(x, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x, x)
plt.show()



# Exercise 8
import matplotlib.pyplot as plt
import numpy as np

NUM_MEANS     = 4
NUM_GROUPS    = 3
bc_means      = [20, 35, 30, 35, 27]
alberta_means = [25, 32, 34, 20, 25]
saskatchewan_means = [18, 28, 32, 24, 31]

# This generates indices from 0 to 4 in a format that is accepted for
# plotting bar charts.
ind = np.arange(NUM_MEANS)
print(ind)
width = 0.25
plt.bar(ind, bc_means[:4], width, label='BC')
plt.bar(ind + width, alberta_means[:4], width, label='AB')
plt.bar(ind + width*2, saskatchewan_means[:4], width, label='SA')

plt.ylabel('Revenue')
plt.title('Quarterly Revenue by Province')

plt.xticks(ind + width, ('Q1', 'Q2', 'Q3', 'Q4'))
plt.legend(loc='best')
plt.show()



# Exsample 9
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.
path = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

plt.hist(df["MomAge"], bins=22)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title('Mother Age')

plt.show()




# Example 10
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.
path = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                 sep='\t',
                 names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                        "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                        'orig.id', 'preemie'))

# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
# This line allows us to set the figure size supposedly in inches.
# When rendered in the IDE the output often does not translate to inches.
plt.subplots(nrows=2, ncols=3, figsize=(14, 7))

plt.subplot(2, 3, 1)  # Specfies total rows, columns and image #
# where images are drawn clockwise.
plt.hist(df["MomAge"], bins=22)
plt.xlabel("Mom Age")
plt.ylabel("Frequency")
# plt.title('Mother Age')

plt.subplot(2, 3, 2)
plt.hist(df["MomEduc"], bins=10)
plt.xlabel("Mom Education")
plt.ylabel("Frequency")

# 1 is married
# 2 is unmarried
plt.subplot(2, 3, 3)
plt.hist(df["MomMarital"], bins=10)
t11 = ['', 'Y', 'N']
plt.xticks(range(len(t11)), t11, rotation=50)

# plt.xticks(['Mar', '2'], rotation=50)
plt.xlabel("Mom Married")
plt.ylabel("Frequency")

# 1 is married. 2 is unmarried.
plt.subplot(2, 3, 4)
plt.hist(df["numlive"], bins=10)
plt.xlabel("# Kids")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)  # of rows, # of columns, # plots.
plt.hist(df["DadAge"], bins=22)
plt.xlabel("Dad Age")
plt.ylabel("Frequency")

plt.subplot(2, 3, 6)
plt.hist(df["dobmm"], bins=12)
plt.xlabel("Birth Month")
plt.ylabel("Frequency")

plt.show()



#Exercise 9
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.

path = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age', 'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen', 'Waist', 'Hip', 'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.hist(df["Pct.BF"], bins=10)
plt.xlabel("Pct.BF")

plt.subplot(2, 2, 2)
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")

plt.subplot(2, 2, 3)
plt.hist(df["Weight"], bins=10)
plt.xlabel("Weight")

plt.subplot(2, 2, 4)
plt.hist(df["Height"], bins=10)
plt.xlabel("Height")

plt.show()




# Exercise 10

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='RetailInventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT * FROM RetailInventory"
results = showQueryResult(SQL)
print(results)




Exercise 11

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT * FROM Inventory WHERE price >= 4"
results = showQueryResult(SQL)
print(results)






#Exercise 12

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT * FROM Inventory ORDER BY productName"
results = showQueryResult(SQL)
print(results)






# Example 13


#Exercise 12

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT productName || '-' || vendor AS ProductVendor  FROM Inventory"
results = showQueryResult(SQL)
print(results)




#Exercise 18

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL     = "SELECT MAX(price) AS MaxPrice FROM Inventory"
results = showQueryResult(SQL)
print(results.iloc[0]['MaxPrice'])




#Exercise 19

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT vendor, price * quantity AS revenue FROM Inventory \
                                      GROUP BY vendor"
results = showQueryResult(SQL)
print(results)



#Exercise 20

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT productName, MIN(price) AS minPrice FROM Inventory \
                                      GROUP BY productName"
results = showQueryResult(SQL)
print(results)



# Exercise 21

import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT vendor, SUM(quantity) AS TotalItemsStocked FROM Inventory \
                GROUP BY vendor HAVING vendor = 'Waterford Corp.'"
results = showQueryResult(SQL)
print(results)


# Exercise 22
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT vendor, SUM(price*quantity) AS revenueValue FROM Inventory \
        GROUP BY vendor HAVING vendor ='Silverware Inc.' or vendor ='Waterford Corp.'"
results = showQueryResult(SQL)
print(results)



#Quiz week 3

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Read all rows from the table.
SQL = "SELECT productID, price*quantity as itemValue FROM Inventory \
       WHERE quantity IS NOT NULL"
results = showQueryResult(SQL)
print(str(results))


plt.bar(results["productID"],results["itemValue"], color='green')
plt.xlabel("Product")
plt.ylabel("Revenue $ Value (Price * Qty)")
plt.title("Inventory Value")

plt.xticks(results["productID"], results["productID"])
plt.show()

