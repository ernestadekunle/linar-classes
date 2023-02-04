def greeetings(name = input("Your are welcome here\nWhat\'s your name please ?\n\n")):
    print(f'\nONCE AGAIN, YOU ARE WELCOME {name.upper()}\n')
    print('This software helps you calculate your salary in the next three year and six years. Kindly answer the questions below.')
    sector = input("Do you work in the Government Sector? (respond with Y or N)\n")
    present_salary = int(input('What\'s your present salary?\nInput the figure only!\n'))  

    if sector.lower() == 'y':
        gov_levels(present_salary)
    elif sector.lower() == 'n':
        pri_levels(present_salary)
    else:
        print("Kindly respond with y for YES or n for NO ")


def gov_levels(present_salary):
    level1s = present_salary * 0.30
    level2s = present_salary * 0.60
    print(f'Your salary in the next three (3) years is {level1s + present_salary}')
    print(f'Your salary in the next six (6) years is {level2s  + present_salary}')
    # return f'Your salary in the next three years is {level1s*0.30}'

def pri_levels(present_salary):
    level1s = present_salary * 0.25
    level2s = present_salary * 0.50
    print(f'Your salary in the next three (3) years is {level1s  + present_salary}')
    print(f'Your salary in the next six (6) years is {level2s  + present_salary}')
    # return f'Your salary in the next three years is {level1s*0.30}'

greeetings()