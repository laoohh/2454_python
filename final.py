#1
import pandas as pd

# The data file path and file name need to be configured.
PATH = "C:/OneDrive_old/OneDrive/BCIT/2454 Python/DataSet/"
CSV_DATA = "oil.csv"

# Note this has a comma separator.

df = pd.read_csv(PATH + CSV_DATA)
print(df)

newData = { 'Day': 3,
            'Future': 'Brent Crude',
            'Close': 36.33}
df = df.append(newData, ignore_index=True)
print("")
print(df)

dfStat = df.groupby('Future')['Close'].mean().round(2).reset_index()
print("")
print(dfStat)


#3
class Province:
    provinceName = ''
    countryName = ''
    population = 0

    def __init__(self, provinceName, countryName, population ):
        self.provinceName = provinceName
        self.countryName = countryName
        self.population = population

    def displayInformation(self):
        print('Province Name: ', self.provinceName)
        print('Country Name : ', self.countryName)
        print('Population   : ', str(self.population))
        print('------------------------------')


NY = Province('NY', 'USA', 9000000)
provinceList = [NY]
BC = Province('BC', 'Canada', 5000000)
provinceList.append(BC)
CA = Province('CA', 'USA', 11000000)
provinceList.append(CA)

for province in provinceList:
    province.displayInformation()



#4
if (not not True and not True):
    print('True')
else:
    print('False')


#11

i = 1
i += 2
t = 0
for i in range(i, 30):
    print(i)
    t += 1
print('t=',str(t))

