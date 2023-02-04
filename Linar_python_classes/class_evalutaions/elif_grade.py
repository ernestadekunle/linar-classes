'''write a script that determines your grade 
100-70 ---> excellent 
69-60 ----> very good 
59-60 --->good
49-45 --->credits
44-0 -----> fail '''
score = int(input('enter score '))
if 70 <= score <=100 :
    print('excellent')
elif 60 <= score <= 69:
    print('very good ')
elif 50 <= score <= 59:
    print('good')
elif 45 <= score <=49 :
    print('credit')
elif 0 <= score <= 44 :
    print('fail')
