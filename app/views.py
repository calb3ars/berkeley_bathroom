from flask import render_template, flash, redirect, session, url_for, request, g #function to load template from Flask framework
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/') #map / file
@app.route('/index') #map /index file
@login_required
def index():
	user = g.user
	posts = [
		{
			'author': {'nickname': 'Lost in Dwinelle'},
			'body': 'I can\'t find a restroom in this d*mn place!'
		},
		{
			'author': {'nickname': 'Moaning Myrtle'},
			'body': 'Watch out for the basilisk'
		},
		{
			'author': {'nickname': 'John Doe'},
			'body': 'I like a view when I pee'
		},
		{
			'author': {'nickname': 'This is the Wurster'},
			'body': 'This is actually the best'
		}
	]
	return render_template("index.html",
				title='Let\'s Pee!',
				user=user,
				posts=posts)

@app.route ('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
			session['remember_me'] = form.remember_me.data
			return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

@app.before_request
def before_request():
	g.user = current_user

@oid.after_login
def after_login(resp):
	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.email).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname=nickname, email=resp.email)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/submit_review', methods=['GET', 'POST'])
def review():
        form = ReviewForm()
        if form.validate_on_submit():
                flash('Successfully submitted review')
                return redirect('/index')
        return render_template('submit_review.html', title='Submit a Review', form=form)
        
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
#you can change the URL based on variables
#@app.route('/user/<username>')
#def show_user_profile(username):
	#show user profile for that user
#	return 'User %s' % username

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
	#display post with the given post_id, id = integer
#	return 'Post %d' % post_id
	#why is this %d whereas 'User' was %s?
	#since post_id is an integer, %d deals with integer number formatting
