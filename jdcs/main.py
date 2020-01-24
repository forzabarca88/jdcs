from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import jdcs.config as config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# this import depends on db, so can't be before that assignment
from jdcs.model import Email, Image
from jdcs.ui.main import ui 

migration = Migrate(app, db)

app.register_blueprint(ui, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
