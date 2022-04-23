from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html',prediction_text='Please Enter the exchange rate for SGD')

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    inp  = request.form.get("sgdValue")
    if inp != "":
        prediction = model.predict([[inp]])
        output = prediction[0]
        return render_template('index.html', prediction_text='The Predict DBS share Price is {}'.format(output))
    else:
        return render_template('index.html', prediction_text='Please Enter the exchange rate for SGD')

if __name__ == "__main__":
    app.run(debug=True)