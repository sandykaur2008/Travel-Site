from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import ContactForm
from app.email import send_email


@app.route('/')
#@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
   return render_template('about.html', title='About')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if app.config['TESTING'] == True:
      recipient = 'test@example.com'
    else: 
      recipient = 'sandykaur2008@gmail.com'
      
    if form.validate_on_submit():
        send_email('My Travels - Feedback', sender='{}'.format(form.email.data),
        recipient=recipient, text_body="""
        From: {} <{}>
        {}
        """.format(form.name.data, form.email.data, form.text.data))
        flash('Thank you for your input, {}!'.format(form.name.data))
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form)


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