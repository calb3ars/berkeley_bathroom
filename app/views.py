from flask import render_template, flash, redirect #function to load template from Flask framework
from app import app
from .forms import LoginForm, ReviewForm

@app.route('/') #map / file
@app.route('/index') #map /index file
def index():
	user = {'nickname': 'Little Tinkler'} #fake user
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
def login():
	form = LoginForm()
	if form.validate_on_submit():
			flash('Login requested for OpenID="%s", remember_me=%s' %
				(form.openid.data, str(form.remember_me.data)))
			return redirect('/index')
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

@app.route('/submit_review', methods=['GET', 'POST'])
def review():
        form = ReviewForm()
        if form.validate_on_submit():
                flash('Successfully submitted review')
                return redirect('/index')
        return render_template('submit_review.html', title='Submit a Review', form=form)
        

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
