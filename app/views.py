from flask import render_template #function to load template from Flask framework
from app import app

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
