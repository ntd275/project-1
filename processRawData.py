
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataN225 = pd.read_csv("./RawData/N225.csv")
dataSP500 = pd.read_csv("./RawData/GSPC.csv")
dataJPY = pd.read_csv("./RawData/USD-JPY.csv")




direction = []

i = 1
while i < dataN225["Close"].count():
    if dataN225["Close"][i] > dataN225["Close"][i-1]:
        direction.append(1)
    else:
        direction.append(-1)
    i = i + 1

SP500 = []
i = 1
while i < dataSP500["Close"].count():
    SP500.append(np.log(dataSP500["Close"][i]/dataSP500["Close"][i-1]))
    i = i + 1

JPY = []
i = 1
while i < dataJPY["JPY/USD"].count():
    JPY.append(np.log(dataJPY["JPY/USD"][i]/dataJPY["JPY/USD"][i-1]))
    i = i + 1

out = {"SP500":SP500,"JPY":JPY,"Direction":direction}
df = pd.DataFrame(out)

df.to_csv("data.csv",index=False)


#plt.plot(df[df["Direction"] == 1]["SP500"],df[df["Direction"] == 1]["JPY"],"go")
#plt.plot(df[df["Direction"] == -1]["SP500"],df[df["Direction"] == -1]["JPY"],"ro")

#plt.show()