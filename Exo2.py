# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
print(np.logical_and(my_house < your_house,my_house >= 18))
print(np.logical_not(my_house < your_house,my_house >= 18))
print(np.logical_or(my_house < your_house,my_house >= 18))
print(np.logical_xor(my_house < your_house,my_house >= 18))

############### Filter pandas dataframe
import pandas as pd
brics=pd.read_csv("brics.csv", index_col=0)
print(brics[brics["area"]>8])
print(brics[np.logical_and(brics["area"]>8,brics["area"]<10)])

## LOOP à faire intermediate Python


