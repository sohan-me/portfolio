from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import *
from mail_utils import send_contact_email

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        full_name = request.form.get('full-name')
        email = request.form.get('email')
        phone_number = request.form.get('phone-number')
        subject = request.form.get('subject')
        budget = request.form.get('budget')
        message = request.form.get('message')

        if send_contact_email(full_name, email, phone_number, subject, budget, message):
            flash('Message sent successfully!', 'success')
        else:
            flash('Error sending message.', 'danger')
        
        return redirect(url_for('views.index'))

    
    
    profile = Profile.query.first()
    pricings = Pricing.query.all()
    featured_projects = FeaturedProject.query.all()
    educational_experiences = EducationalExperience.query.all()
    specializations = Specialization.query.all()
    advantages = Advantage.query.all()

    return render_template(
        'index.html',
        profile=profile,
        pricings=pricings,
        featured_projects=featured_projects,
        educational_experiences=educational_experiences,
        specializations=specializations,
        advantages=advantages
    )
    


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')