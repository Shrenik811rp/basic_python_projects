from numpy import median
import pandas as pd
import seaborn as sns
#giving names to the columns of the dataset
cols = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration', 'Model Year','Origin']

#read data from the file
#give the name of the columns from the cols array
# the na values are all the values with ? mark
# all the data after "\t" should be ignored
#skipinitialspace=True -> remove the initial space of data
data_frame = pd.read_csv("auto-mpg.data",names=cols,na_values="?",comment='\t',sep=" ",skipinitialspace=True)

#copy the dataframe into data variable
data = data_frame.copy()

#print the first 5 rows of dataframe 
print("\nINFO IN DATASET : \n")
print(data.head(5))

#gives details of the data in the dataset
print("\nDATA INFO: \n")
print(data.info())

#check if there are any null values
print("\n NUMBER OF NULL VALUES IN THE DATASET: \n")
print(data.isnull().sum())
print("\n CHECK FOR NULL VALUES IN THE DATASET: \n")
print(data.isnull().any())

print("\n STATISTICAL DATA ABOUT DATASET: \n")
print(data.describe())


#to fill na values in horsepower column we fill it with median values

median_hrspw = data["Horsepower"].median()
#fillna->fill the na values with median horsepower values
data["Horsepower"] = data["Horsepower"].fillna(median_hrspw)

#New data info()
#check if there are any null values
print("\n New NUMBER OF NULL VALUES IN THE DATASET: \n")
print(data.isnull().sum())
print("\n New CHECK FOR NULL VALUES IN THE DATASET: \n")
print(data.isnull().any())

#print number of unique values of types of cylinder counts in dataset
print("\nNumber of different cylinders of each type:\n")
print(data["Cylinders"].value_counts())

#print percentage of unique values of types of cylinder counts in dataset
print("\nPercentage distrbution of cylinder types:\n")
print("51%' of vehicles have 4 cylinders...")
print("25%' of vehicles have 8 cylinders...")
print(round(100*(data["Cylinders"].value_counts()/ len(data)),2))


#print number of unique values of types of Origin counts in dataset
print("\nNumber of different values with their Origins\n")
print(data["Origin"].value_counts())

#print percentage distribution of unique values of types of Origin counts in dataset
print("\nPercentage distrbution of Origin types:\n")
print(round(100*(data["Origin"].value_counts()/ len(data)),2))


















