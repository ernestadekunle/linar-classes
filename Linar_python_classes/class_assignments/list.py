motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#i bought a new harley davidson 
print(motorcycles.index("honda"))
print(f'my new list of motorcysles is \n{motorcycles}')
# then i bought another bmw motorbike 
motorcycles.append('BmW')
print(f'my new list of motorcysles is \n{motorcycles}')
#my favorite bike 
print(f'i love my {motorcycles[3]}')
for bike in motorcycles:
    print(f'i own a  {bike}')

