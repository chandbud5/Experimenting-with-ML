import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:\Datasets\Corona\owid-covid-data.csv")
dfw = df.loc[df['location']=='World']

dt = dfw['date'].values
y = dfw['total_cases'].values
plt.plot(dt,y,'r--')
plt.xticks(np.arange(0, 138, 10), rotation=90)
plt.title("Total cases in World")
plt.savefig("Total-cases-in-World.png",dpi=450)
plt.show()

plt.plot(dfw['date'], dfw['new_cases'], '--')
plt.xticks(np.arange(0, 138, 10), rotation=90)
plt.title("New cases in World")
plt.savefig("New-cases-in-World.png",dpi=450)
plt.show()

dfi = df.loc[df['location']=="India"]
plt.plot(dfi['date'], dfi['total_cases'],'--')
plt.xticks(np.arange(0, 138, 10), rotation=90)
plt.title("Total cases in India")
plt.savefig("Total-cases-in-India.png",dpi=450)
plt.show()

plt.plot(dfi['date'], dfi['new_cases'], '--')
plt.xticks(np.arange(0, 138, 10), rotation=90)
plt.title("New cases in India")
plt.savefig("New-cases-in-India.png",dpi=450)
plt.show()