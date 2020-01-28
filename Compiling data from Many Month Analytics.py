#After downloading many csv. files for website click each month,
#This script compiles many month's website click data into a big datasheet.
#If you have a list of website that you are interested in, you can put it into AllURLs.csv. 
#And the program will only pick out the websites that you are interested in.
#Written by Jimmy Zhong (Juntao), zhongj2@carleton.edu, 
#Carleton College, IT Department, DataSquad.

import pandas as pd
import glob
import csv
from pandas import DataFrame

#importing the website list that you want to monitor
AllURLs= pd.read_csv("AllURLs.csv", low_memory=False)
#Converting the website list into a panda dataframe
df = DataFrame(AllURLs, columns= ['All URLs you would like to search for:'])
#csv is, by default, a 2D table, but I want to make csv into a list, which is easier to be manipulated
listURL = df['All URLs you would like to search for:'].values.tolist()

#create a dataframe with data in one csv. file
def onemonth(dataframe):
    thismonth = []
    thismonth1 = pd.DataFrame(thismonth)
    for x in listURL:
        clicknumber = dataframe.loc[dataframe['ga:pagePath'] == x]
        #if the row is empty, then assgin an 0 value to it
        if clicknumber.empty == True:
            clicknumber = {'ga:pagePath': x, 'ga:pageviews': 0}
        else:
            pass
        #appending the row to below
        thismonth1= thismonth1.append(clicknumber, ignore_index=True)
    #change the column name into "PagePath" and "filename" (i is in the for loop below)
    thismonth1.columns =['PagePath', i.replace('C:/Users/Admin Juntao/Desktop/Many Months Google Analytics/data', '')]
    return (thismonth1)


#change into your own directory
path = 'C:/Users/Admin Juntao/Desktop/Many Months Google Analytics/data/*.csv'
#these are all the csv files in the folder
all_files = glob.glob(path)
allmonth = []
for i in all_files:
    monthly = pd.read_csv(i, low_memory=False)
    #monthly is the csv file for each individual month
    monthly1 = pd.DataFrame(monthly)
    try:
        #for the first month, pd.concat[allmonth, justnumber] will return an error
        add=onemonth(monthly1)
        #justnumber get rid of the first column, which is the PagePaths. 
        justnumber = add.iloc[ : , 1 ]
        #pd.concat([left table, right table], axis =1) joins 2 tables horizontally 
        allmonth = pd.concat([allmonth, justnumber], axis=1)
    except:
        #Pagepath only need to appear once on the left. 
        allmonth = onemonth(monthly1)
#printing panda datafram allmonth into csv. 
result_csv = allmonth.to_csv (r'C:/Users/Admin Juntao/Desktop/Many Months Google Analytics/result.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path


#to check variable during the process, do this:
#print(allmonth)
#print(justnumber)