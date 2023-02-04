def sumfunction (value1, value2 ):
    total = int(value1)+int(value2)
    print('your total is ' + str (total) + '\n thank you ')

#sumfunction(34,54)

def greetings(name,department):
    print('good day ' + name + '.')
    print('welcome to the department of ' + department)


#greetings('segun ','linar')

def classupdate(day,date,time):
    '''a function tht prints class updates by taking 
    3 parameters (day,date,time)
    day in format string 
    date in format dd-mm-yyyy
    time in format hhmm 
    '''
    print('hello guys \n schedule for next class follows ')
    print('time :' + str(time))
    print('date :' + str(date)+ 'tomorrow ')
    print('please be punctual as the next class is '+ day)


#classupdate('wednesday','14-12','2:30')


def quickmaths (a,b,c):
    d=int(a)/int(b)
    e=d**int(c)
    print(e)

quickmaths(3,2,4)




