from flask import Flask
import os
from models import db, User
from views import views
from admin import setup_admin 
from flask_migrate import Migrate
from flask_login import LoginManager
from mail_utils import mail

app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='57bb67aa6730e86a4cf106df20059b5e803fe7b22425fdd2f83baf551c61f209'

app.config['SUPABASE_URL'] = os.getenv('URL')
app.config['SUPABASE_KEY'] = os.getenv('KEY')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')


mail.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

setup_admin(app)

app.register_blueprint(views)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)
