'''student_1= {'name':'esther', 'complexion': 'fair' , 'height': '4ft 8" ', 'education ': 'tetiary'}
print(student_1['name'])'''


alien_1= {'color':'green', 'points':5}

new_points= alien_1['points']
print(f'you just earned {new_points} points ! ')
position= alien_1.get('x_position','no value exist')
print(position)

#alien_1.clear()
print(alien_1)

alien_1.popitem()
print(alien_1)
#I am master