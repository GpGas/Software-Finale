import numpy as np

f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()

appleprices=listItems
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])

print ("The Mean of the prices is" , np.mean(listItems) ,"\n" , "The Standard deviation of the prices is" , np.std(listItems))

print("Rounded the mean is" , (round(np.mean(listItems))) ,"\n" ,"Rounded Standard deviation" , (round(np.std(listItems))))
