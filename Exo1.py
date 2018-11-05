# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import  pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
dict={'country':names,'drives_right':dr ,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(dict)
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# Print car




#print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars

cars.index=row_labels
# Print cars again
#print(cars)


##########################################


# Import pandas as pd


# Import the cars.csv data: cars

cars_CSV=pd.read_csv("cars.csv", index_col=0)
# Print out cars

#print(cars_CSV)

############################

# Acces data with aquare bracket

  #Select country column
print(cars_CSV["country"])
type(cars_CSV["country"])  # pandas series

print(cars_CSV[["country"]])

brics=pd.read_csv("brics.csv", index_col=0)
print(brics[["country","capital"]])

#select row


print(brics[1:4])
#Advanced method
  #loc(label-based)
  #iloc(integer position based)

  ## Row access
print(brics.loc[["RU","IN","CH"]]) # three rows
  ## Row and column
print(brics.loc[["RU","IN","CH"],['country',"capital"]])

print(brics.loc[:,['country',"capital"]])   # all row and twoo column

  #Row 1
print(brics.iloc[[1,4],[2,3]])
print(brics.iloc[:,[2,3]])






