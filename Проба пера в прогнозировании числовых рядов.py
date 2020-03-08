import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("test.csv", sep=',')
last = df.last_valid_index()

X_train = []
for i in range(last+1):
    p1 = tuple(df.iloc[i])
    X_train.append(p1)
    
print(X_train)
plt.plot(X_train)

i = last+2

while i < (last+4):
    b = 1.4643 * i + 235.14
    an = (b, i)
    X_train.append(an)
    i = i + 1
print(X_train)
    

columns = ("id", "sell")

answ = pd.DataFrame(X_train, columns=columns)
answ.to_csv("test.csv", index=False)
