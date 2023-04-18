# foodtruck
after running python3 app.py click on url provided it will display the csv file data in html
http://localhost:5000/result endpoint will provide a form to filter data with key  pair. for example key can be FacilityType and value can be "Truck" then it will provide data based on that.
http://localhost:5000/product endpoint will allow user to provide list of data to filter for a particular field
http://localhost:5000/location endpoint will allow to provide latitude and longitude to get foodtruck list near to the location. It will cut the list to size 5 to provide only 5 of them. If latitude and longitude is not provided it will find the location of the customer and provide the list of foodtruck of size 5 close to the location
