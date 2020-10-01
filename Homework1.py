import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Import data into a DataFrame.
path = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/fruit.csv"
df = pd.read_csv(path, skiprows=1,
                 names=('Date','Product','Quantity','Price','Region'))



# Question 1

df['Year']  = [df['Date'].iloc[i].split("/")[2] for i in range(len(df['Date']))]
df['Month'] = [df['Date'].iloc[i].split("/")[0] for i in range(len(df['Date']))]
df['Day']   = [df['Date'].iloc[i].split("/")[1] for i in range(len(df['Date']))]


#df['Date'] = pd.to_datetime(df['Date'])
#df['Year'] = df['Date'].dt.year
#df['Month'] = df['Date'].dt.month
#df['Day'] = df['Date'].dt.day


df=df.drop('Date', axis=1)

print(df)
print("")
print("")

# Question 2
df["Revenue"] = df["Price"] * df["Quantity"]
df['Revenue']=df['Revenue'].round(2)
#df['Price']=df['Price'].round(2)
df=df.sort_values(['Year','Month','Day'],ascending=[True,True,True])
print(df)
print("")
print("")


#Question 3
dfStats = df.groupby('Product')['Price'].mean().reset_index()  \
            .rename(columns={'Price': 'PriceAVG'})
dfStats['PriceSTD'] = df.groupby('Product')['Price'].std().reset_index()['Price']
dfStats['PriceAVG'] = round(dfStats['PriceAVG'], 2)
dfStats['PriceSTD'] = round(dfStats['PriceSTD'], 2)

print(dfStats)
print("")
print("")


# Question 4
from sqlalchemy import create_engine

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='FruitSales', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL= "SELECT Year,Month,product, SUM(Price*Quantity) AS revenue FROM FruitSales GROUP BY Year,Month,product"
results = showQueryResult(SQL)
results['revenue']=round(results['revenue'],2)

print(results)
print("")
print("")

# this way better
dfSummary = df[['Year','Month','Product','Revenue']]  \
    .groupby(['Year','Month','Product'])['Revenue'].sum()
print(dfSummary)
print("")
print("")


# Question 5
SQL= "SELECT Region,Product, SUM(Price*Quantity) AS revenue, AVG(Price) AS meanPrice FROM FruitSales Group by Region,Product"
results = showQueryResult(SQL)
results['revenue']=round(results['revenue'],2)
results['meanPrice']=round(results['meanPrice'],2)

print(results)
print("")
print("")

# another way
dfSummary = df[['Region','Product','Revenue']]  \
    .groupby(['Region','Product'])['Revenue'].sum().reset_index()
dfSummary['meanPrice'] = df[['Region','Product','Price']]  \
    .groupby(['Region','Product'])['Price'].mean().reset_index()['Price'].round(2)
print(dfSummary)
print("")
print("")


# Question 6
SQL= "SELECT Product, SUM(Price*Quantity) AS revenue, SUM(Quantity) AS totalQuantities FROM FruitSales Group by Product"
results = showQueryResult(SQL)
results['revenue']=round(results['revenue'],2)

print(results)
print("")
print("")


# another way
dfSummary = df.groupby('Product')[['Revenue','Quantity']].sum().reset_index()
print(dfSummary)
print("")
print("")
