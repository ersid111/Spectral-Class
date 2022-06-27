from flask import Flask, request, render_template
import numpy as np
import pickle

with open('model.pkl', 'rb')as file:
    mymodel = pickle.load(file)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    Star_color_Blue_white =0
    Star_color_Orange =0
    Star_color_Orange_Red =0
    Star_color_Pale_yellow_orange =0
    Star_color_Red =0
    Star_color_White =0
    Star_color_yellow_white =0
    Star_color_yellowish =0
   
    Temperature = (request.form['Temperature (K)'])
    Luminosity = (request.form['Luminosity(L/Lo)'])
    Radius = (request.form['Radius(R/Ro)'])
    Absolute_magnitude = (request.form['Absolute magnitude (Mv)'])
    Star_type = (request.form['Star type'])

    star_color = int(request.form['Star color'])
    if star_color == 0:
        Star_color_Blue_white = 1
    elif star_color == 1:
        Star_color_Orange = 1
    elif star_color == 2:
        Star_color_Orange_Red = 1
    elif star_color == 3:
        Star_color_Pale_yellow_orange = 1
    elif star_color == 4:
        Star_color_Red = 1
    elif star_color == 5:
        Star_color_White = 1
    elif star_color == 6:
        Star_color_yellow_white = 1
    elif star_color == 7:
        Star_color_yellowish = 1

    output = mymodel.predict([[Temperature, Luminosity, Radius,
                             Absolute_magnitude, Star_type, Star_color_Blue_white, Star_color_Orange, Star_color_Orange_Red,
                              Star_color_Pale_yellow_orange, Star_color_Red, Star_color_White,
                              Star_color_yellow_white, Star_color_yellowish
                              ]])
    return render_template('index.html', predict=output[0])


if __name__ == '__main__':
    app.run(debug=True)
