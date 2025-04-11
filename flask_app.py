from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    number = request.form['number']
    message = request.form['message']

    if "free" in message.lower() or "win" in message.lower():
        prediction = "Spam"
        result_class = "spam"
        suggestion = "⚠️ This message looks suspicious. Avoid clicking any links."
    else:
        prediction = "Not Spam"
        result_class = "not_spam"
        suggestion = "✅ This looks like a safe message. Be sure to proceed with caution."

    return render_template(
        'index.html',
        result=True,
        number=number,
        message=message,
        prediction=prediction,
        result_class=result_class,
        suggestion=suggestion
    )

if __name__ == '__main__':
    app.run(debug=True)
