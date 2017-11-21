from flask import render_template, url_for, redirect, request
from forms import *
from app import app

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
            return redirect(url_for('dashboard'))

        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = AddEventForm()
    if request.method == 'POST':
        form = AddEventForm(request.form)
        if form.validate_on_submit():
            name = form.name.data
            category = form.category.data
            location = form.location.data
            date = form.date.data
            description = form.description.data
        return render_template('dashboard.html', form=form)
    return render_template('dashboard.html', form=form)

@app.route('/myevent')
def myevent():
    form = AddEventForm()
    return render_template('myevent.html', form=form)

@app.route('/editevent', methods=['POST'])
def editevent():
    form = EditEventForm(request.form)
    if form.validate():
        name = form.name.data
        category = form.category.data
        location = form.location.data
        date = form.date.data
        description = form.description.data            
    return render_template('myevent.html', form=form)

@app.route('/deleteevent', methods=['POST'])
def deleteevent():
    form = DeleteEventForm(request.form)
    if form.validate:
        name = form.name.data
        location = form.location.data
        description = form.description.data
    return redirect(url_for('myevent'))

@app.route('/otherevents')
def otherevents():
    return render_template('otherevents.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))
