from flask import Flask
from flask_migrate import Migrate

#import from local modules
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#link migrations
migrate = Migrate(app, db)

db.init_app(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    app.run()