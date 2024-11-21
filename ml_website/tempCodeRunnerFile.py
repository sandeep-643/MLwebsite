from flask import Flask, request, jsonify, render_template
import pickle  
import numpy as np


model = pickle.load(open('model.pkl', 'rb')) 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():

    data = [float(x) for x in request.form.values()]
    features = np.array(data).reshape(1, -1)
    

    prediction = model.predict(features)
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)