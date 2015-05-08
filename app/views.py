from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Little Tinkler'}
	return render_template('index.html',
				title='Welcome',
				user=user)


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
