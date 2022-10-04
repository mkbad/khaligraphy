from flask import Flask, render_template, request, url_for
#from send_mail import send_mail
from datetime import datetime

app = Flask(__name__)

@app.errorhandler(404)
def error_404(e):
    return "<div align='center'><h1>Page not found</h1></div>"


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/booking', methods=['POST', 'GET'])
def booking():
    return render_template("booking.html")


@app.route('/pricing', methods=['POST', 'GET'])
def pricing():
    return render_template("pricing.html")



if __name__ == "__main__":
    app.run(debug=True, port=7000)