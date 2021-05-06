from . import  main
from flask import render_template, url_for,redirect,request,flash, abort
from ..models import Quote, User, Comment,Subscribe, Blogs
from flask_login import login_required, current_user, UserMixin
from .forms import UpdateProfile, PostForm
from .. import db
from sqlalchemy import desc
from ..request import get_quotes
from ..email import mail_message
@main.route('/')
def home():
    #blogs = Blogs.query.order_by(Blogs.time_created.desc()).all()
    quote = get_quotes()
    user = current_user
    posts = Blogs.query.order_by(Blogs.time_created.asc())

    return render_template('home.html', quote=quote, posts=posts)
   

#function for profile page
@main.route('/user/<uname>')
def profile(uname):
    user = current_user
    user = User.query.filter_by(username = uname)
    
    
    if user is None:
        abort(404)

   

    return render_template("profile/profile.html", user = user)

#view to handle editing profile details
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.name))

    return render_template('profile/update.html',form =form)



@main.route('/new', methods=['GET','POST'])
@login_required
def new():
  form=PostForm()

  if form.validate_on_submit():
    title=form.title.data
    blog_category=form.title.data
    blog_description=form.blog_description.data
    user=current_user
    post=Blogs(title=title, blog_category=blog_category, user=user, blog_description=blog_description)
    post.save_posts()

    subscriberList=Subscribe.query.all()
    subscribers=[]
    for subcriber in subscriberList:
      subscribers.append(subcriber.email)
    for subcriber in subscribers:
      subscriber_mail("New Blog Created!","email/subscribe",subcriber,user=current_user,post=post)

    flash("Post created successfully!")
    return redirect(url_for('main.home'))

  return render_template("new.html", form=form)