
from flask import Flask, render_template, request, redirect, url_for, jsonify
from joblib import load
import sys

pipeline = load("text_classification.joblib")
    
# start flask
app = Flask(__name__)

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        return redirect(url_for('/'))
    else:
        return render_template('index.html')


@app.route('/get-sentiment', methods=['POST'])
def predictor():
    if request.method == 'POST':
        user = request.form['search']
        predarr = pipeline.predict([user])
        predarr = predarr[0]
        return predarr

if __name__ == '__main__':
    app.run(debug=True)