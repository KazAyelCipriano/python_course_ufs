import matplotlib.pyplot as plt
import math
import random
t = range(0,1000)
y=[];x=[]
for tt in t: 
    x.append(tt*0.01)
    y.append(5*math.sin(tt*0.01)+random.random())
plt.plot(x,y)
plt.ylabel('Dados Obtidos')
plt.show()
