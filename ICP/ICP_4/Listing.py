import numpy as np
# GeneratenVector of size 10 * 10 using random function
x = np.random.randint(20, size=(10,10))
# print the generated vector
print("Original Array:")
print(x)
# counter to print the row number
j=0
# loop through each element in x to get max, min values
for i in x:
    # increment j for each row
    j= j +1
    # print row number and min , max values
    print(f"Maximum and  Minimum values in row Number  {j}:")
    # predefined function to get min , max values
    xmin, xmax = i.min(), i.max()
    print(xmin, xmax)




