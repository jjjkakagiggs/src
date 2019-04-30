from flask import Flask


app = Flask('src')
app.config['SECRET_KEY'] = "dfdfdffdad"
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from src import views