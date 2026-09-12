# import pandas as pd

# df = pd.read_csv("Pandas/student.csv")



# fibo nachi sereis..

# fibo 1 1 2 3 5 8

def fibo(nn):
    if nn == 1:
        return 
    return fibo(nn) + fibo(nn - 1)
print(fibo(44))