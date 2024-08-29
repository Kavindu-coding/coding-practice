from itertools import product

x = int(input())
y = int(input())
z = int(input())
n = int(input())

element = [0,0,0]
array_of_elements = []

x_list = [x_1 for x_1 in range(x+1)]
y_list = [y_1 for y_1 in range(y+1)]
z_list = [z_1 for z_1 in range(z+1)]

for x,y,z in product(x_list,y_list,z_list):
    sum = x+y+z
    if sum<n:
        array_of_elements.append([x,y,z])

print(array_of_elements)





