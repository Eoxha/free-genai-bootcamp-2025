from flask import Blueprint

activity = Blueprint('activity', __name__)

@activity.route('/activities')
def index():
    return "This is an example activities"