from flask import Blueprint, jsonify
#from entities.Words import Words


dashboard = Blueprint('dashboard', __name__)


@dashboard.before_request
def before_request():
    return

@dashboard.after_request
def after_request(response):
    
    return response

@dashboard.route('/')
def index():
    return "test"
'''
 
dashboard
dashboard/study_progress
dashboard/quick_stats

study_activities 
study_activities/id
study_activities/id/study_sessions
words
words/id
groups/
groups/id
groups/id/words

'''