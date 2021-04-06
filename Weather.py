# The weather dataset is a time series data set with per hour information
# About the weather conditions at a particulat lociton.
# It records Temperature, Dwe point Temperature, Relative Humidity,
# Wind Speed, Visibility, Pressure and other Conditions

import pandas as pd
# reading the data
data = pd.read_csv(r"D:\College\Pace University\PACE University SEM 2\Introduction to Coding\Python projects\Data science (weather_dataset)\1. Weather Data.csv")
data

# analyze the data
# in all the files data. (funciton is used because the read me file is stored in data)

data.head()   #this will show the first n number of rows which is 5 by default
data.shape # used to show the number of rows and columns of a data set

data.index

data.columns #to see our column names
data.dtypes # it shows the data type of each column
#this command is used on column(single column only) and can not be applied to all,
# used to show the unique value 
data['Weather'].unique()

#nunique()  total number of unique value on the whole dataframe and a single column 
data.nunique()
print(data.nunique)
#count shows the total number of not null value on both (whole data and column)
data.count()
print(data.count)
#value_counts it shows all the unique values with their count. (only for single columns)
data['Weather'].value_counts()

#info() provides basic info about the dataframe
data.info()
print(data.info)
print('\t\t\t\t\t\t\t\t\t just showing 2 values')
#  find all the unique windspeed value in the data
data.head(2) # just showing 2 records
print(data.head(2))
data.nunique()  # to show the unique value

nunique_windspeed= data['Wind Speed_km/h'].nunique()

print('number of unique vaues in the wind speed column:\t', nunique_windspeed)

data['Wind Speed_km/h'].unique() #it shows all the unique values in the windspeed column
#                                   and the total number is 34
print('All the unique value in the wind speed column:\t', data['Wind Speed_km/h'].unique())


print('part 2 to filter hte weather: when weather is clear')
#find the number of times when the weather is clear (method is i think flitering)

data.head(2)
print(data.head(2))

# there are 3 ways to do this 
# 1st is value count 
weather_count=data.Weather.value_counts()
print('count of weather column:\t', weather_count)


# 2nd is flitering

data.head(2)
print(data.head(2))
data[data.Weather =='Clear']  # change the (clear) according to the filter criteria
print('\n')
print('\t\t\tFiltering using ***CLEAR*** conditio: ')
print('\n')
print(data[data.Weather=='Clear'])


print('\n')
print('\t\t\tUsing Groupby: ')
print('\n')
# 3rd using groupby command 
data.head(2)
print(data.head(2))

clear_weather =data.groupby('Weather').get_group('Clear') #get_group is used to pick a particular 
                                    # a particular element from the column('Clear')
print('\t\t\t\tClear weather using GROUPBY')
print(clear_weather)

# number of times when the wind speed was exactly 4km/h
data.head(2)
print(data.head(2))

data[data['Wind Speed_km/h']==4]

print(data[data['Wind Speed_km/h']==4])

#find out the null values
#there are 2 ways (isnull)
data.isnull().sum()
print(data.isnull().sum())

#second is using not null
data.notnull().sum()
print(data.notnull().sum())

#rename the column "WEATHER" of the dataframe to WEATHER CONDITION
data.rename(columns={'Weather':'Weather Conditions'}, inplace=True)
print(data.rename(columns={'Weather':'Weather Conditions'},inplace=True))

#to find mean visibility
data.head(2)
print(data.head(2))
data.Visibility_km.mean()
print(data.Visibility_km.mean())

#standard deviation of "PRESSURE COLUMN"
data.Press_kPa.std()
print(data.Press_kPa.std())

#what is the variance of relative humidity
#if there is space between the words in the data set for example"press_kPa"
#and "Rel Hum_%"" we use data[] when there is a space and use data.press_kPa() when theres no space

data['Rel Hum_%'].var()
print(data['Rel Hum_%'].var())

#find all the instances when snow was recorded.
# there are 3 ways

#1 Value_ count()
data['Weather Conditions'].value_counts()
print(data['Weather Conditions'].value_counts())

#2 is filtering
data[data['Weather Conditions']=='Snow']
print(data[data['Weather Conditions']=='Snow'])

#3 is str.contains   #anything that contains word "SNOW"
data[data['Weather Conditions'].str.contains('Snow')]
print(data[data['Weather Conditions'].str.contains('Snow')])


# all the instances when wind speed is above 24 and visibility is 25
#data[(data['Wind Speed_km/h']>24) and (data['Visibility_km']==25)]
#print(data[(data['Wind Speed_km/h']>24) and (data['Visibility_km']==25)])

#what is the mean vaue of each column against the weather condition

data.head(2)
print(data.head(2))
data.groupby('Weather Conditions').mean()
print(data.groupby('Weather Conditions').mean())
# mean value of each column against each unique value of weather column is shown in the output


#what is the minimim and maximum value of each column against each weather condition
#we will use groupby here as well because it is asking to compare in respect to weather condition

data.groupby('Weather Conditions').min()
print(data.groupby('Weather Conditions').min())
data.groupby('Weather Conditions').max()
print(data.groupby('Weather Conditions').max())


#show all the records where weather condition is FOG

data[data['Weather Conditions']=='Fog']
print(data[data['Weather Conditions']=='Fog'])


# all the instances where weather is clear or visibility is above 40

data[(data['Weather Conditions']=='Clear')| (data['Visibility_km']>40)].tail(50)
print(data[(data['Weather Conditions']=='Clear') | (data['Visibility_km']>40)].tail(50)) # | is or here

#find all the instances where weather is clear, relative humidity is greater than 50 or visibility is above 40
data[(data['Weather Conditions']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]

print(data[(data['Weather Conditions']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)])
