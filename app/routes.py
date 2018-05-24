from flask import render_template, url_for 
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

def about():
    return render_template('about.html', title='About')

def contact():
    return render_template('contact.html', title='Contact')

def argentina():
    return render_template('argentina.html', title='Argentina')

def canada():
    return render_template('canada.html', title='Canada')

def egypt():
    return render_template('egypt.html', title="Egypt")

def france():
    return render_template('france.html', title='France')

def germany():
    return render_template('germany.html', title='Germany')

def greece():
    return render_template('greece.html', title='Greece')

def india():
    return render_template('india.html', title='India')

def ireland():
    return render_template('ireland.html', title='Ireland')

def italy():
    return render_template('italy.html', title='Italy')

def netherlands():
    return render_template('netherlands.html', title='Netherlands')

def spain():
    return render_template('spain.html', title='Spain')

def uk():
    return render_template('uk.html', title='UK')

def uruguay():
    return render_template('uruguay.html', title='Uruguay')