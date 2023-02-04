#mfrom cmath import sqrt


a=int(input('enter value for a '))
b=int(input('enter value for b '))
c=int(input('enter value for c '))
b_sqr=b**2
ac_4=4*a*c
A_2=2*a
b_4ac=b_sqr-ac_4
sqrt_b_4ac=sqrt(b_4ac)
bcal=-1*b
x_postive=bcal+sqrt_b_4ac
x_negative=bcal-sqrt_b_4ac
finai_x_postitve=x_postive/A_2
final_x_negtive=x_negative/A_2
print(finai_x_postitve)
print(final_x_negtive)
