from . import main
# from ..request import get_movies,get_movie,search_movie
# from .forms import ReviewForm, UpdateProfile
from ..models import User
from flask_login import login_required, current_user
from flask import render_template
# from .. import db,photos


# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitches App'

    return render_template('index.html')

    # Getting popular movie
