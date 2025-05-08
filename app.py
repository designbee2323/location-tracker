from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("locations.txt", "a") as file:
        file.write(f"Time: {time}, Latitude: {lat}, Longitude: {lon}\n")

    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)