from flask import render_template, Flask, url_for
from utils import placeholder_text

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', title="Home Page",
                            description=placeholder_text())

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog Posts")

@app.route('/data')
def data():
    return render_template('data.html', title="Data")

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)