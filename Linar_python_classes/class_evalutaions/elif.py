age= int(input('your age ?'))
if 0 <= age <= 12 :
    print('you are a child ')
elif 13 <= age <= 19:
    print('you are a teenager ')
elif 20 <= age <= 55:
    print('you are an adult')
elif age >= 56:
    print('weldone sir ')
else:
    print('please input a valid digit ')