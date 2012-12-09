from flask import Blueprint, render_template

Frontend = Blueprint('frontend', __name__, template_folder='templates')

@Frontend.route('/')
def index():
    return render_template('index.html')

