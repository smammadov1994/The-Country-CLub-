import datetime
from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = 'false'
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

activities=[]



@app.route('/')
def index():
	return render_template("authentication.html")

@app.route('/dashboard', methods=["POST"])
def dashboard():
	if session.get('activities') is None:	
		session["activities"] = []
	if request.method == "POST":
		name=request.form.get('username')
		activity=request.form.get('activities')
		session["activities"].append(activity)
		date=datetime.date.today()
	if len(activities) ==5:
			session["activities"].pop(0)
	return render_template("dashboard.html", activities=session["activities"], date=date , name=name)
