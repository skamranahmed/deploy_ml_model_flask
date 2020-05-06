from flask import Flask, render_template, jsonify, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/)
def index():
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def predict():
    #   storing the values received from the form as an array in the inputs variable
    inputs = [float(x) for x in request.form.values()]

    #   predicting the values. Note that we are passing a 2D array in the model.predict method.
    prediction = model.predict([inputs])

    predicted_value = round(prediction[0], 3)
    return render_template('index.html', predicted_value=f'Profit will be: ₹{predicted_value}')


@app.route('/api/profit/', methods=['POST'])
def profit_api():
    #   retrieving the data got from the api call
    data = request.get_json(force=True)

    #   storing those values as a 2D array object in the inputs variable
    inputs = [list(data.values())]

    #   predicting the values. Note that we are passing a 2D array in the model.predict method.
    prediction = model.predict(inputs)

    predicted_value = round(prediction[0], 3)
    return jsonify(predicted_value)


if __name__ == '__main__':
    app.run(debug=True)