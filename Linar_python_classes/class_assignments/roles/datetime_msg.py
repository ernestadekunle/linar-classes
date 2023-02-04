import datetime as dt 
import time as tm
import pandas as pd 


# this function determines the  date  of the month i.e (1-31) by converting  
#the date into a string and slicing the string using string indexing
def todays_date_time1():
    today= dt.date.today()
    string_today= str(today)
    sliced_date=string_today[9:11]
    return sliced_date

date_of_the_month= todays_date_time1()
#Texting Github
#nother Testing
 #this function detetmines the the current year by converting  the date 
 # into a string and slicing the year out using string indexing    
def todays_date_time2():
    today= dt.date.today()
    string_today= str(today)
    
    sliced_year= string_today[0:4]
    return sliced_year
current_year_= todays_date_time2()

#this function determines the name of the month by converting the date into a string  and deriving the month number , 
# we then use the 'if' method to assign corresponding month name 
def todays_date_time3():
    today= dt.date.today()
    string_today= str(today)
   # sliced_date=string_today[9:11]
    #sliced_year= string_today[0:5]
    if string_today[-5:-3] == '01' :
        month= 'january'
    elif string_today[-5:-3] =='02':
        month= 'february'
    elif string_today[-5:-3] =='03':
        month= 'march'
    elif string_today[-5:-3] =='04':
        month= 'april'
    elif string_today[-5:-3] =='05':
        month= 'may'
    elif string_today[-5:-3] =='06':
        month= 'june'
    elif string_today[-5:-3] =='07':
        month= 'july'
    elif string_today[-5:-3] =='08':
        month= 'august'
    elif string_today[-5:-3] =='09':
        month= 'september'
    elif string_today[-5:-3] =='10':
        month= 'october'
    elif string_today[-5:-3] =='11':
        month= 'november'
    elif string_today[-5:-3] =='12':
        month= 'December'
    else:
        month= None
    return month
month_name_= todays_date_time3()

    
    

'''this function determines the time of the day by converting the datetime output 
into a string then slicing out the hour of the day ,we then convert the hour into a string and 
proceed to use the 
'if' formula to determine the period of the day i.e (morning , afternoon or evening )'''

def time_of_day():
    time= dt.datetime.now()
    striped_time=str(time)
    sliced_time= striped_time[11:13]
    int_sliced_time= int(sliced_time)
    if 5 <= int_sliced_time <= 12  :
        greetings = 'GOOD MORNING ! '
    elif  12 <= int_sliced_time <=  17:
        greetings= 'GOOD AFTERNOON ! '
    elif  17 <= int_sliced_time <= 23 :
        greetings= 'GOOD EVENING !'
    else :
        greetings= 'Its a new Day'
    return greetings
period_= time_of_day()








    

#2023-02-03 12:00:07.908007 12:14
#this function import csv files from current working folder and iterates the file content using 'for' loop 
#the print function output names and roles from the csv files as a message using the 'f-string' method 
#to insert texts and  corresponding values  
def message():
    for name,role in zip(pd.read_csv(r'namees.csv'),pd.read_csv(r'roles.csv')):        
        print(f'{period_} MR {name.capitalize()} you have been appointed as the {role.upper()} of Linar as at today, {date_of_the_month} of {month_name_} {current_year_} ')


message()