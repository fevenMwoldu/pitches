from . import main
from ..models import User, Pitch, Category, Comment
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for
from .forms import PitchForm, CommentForm, CategoryForm


# from ..models import Pitch, Category
from .. import db

# from .. import db,photos


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Pitches App'

    pitches = Pitch.query.all()
    print(pitches)

    return render_template('index.html', pitches=pitches, title=title)

    # Getting popular movie


@main.route('/AddPitch', methods=["GET", "POST"])
def Addpitch():
    form = PitchForm()
    form1 = CategoryForm()
    if form.validate_on_submit():
        new_pitch = Pitch(content=form.pitch_content.data)
        new_category = Category(category_name=form.choose_category.data)
        new_category.save_category()
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Adding new pitches'
    return render_template('Addpitch.html', PitchForm=form, categoryForm=form1, title=title)


@main.route('/Addcomment', methods=["GET", "POST"])
def Addcomment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(content=form.comment.data)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    title = 'Adding comments'
    return render_template('comment.html', CommentForm=form, title=title)


@main.route('/', methods=["GET", "POST"])
def upvote_count():
    upvote = Pitch.upvotes
    upvote += upvote
    db.session.add(upvote)
    db.session.commit()
    return upvote
    # return render_template('index,html')


@main.route('/', methods=["GET", "POST"])
def downvote_count():
    downvote = Pitch.downvotes
    downvote += downvote
    db.session.add(downvote)
    db.session.commit()
    return downvote
    # return render_template('index.html')
