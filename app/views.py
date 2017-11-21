from flask import render_template
from app import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/myevent')
def myevent():
    return render_template('myevent.html')

@app.route('/otherevents')
def otherevents():
    return render_template('otherevents.html')