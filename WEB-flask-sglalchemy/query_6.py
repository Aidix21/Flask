from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

#
надо переписать
#
