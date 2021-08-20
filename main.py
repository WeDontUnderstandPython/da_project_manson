#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Mason>
#Group Name: <WeDontUnderstandPython>
#Class: <PN2004Y>
#Date: <16/7/2021>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pyplot for PieChart
import matplotlib.pyplot as plt
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    seaData(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def seaData(df):

 
  df.head()
  countries = [" Brunei Darussalam ", " Indonesia ", " Malaysia ", " Philippines ", " Thailand ", " Viet Nam ", " Myanmar "]
  df2 = df[["Year", "Month"] + countries]
  df3 = df2[(df2["Year"] >= 1998) & (df2["Year"] <= 2008)]
  print(df3)

  visitors = []
  for i in countries:
    sum = 0
    for j in df3.index:
      sum += int(df3.at[j, i])
    visitors.append(sum)
  data = {'Countries': countries, 'Visitors': visitors}
  df4 = pd.DataFrame(data, columns=['Countries','Visitors'])
  sorted_df = df4.sort_values('Visitors', ascending =[0])
  #print(sorted_df)

  print("The Top 3 countries (SEA) of visitors to Singapore from the span of 10 years are: ")
  print("################################")
  print("Period: 1998 to 2008 ")
  print("Region: SEA ")
  print(sorted_df.head(n=3))

  # Pie chart, where the slices will be ordered and plotted counter-clockwise:
  labels = 'Indonesia', 'Malaysia', 'Thailand'
  sizes = [64, 24, 12]
  explode = (0.1, 0.1, 0.1)  

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
          shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

  plt.show()

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('The following dataframe for SEA from 1998 to 2008 are read as follows:')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################