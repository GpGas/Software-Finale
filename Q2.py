import numpy as np
import matplotlib.pyplot as plt

f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()

appleprices=listItems
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])
x= np.arange (1,253)
y= listItems
print(x)
print(y)
plt.plot (x , y)
