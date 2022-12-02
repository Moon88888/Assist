### Building Url Dynamically 
####Variable Rules And URL Building

import pickle

import numpy as np
import pandas
from flask import Flask, redirect, render_template, request, url_for

model= pickle.load(open('assist.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def man():
   return render_template('home.html')

@app.route('/predict',methods=['POST'])
def home():
    s1 = int(request.form['a'])
    s2 = int(request.form['b'])
    s3 = int(request.form['c'])
    s4 = int(request.form['d'])
    s5 = int(request.form['e'])
    ls2 = [s1,s2,s3,s4,s5]
    print(ls2)
    ls1=[]
    for i in range(1,51):
        ls1.append(i)

    print(ls1)

    '''ls1 = ['1', '2',
        '3', '4', '5',
        '6', '7', '8', '9', '10',
        '11', '12', '13', '14',
        '15', '16', '17', '18',
        '19', '20', '21',
        '22', '23', '24',
        '25', '26', '27', '28',
        '29', '30', '31', '32',
        '33', '34', '35', '36',
        '37', '38', '39', '40',
        '41', '42', '43', '44',
        '45', '46', '47', '48', '49',
        '50']'''
    #print(ls2)
    ls3 = np.zeros(50, dtype = int)
    for i in range(len(ls2)):
        k = ls2[i]
        print(k)
        ls3[k-1]=1
    print(ls3)    
    pred =model.predict([ls3])
    return render_template('after.html',data=pred[0])
    


if __name__=='__main__':
    app.run(debug=True, port=8000)