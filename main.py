x = [1,3,5,7,9]
y = [2,4,6,8,10]

print(type(x))
print(type(y))

import matplotlib.pyplot as plt
plt.plot(x,y,marker=10, c='yellow', s=100)
plt.xlabel('Population')
plt.ylabel('GDP per capita')

plt.show()