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

	elif not(get_user_by_username(request.form['username'])==None) and get_user_by_username(request.form['username']).password == request.form['password']:
		return render_template('brouse.html')


@app.route("/brouse")
def brouse():
	return render_template("brouse.html")


if __name__ == '__main__':
	app.run(debug=True)