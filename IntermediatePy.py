# INTERMEDIATE PYTHON COURSE
import  pandas as pd

dict={"Pays":["Haiti", "Canada","USA"], "Capital":["Port-au-Prince","Ottawa","Washington"]}
brics=pd.DataFrame(dict)

print(brics)

brics.index=["HT","CAN","US"]
print(brics)

brics1=pd.read_csv("brics.csv")

#print(brics1)

#sinon la premiere ne pas reconnu comme index
brics1=pd.read_csv("brics.csv", index_col=0)

print(brics1)



