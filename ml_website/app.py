from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the model and LabelEncoder
model = pickle.load(open('model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    val1 = float(request.form['val1'])
    val2 = float(request.form['val2'])
    val3 = float(request.form['val3'])
    val4 = float(request.form['val4'])
    val5 = float(request.form['val5'])

    input_data = np.array([[val1, val2, val3, val4, val5]])
    encoded_prediction = model.predict(input_data)
    failure_type_mapping = {
    0: 'Heat Dissipation Failure',
    1: 'No Failure ',
    2: 'Overstrain Failure',
    3: 'Power Failure',
    4: 'Random Failure',
    5: 'Tool wear Failure'
}

    decoded_prediction = failure_type_mapping[encoded_prediction[0]]

    return render_template('result.html', prediction=decoded_prediction)


if __name__ == '__main__':
    app.run(debug=True)
