from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods = ['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])

    predicted_value = round(prediction[0], 3)
    return render_template('index.html', predicted_value = f'Profit will be: ₹{predicted_value}')


@app.route('/api/profit/', methods = ['POST'])
def profit_api():
    data = request.get_json(force = True)
    inputs = [list(data.values())]
    prediction = model.predict(inputs)
    predicted_value = round(prediction[0], 3)
    return jsonify(predicted_value)


if __name__ == '__main__':

    app.run(debug = True)