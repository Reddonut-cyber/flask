from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        #Get user inputs
        x_from = float(request.form.get('x_from'))
        x_to = float(request.form.get('x_to'))
        function = request.form.get('function')
        color = request.form.get('color')
        
        #Create x values
        x_values = np.linspace(x_from, x_to, 500)
        
        if function == 'sin':
            y_values = np.sin(x_values)
        elif function == 'cos':
            y_values = np.cos(x_values)
        elif function == 'x^2':
            y_values = x_values**2
        elif function == 'sqrt(x)':
            y_values = np.sqrt(x_values)
        else:
            y_values = x_values
            
        #Plot the funcion
        
        