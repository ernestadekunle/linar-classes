salutations= ['mr', 'mr', 'mrs', 'mr', 'mr' ]
first_names= ['adekunle','lawrence','adenuga','lasisi','eke']
last_names= ['idris','martins','sewa','rodiat','samson']
middle_name= ['e','i','o','','u']
grades_=['c+', 'b', 'c', 'b', 'b']
scores= ['100','80','50', '80', '80']

for salutation,firstname,lastname,middlename,grade,score in zip(salutations,first_names,last_names,middle_name,grades_,scores,):
    print(f'Hello {salutation.upper()} {lastname.upper()} {firstname.upper()} . {middlename.upper() } , your first semester score is {score} with grade {grade.upper()} . ')