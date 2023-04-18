### Start solution here

import pandas as pd
import os
from geopy import distance # to calculate distance on the surface
from flask import  Flask, render_template, request
from geopy import distance
import  geocoder


app = Flask(__name__)

@app.route('/')
def index():
    filename= "Mobile_Food_Facility_Permit.csv"
    data = pd.read_csv(filename, header=0)
    data.to_html(open('templates/data.html', 'w'))
    data = pd.read_csv(filename)
    return render_template('data.html',name=filename, datae=data.to_html())
   
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        re=result.getlist('key')[0]+" == "+result.getlist('value')[0]
        df1=pd.read_csv("Mobile_Food_Facility_Permit.csv").query(re)
        return render_template('rresult.html',data=df1.to_html())
        
    else:
        return render_template('resultform.html')



@app.route('/product',methods = ['POST', 'GET'])
def query_prod(): 
    if request.method == 'POST':
        result = request.form
        list_pr=result.getlist('productname')   
        product_worth={}
        list_pr = [y for y in (x.strip() for x in request.form['list'].split(',')) if y]
        df2 = pd.DataFrame()
        for product in list_pr:
            re=result.getlist('key')[0]+" == "+product
            df1=pd.read_csv("Mobile_Food_Facility_Permit.csv").query(re)
            df2=df2.append(df1)
        return render_template("productdata.html", data=df2.to_html())
       
    else:
        return render_template("product.html")
@app.route('/location',methods = ['POST', 'GET'])
def query_location(): 
    if request.method == 'POST':  
        result = request.form
        Latitude=result.getlist('Latitude')[0]
        Longitude=result.getlist('Longitude')[0]
        myloc=[]
        if not Latitude or not Longitude :
            myloc=geocoder.ip('me')
            print(myloc.latlng)
            myloc=myloc.latlng
        else:
            myloc.append(Latitude.strip())
            myloc.append(Longitude.strip())
        data = pd.read_csv("Mobile_Food_Facility_Permit.csv")
        data['distance']=0.0
        for index, row in data.iterrows():
            longi=data['Longitude'][index]
            lati= data['Latitude'][index]
            foodtruck_loc=[]
            foodtruck_loc.append(lati)
            foodtruck_loc.append(longi)
            dl=distance.distance(foodtruck_loc, myloc).miles
            data['distance'][index] =dl 
        data=data.sort_values(by=['distance'])
        if data.shape[0]>5:
            data=data.iloc[:5]
        data.to_html(open('templates/udata.html', 'w'))

        return render_template('udata.html') 
        #return render_template("udata.html",  tables=[data.to_html(classes='data')], titles=data.columns.values)
    else:
        return render_template("locationform.html")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
    #app.run(host='0.0.0.0', port=80)




