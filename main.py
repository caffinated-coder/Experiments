import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('covid_19_india.csv')
data.head()
print(data)

plt.scatter(data.Deaths, data.Confirmed, s=150, c=data.Confirmed,marker=10 )
plt.grid(100)
plt.title("Covid Mortaility")
plt.xlabel("Number of Death")
plt.ylabel("Deaths confirmed")


plt.show()

