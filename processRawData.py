
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataN225 = pd.read_csv("./RawData/N225.csv")
dataSP500 = pd.read_csv("./RawData/GSPC.csv")
dataJPY = pd.read_csv("./RawData/USD-JPY.csv")




direction = []
N225 = []

i = 1
while i < dataN225["Close"].count():
    N225.append(np.log(dataN225["Close"][i]/dataN225["Close"][i-1]))
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


out = {"SP500":SP500[0:639],"JPY":JPY[0:639],"Direction":direction[0:639]}
df = pd.DataFrame(out)

df.to_csv("tranningset.csv",index=False)

out = {"SP500":SP500[640:675],"JPY":JPY[640:675],"Direction":direction[640:675]}
df = pd.DataFrame(out)
df.to_csv("testset.csv",index=False)

plt.title("Preview")
plt.plot(SP500[0:70],"r",label="S&P 500 Index")
plt.plot(JPY[0:70],"g",linestyle="dashed",label="JPY/USD")
plt.plot(N225[0:70],"b",label="NIKKEI 225 Index")

plt.legend()
plt.show()