from flask import Flask, render_template, redirect, request, url_for, send_file
import mysql.connector, joblib
import pandas as pd
import numpy as np
import string
import random
import re

app = Flask(__name__)
app.secret_key = 'thyroid'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database='thyroid'
)

mycursor = mydb.cursor()

def executionquery(query, values):
    mycursor.execute(query, values)
    mydb.commit()
    return

def retrivequery1(query, values):
    mycursor.execute(query, values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data

def is_strong_password(password):
    if (len(password) < 8 or not re.search("[a-z]", password) or
        not re.search("[A-Z]", password) or not re.search("[0-9]", password) or
        not re.search("[!@#$%^&*(),.?\":{}|<>]", password)):
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        
        if not is_strong_password(password):
            return render_template('register.html', message="Password is not strong enough!")
        
        if password == c_password:
            query = "SELECT UPPER(email) FROM users"
            email_data = retrivequery2(query)
            email_data_list = [i[0] for i in email_data]
            
            if email.upper() not in email_data_list:
                query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                values = (name, email, password)
                executionquery(query, values)
                return render_template('login.html', message="Successfully Registered!")
            
            return render_template('register.html', message="This email ID already exists!")
        
        return render_template('register.html', message="Confirm password does not match!")
    
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT email, password FROM users WHERE email = %s"
        values = (email,)
        user_data = retrivequery1(query, values)

        if user_data:
            stored_password = user_data[0][1]
            if password == stored_password:
                global user_email
                user_email = email
                return redirect("/home")
            return render_template('login.html', message="Invalid Password!!")
        return render_template('login.html', message="This email ID does not exist!")
    
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_csv(file)
        df1 = df.head(500)
        return render_template('prediction.html', 
                               data=df1.to_html(classes='table table-striped table-bordered table-hover', index=False), 
                               message="Dataset uploaded successfully!")
    return render_template('prediction.html')

# @app.route('/prediction', methods=['GET', 'POST'])
# def prediction():
#     if request.method == 'POST':
#         TT4 = float(request.form['TT4'])
#         tumor = int(request.form['tumor'])
#         FTI = float(request.form['FTI'])
#         TSH_measured = int(request.form['TSH_measured'])
#         pregnant = int(request.form['pregnant'])
#         TSH = float(request.form['TSH'])
#         query_hyperthyroid = int(request.form['query_hyperthyroid'])
#         T4U = float(request.form['T4U'])
#         on_antithyroid_meds = int(request.form['on_antithyroid_meds'])
#         query_hypothyroid = int(request.form['query_hypothyroid'])

#         model = joblib.load("C:/Users/prana/Desktop/Major_Project_Batch-06/FRONTEND/MODEL/best_ensemble_model .pkl")

#         condition_class = {
#             0: "Subclinical (initial level)", 1: "T3 toxic", 2: "toxic goitre", 3: "secondary toxic", 4: "Subclinical (initial level)",
#             5: "primary hypothyroid", 6: "compensated hypothyroid", 7: "secondary hypothyroid", 8: "Negative"
#         }

#         disorder_class = {0: "hyperthyroid", 1: "hyperthyroid", 2: "hyperthyroid", 3: "hyperthyroid", 4: "hypothyroid", 5: "hypothyroid", 6: "hypothyroid", 7: "hypothyroid", 8: "Negative"}

#         def prediction_func(input_features):
#             input_array = np.array([input_features])
#             prediction = model.predict(input_array)
#             return disorder_class[prediction[0]], condition_class[prediction[0]]
        
#         predicted_disorder, predicted_condition = prediction_func([TT4, tumor, FTI, TSH_measured, pregnant, TSH, query_hyperthyroid, T4U, on_antithyroid_meds, query_hypothyroid])
#         return render_template('prediction.html', predicted_disorder=predicted_disorder, predicted_condition=predicted_condition)
#     return render_template('prediction.html')
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        TT4 = float(request.form['TT4'])
        tumor = int(request.form['tumor'])
        FTI = float(request.form['FTI'])
        TSH_measured = int(request.form['TSH_measured'])
        pregnant = int(request.form['pregnant'])
        query_hyperthyroid = int(request.form['query_hyperthyroid'])
        T4U = float(request.form['T4U'])
        on_antithyroid_meds = int(request.form['on_antithyroid_meds'])
        query_hypothyroid = int(request.form['query_hypothyroid'])

        # Exclude TSH if TSH_measured is 0
        if TSH_measured == 1:
            TSH = float(request.form['TSH'])
        else:
            TSH = 0  # Assign a default value (consider setting it to NaN or mean value if needed)

        model = joblib.load("C:\myProjects\MAJOR PROJECT\Major_Project_Batch-06\FRONTEND\MODEL\best_ensemble_model.pkl")

        condition_class = {
            0: "Subclinical (initial level)", 1: "T3 toxic", 2: "toxic goitre", 3: "secondary toxic", 4: "Subclinical (initial level)",
            5: "primary hypothyroid", 6: "compensated hypothyroid", 7: "secondary hypothyroid", 8: "Negative"
        }

        disorder_class = {
            0: "hyperthyroid", 1: "hyperthyroid", 2: "hyperthyroid", 3: "hyperthyroid", 
            4: "hypothyroid", 5: "hypothyroid", 6: "hypothyroid", 7: "hypothyroid", 8: "Negative"
        }

        def prediction_func(input_features):
            input_array = np.array([input_features])
            prediction = model.predict(input_array)
            return disorder_class[prediction[0]], condition_class[prediction[0]]

        predicted_disorder, predicted_condition = prediction_func(
            [TT4, tumor, TSH_measured,FTI,  pregnant, TSH, query_hyperthyroid, T4U, on_antithyroid_meds, query_hypothyroid]
        )

        return render_template('prediction.html', predicted_disorder=predicted_disorder, predicted_condition=predicted_condition)

    return render_template('prediction.html')


if __name__ == '__main__':
    app.run(debug=True)
