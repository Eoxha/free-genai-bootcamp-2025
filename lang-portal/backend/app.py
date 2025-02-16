from flask import Flask, request, abort
from markupsafe import escape

# Blueprint Modules
from activities.activity import activity
from common.dashboard import dashboard
from words.main import words

app = Flask(__name__)

# register modules
app.register_blueprint(dashboard)
app.register_blueprint(activity)
app.register_blueprint(words)