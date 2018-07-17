# import numpy library to perform mathematical calculations
import numpy as np
import matplotlib.pyplot as plt
# array of values in to x
x=np.array([0,1,2,3,4,5,6,7,8,9])
# load array of values to y
y=np.array([1,3,2,5,7,8,8,9,10,12])
# calculate mean of x
meanx=np.mean(x)
# calculate mean of y
meany=np.mean(y)
# calculate variance
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
# calculate slope
slope=num/den
# calculate intercept
intercept=meany-(slope*meanx)
# print slope and intercept
print("slope",slope)
print("intercept",intercept)
# substitute values in the below equation
val=(slope*x)+intercept
# plot x,y values
plt.plot(x,y)
# plot x and equation values
plt.plot(x,val)
# show it on the graph
plt.show()
