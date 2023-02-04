'''password= input('enter password ')
message = 'very strong '
special_char= ['@','#','!','+','$','&']
lenth= len(password)
invalid=False


for char in password:
    if char not in special_char:
        print ('weak password ')
        invalid=True
        break
if not invalid:
    print('valid')'''

special_chars =  ['$', '&', '!']
special_chars.append('@')

password = input("Provide your password: ")    
invalid = False

for char in password:
    if char not in special_chars:
        print('Invalid char found! Use only: {}'.format(special_chars))
        invalid = True
        break

for char in password:
    if char in special_chars:
        print('valid ')
        break


        
