import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv(r'C:\Users\Saravanan\Documents\kaggle_projects\Car Project\car_project\data.csv')
yrs_old = int(2020) - data['Year']
data['yrs_old'] = yrs_old
y = data['Selling_Price']
data.drop(['Car_Name','Year'],inplace=True,axis=1)

final_df = pd.get_dummies(data,drop_first=True)
final_df.drop(['Fuel_Type_Diesel','Selling_Price'],inplace=True,axis=1)
x = final_df
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2,random_state=123)

from sklearn.ensemble import RandomForestRegressor
RFmodel = RandomForestRegressor()
RFmodel.fit(x_train,y_train)
y_pred = RFmodel.predict(x_test)

from sklearn.metrics import r2_score
print("Accuracy: ", r2_score(y_pred, y_test))

file = open('RFmodel.pkl','wb')
pickle.dump(RFmodel,file)
