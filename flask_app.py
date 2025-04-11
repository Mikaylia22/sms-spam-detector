from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model/rf_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/CountVector.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        data = pd.Series([message])
        transformed = vectorizer.transform(data)
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            result = 'Spam Message Detected!'
            result_class = 'spam'
            suggestion = '⚠️ Be cautious! This may be a spam or phishing message.'
        else:
            result = 'Not a Spam Message!'
            result_class = 'ham'
            suggestion = '✅ This looks like a safe message.'

        return render_template('index.html',
                               number=number,
                               message=message,
                               prediction=result,
                               result_class=result_class,
                               suggestion=suggestion,
                               result=True)
    return render_template('index.html', result=False)

if __name__ == '__main__':
    app.run(debug=True)
