from flask import Flask

app = Flask(__name__)

app.secret_key = 'ham and cheese'

DATABASE = 'users_schema'