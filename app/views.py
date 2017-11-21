from flask import render_template, url_for, redirect, request
from forms import *
from app import app
from flask.views import View

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            name = form.name.data
            email = form.email.data
            password = form.password.data
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data

        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/myevent')
def myevent():
    return render_template('myevent.html')

@app.route('/otherevents')
def otherevents():
    return render_template('otherevents.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))
