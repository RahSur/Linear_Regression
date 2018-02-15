from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x=np.array([1,2,3,5,2,4],dtype=np.float64)
y=np.array([2,1,4,5,3,5],dtype=np.float64)

style.use('fivethirtyeight')
plt.scatter(x,y)
#plt.show()

def function (x,y) :
    m=(((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x)))
    c=mean(y)-m*mean(x)
    return m,c

m,c=function (x,y)
print ('Slope(m) and Y-intercept(c)')
print (m,c)
print('\n')

regression_line=[(m*v)+c for v in x]

style.use('fivethirtyeight')
plt.scatter(x,y,color='b')
plt.plot(x,regression_line)
#plt.show()

predict_x= 3.2
predict_y=(m*predict_x)+c
plt.scatter (predict_x,predict_y,color='r')
print('Predicted output:')
print(predict_y)
plt.show()
