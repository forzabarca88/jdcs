from flask import render_template, Flask, url_for
from utils import placeholder_text, get_all_files_in_dir
import tests.mock_objects as test

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', title="Home Page",
                           description=test.DESC_TEXT_INDEX.text)


@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog Posts",
                           description=test.DESC_TEXT_BLOG.text)


@app.route('/data')
def data():
    return render_template('data.html', title="Data",
                           description=test.DESC_TEXT_DATA.text)


@app.route('/gallery')
def gallery():
    images = get_all_files_in_dir(os_dir_join_args=['static', 'gallery'],
                                  file_filter='.jpg')
    return render_template('gallery.html', title="Gallery", images=images,
                           description=test.DESC_TEXT_GALLERY.text)


@app.route('/about')
def about():
    return render_template('about.html', title="About",
                            description=test.DESC_TEXT_ABOUT.text)


if __name__ == '__main__':
    app.run(debug=True)
