from flask import render_template, Blueprint, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import tests.mock_objects as test
import jdcs.config as config
from jdcs.ui.forms import ContactForm
from jdcs.utils import (
    placeholder_text,
    get_all_files_in_dir,
    contact_admin,
    add_email_to_db
)

ui = Blueprint('ui', __name__)

# this import depends on db, so can't be before that assignment
from jdcs.model import Email, Image


@ui.route('/')
@ui.route('/index.html')
def home():
    return render_template('index.html', title="Home Page",
                           description=test.DESC_TEXT_INDEX.text)


@ui.route('/blog')
def blog():
    return render_template('blog.html', title="Blog Posts",
                           description=test.DESC_TEXT_BLOG.text,
                           posts = test.BLOG_POSTS)


@ui.route('/data')
def data():
    return render_template('data.html', title="Data",
                           description=test.DESC_TEXT_DATA.text)


@ui.route('/gallery')
def gallery():
    images = get_all_files_in_dir(os_dir_join_args=['static', 'gallery'],
                                  file_filter='.jpg')
    return render_template('gallery.html', title="Gallery", images=images,
                           description=test.DESC_TEXT_GALLERY.text)


@ui.route('/about', methods=['GET', 'POST'])
def about():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if add_email_to_db(Email(), form.name, form.email, config.ADMIN_EMAIL_ADDRESS, 
                                'Email from User', form.comment):
                flash(message='Success!', category='success')
                contact_admin(form.email, form.comment)
                return redirect(url_for('ui.about'))
            flash(message='Error saving contact details.', category='error')
        validation_errors = form.name.errors + form.email.errors + form.comment.errors
        total_errors = len(validation_errors)
        list(map(flash, validation_errors, 
                ['error' for i in range(total_errors)]))
    return render_template('about.html', title="About",
                            description=test.DESC_TEXT_ABOUT.text, form=form)
