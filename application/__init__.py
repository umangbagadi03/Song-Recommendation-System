import os
from flask import Flask

#create an instance of a flask app and indicating its location
app_path = os.path.dirname(__file__)
app = Flask(__name__, static_folder=app_path+'C:\Users\Umang\OneDrive\Desktop\Python\apps\Spotify-Song-Recommendation\recommendation_app\application\static')
#creating a secret key for security
app.config['SECRET_KEY'] = 'f074425c98f1480d9e200e6dfa8ae988'
#locating the database in our directory
#db_path = os.path.join(os.path.dirname(__file__), 'Kanban.db')
#URI = 'sqlite:///{}'.format(db_path)
#app.config['SQLALCHEMY_DATABASE_URI'] = URI
#db = SQLAlchemy(app)

from application import routes