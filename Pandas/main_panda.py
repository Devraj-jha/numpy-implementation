import pandas as pd

df = pd.read_csv("Pandas/student.csv")

#seris = one column of data.
#index based.

print(df)

ages = pd.Series([20,21,19,25])

print(ages[0])

## data frame  it is a table.


dfF = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 25, 22],
    "city": ["Delhi", "Mumbai", "Delhi"]
})

## with a proper table 

print(dfF)

print(dfF.index)


## differnt methods.
# method of insptect the top of head.

# method of inspect the bottom. 

# method to inspect the shape.

# method to get a column

print(df.info())