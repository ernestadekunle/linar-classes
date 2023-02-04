def greetings(name =input('You are welcome here\nWhat\'s your name?\n')):
    print('This calculator helps you solve mathematical problem\nThanks for using this calculator')
    print(input('whats the value?\n'))
    '''value format x,y'''
def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
def square_root(x):
    return(x**(1/2))
def power(x,y):
    return(x**y)
def factorial(x):
    if x==0:
        return 1
    return x * factorial(x-1)
def quadratic_equation(a,b,c):
    yale= b*b-4*a*c
    square_root=sqrt(abs(yale))
    if yale>0:
        ans1=(-b+square_root)/(2*a)
        ans2=(-b-square_root)/(2*a)
        return ans1,ans2 
    elif yale==0:
        ans=-b/(2*a)
        return ans
    else:
        return "Imaginary"
print("choose your desired calculator operation!.")
print("1.Add") 
print("2.Subtract")
print("3.Multiply") 
print("4.Divide")
print("5.Square_root")
print("6.Power")
print("7.Factorial")
print("8.Quadratic_equation")

choice=input("Enter your choice below(1/2/3/4/5/6/7/8):\n")

num1=int(input("Enter the first number below:\n"))
num2=int(input("Enter the second number below:\n"))

if choice=='1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice=='5':
    print("square root of",num1,"=", square_root(num1))
elif choice=='6':
    print(num1,"raised to the power of",num2,"=",power(num1,num2))
elif choice=='7':
    print("factorial of",num1,"=",factorial(num1))
elif choice=='8':
    a=int(input("whats the value of a:"))
    b=int(input("whats the value of b:"))
    c=int(input("whats the value of c:"))

    print("The solutions to the equation are:/n", quadratic_equation(a,b,c))

else:
    print("Invalid")    


greetings()






    




