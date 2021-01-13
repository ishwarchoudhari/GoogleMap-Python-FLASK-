from flask import Flask, render_template,redirect,request,url_for,jsonify
from flask_googlemaps import GoogleMaps
import cgi
form = cgi.FieldStorage()

app = Flask(__name__)
GoogleMaps(app, key="'Add Your Key here'")

@app.route('/getdata',methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        Latitude =request.form['Latitude']
        Longitude =request.form['Longitude']
        print("Longitude:",Latitude)
        print("Latitude :",Longitude)
        return redirect(url_for('Map2', Latitude=Latitude,Longitude=Longitude))
    return render_template('Map2.html')

@app.route('/Map2')
def Map2():
    Latitude= request.args.get('Latitude', None)
    Longitude = request.args.get('Longitude', None)
    return render_template('Map2.html', Latitude=Latitude, Longitude=Longitude)

@app.route('/', methods=["GET"])
def my_map():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
