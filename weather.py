from flask import Flask,render_template,request,abort
import json
import urllib.request


app = Flask(__name__)
def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/',methods=['POST','GET'])
def weather():
    api_key = 'your api key'
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'Kerala'
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='+api_key).read()
    except:
        return abort(404)

    list_of_data = json.loads(source)

    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
