from app import application
from flask import render_template, redirect, url_for
from app.forms import SignUpForm

@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')

@application.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print("{}\n{}\n{}\n{}\n{}".format(form.name.data, form.email.data,
                                          form.mobile.data, form.newsletter.data, form.country.data))
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)
