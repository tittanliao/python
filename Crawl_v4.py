import pandas as pd
import pickle

sStockId = '2344'
sCSVFilePath = '../../Data/' + sStockId + '_Final.csv'
sModelFilePath = '../../Data/lin_r_model.pickle'
df = pd.read_csv(sCSVFilePath)
df.sort_index(ascending=False).head()

def regData(x,iCount):
    for i, row in x.iterrows():
        x.loc[i, '成交股數'] = row['成交股數'].replace(',', '')
        x.loc[i, '成交筆數'] = row['成交筆數'].replace(',', '')
    for i, row in X.iterrows():
        if i <= len(X)-2:
            x.loc[i, '成交股數'] = int(x.loc[i+1, '成交股數'])/int(x.loc[i, '成交股數'])
            x.loc[i, '成交筆數'] = int(x.loc[i+1, '成交筆數'])/int(x.loc[i, '成交筆數'])
            x.loc[i, '美元／新台幣'] = x.loc[i+1, '美元／新台幣']/x.loc[i, '美元／新台幣']
    return x.head(iCount-1)
 
def linReg(y):
    y.drop(0, axis=0, inplace=True)
    y = y.reset_index(drop=True)
    return y
iCount = len(df)
X = df[['成交股數', '成交筆數', '美元／新台幣']].head(iCount)
X = regData(X,iCount)
y = linReg(df[['收盤價']].head(iCount))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

from sklearn.linear_model import LinearRegression
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

intercept = regression_model.intercept_[0]
predictions = regression_model.predict(X_test)
regression_model.score(X_test, y_test)

with open(sModelFilePath, 'wb') as f:
    pickle.dump(regression_model, f)


for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))
print("The intercept for our model is {}".format(intercept))
print(predictions)