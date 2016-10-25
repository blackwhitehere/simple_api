from flask import Flask
from flask import request, session
import datetime



app = Flask(__name__)
app.secret_key = 'F12Zz47j\3yX R~X@H!jmM]Lwf/,?KT'
#http://code.runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python
	
def resetCounter():
	session['counter'] = 0

def incrementCounter():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1

@app.route("/", methods = ["GET", "DELETE"])
def execute():
	def relevant_image(time):
		if time.hour<12:
			return("elephant.jpg/")
		else:
			return("capybara.jpg/")

	time_right_now = datetime.datetime.now()

	if request.method == 'DELETE':
		resetCounter()
		return("Counter reset")
	else:
		image_url = relevant_image(time_right_now)
		incrementCounter()
		counter=session['counter']
		return(str({'url': request.url+image_url, 'counter': counter}))

if __name__ == "__main__":
    app.run(debug=True)
