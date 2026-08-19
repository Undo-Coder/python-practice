from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()

    strdate = now.strftime('%Y/%m/%d %H:%M:%S')

    return render_template("index.html", date=strdate)

if __name__ == '__main__':
    app.run(debug=True)