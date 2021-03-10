from flask import Flask, redirect, url_for, render_template, request
from rock_paper_scissors import *

app = Flask(__name__)

@app.route("/")
def index():
	return redirect(url_for('game'))

@app.route("/game/")
def game():
	return render_template("rock_scissors_paper.html")

@app.route("/decision", methods=['GET', 'POST'])
def decision():
	if request.method == 'POST':
		user_choice = request.form['subject']
		comp_choice = random.choice(options)
		return rules(user_choice,comp_choice)
	return redirect(url_for('game'))
		

@app.route("/hi/")
def who():
	return "Who are you?"


@app.route("/hi/<username>")
def greet(username):
	return f"Hi there, {username}!"
