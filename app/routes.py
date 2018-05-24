from flask import render_template, url_for 
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
   return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/argentina')
def argentina():
    return render_template('argentina.html', title='Argentina')

@app.route('/canada')
def canada():
    return render_template('canada.html', title='Canada')

@app.route('/egypt')
def egypt():
    return render_template('egypt.html', title="Egypt")

@app.route('/france')
def france():
    return render_template('france.html', title='France')

@app.route('/germany')
def germany():
    return render_template('germany.html', title='Germany')

@app.route('/greece')
def greece():
    return render_template('greece.html', title='Greece')

@app.route('/india')
def india():
    return render_template('india.html', title='India')

@app.route('/ireland')
def ireland():
    return render_template('ireland.html', title='Ireland')

@app.route('/italy')
def italy():
    return render_template('italy.html', title='Italy')

@app.route('/netherlands')
def netherlands():
    return render_template('netherlands.html', title='Netherlands')

@app.route('/spain')
def spain():
    return render_template('spain.html', title='Spain')

@app.route('/uk')
def uk():
    return render_template('uk.html', title='UK')

@app.route('/uruguay')
def uruguay():
    return render_template('uruguay.html', title='Uruguay')