from flask import Flask, render_template, request,url_for
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model_filename = "RFmodel.pkl"
model = pickle.load(open(model_filename, 'rb'))

@app.route('/',methods=['GET'])
def hello():
    return render_template('homepage.html')

@app.route('/calc_price',methods=['POST'])
def calc_price():
    if request.method == "POST":
        yrs_old = int(request.form['car_age'])
        Present_Price = float(request.form['ori_price'])
        Kms_Driven = int(request.form['kms_driven'])
        Owner = request.form['owner_type']
        if (Owner == "First hand"):
            Owner = 0
        elif (Owner == "Second_hand"):
            Owner = 1
        else:
            Owner = 3
        Fuel_Type_Petrol = request.form['fuel_type']
        if (Fuel_Type_Petrol == "Petrol"):
            Fuel_Type_Petrol = 1
        else:
            Fuel_Type_Petrol = 0
        Seller_Type_Individual = request.form['seller_type']
        if (Seller_Type_Individual == "Individual"):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0
        Transmission_Manual = request.form['seller_type']
        if (Transmission_Manual == "Manual"):
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        prediction=model.predict([[Present_Price,Kms_Driven,Owner,yrs_old,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('result.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',prediction_text="You Can Sell your car for {} Lakhs".format(output))
    else:
        return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
