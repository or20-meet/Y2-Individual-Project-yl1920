from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"



@app.route("/")
def home():
	return render_template("home.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'GET' :
		return render_template('signup.html')
	elif not(request.form['password'] == request.form['repeat']):
		return render_template('signup.html')
	else:
		name = request.form['name']
		username = request.form['username']
		password = request.form['password']
		add_user(username, name, password)
		return render_template('login.html')

		
@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		password = request.form['password']
		if not(get_user_by_username(username)==None) and get_user_by_username(username).password == password:
			return render_template('user.html', user = get_user_by_username(username))
		else:
			return render_template('login.html')


@app.route("/brouse")
def brouse(user):
	images = get_all_images()
	return render_template("brouse.html", images=images)

@app.route("/user")
def user(user):
	images = images_by_id(id = user.id)
	return render_template("user.html", images = images, current_user = user)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
	if request.method == 'GET' :
		return render_template(upload.html)
	
####################take care of me pls




if __name__ == '__main__':
	app.run(debug=True)