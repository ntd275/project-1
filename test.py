import joblib
import pandas as pd

testset = pd.read_csv("testset.csv")

Xtest = testset[["JPY","SP500"]].values
ytest = testset["Direction"].values


clf = joblib.load("clf.pkl")
ypred = clf.predict(Xtest)

def accuracy_score(test,pred):
    dem = 0
    for i in range(len(test)):
        if pred[i]*test[i] > 0:
            dem = dem+1
    return dem/len(test)

print("Accuracy: %.2f %%" %(100*accuracy_score(ytest, ypred)))