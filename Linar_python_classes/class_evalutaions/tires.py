num_of_tires=int(input('enter the number of tires'))
if num_of_tires == 1 :
    print('this is a wheel barrow ')
elif num_of_tires ==2:
    print('this is a bicycle ')
elif num_of_tires ==3:
    print('this is a tricycle')
elif num_of_tires ==4:
    print('this is a car')
elif  5 <= num_of_tires <= 6 :
    print('this is a truck ')
elif  7 <= num_of_tires <= 12 :
    print('this is a trailer')
elif 12 <= num_of_tires <= 24:
    print('this is a catapilar')
else:
    print('enter a valid value')

