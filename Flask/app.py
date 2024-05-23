from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS
import pickle
app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
CORS(app)
###@app.route("/")
###def welcome():
###	return render_template('index.htm')
###@app.route("/success/<int:score>")
###def success(score):
###	data = [100, 20, 30, 40, 20, 20, 20, 10, 50]
###	return render_template('results.htm', data=data)
###@app.route("/fail/<int:score>")
###def fail(score):
###	return "Failed " + str(score)
###@app.route("/results/<int:marks>")
###def results(marks):
###	return redirect(url_for('success', score=marks))
###@app.route("/submit", methods=["GET", "POST"])
###	
###total_score=0
###	if (request.method == 'POST'):
###		science = float(request.form['science'])
###		maths = float(request.form['maths'])
###		social = float(request.form['social'])
###		total_score = (science + maths + social) / 3
###	return redirect(url_for('success', score=total_score))
@app.route('/submit', methods=['POST'])
def post_data():
	data = request.json
	asymptomatic = 0
	nonanginal = 0
	nontypical = 0
	typical = 0
	fixed = 0
	normal = 0
	reversable = 0
	if (data['chestPain'] == 'asymptomatic'):
		asymptomatic = 1
	elif (data['chestPain'] == 'nonanginal'):
		nonanginal = 1
	elif (data['chestPain'] == 'nontypical'):
		nontypical = 1
	elif (data['chestPain'] == 'typical'):
		typical = 1
	elif (data['chestPain'] == 'fixed'):
		fixed = 1
	elif (data['chestPain'] == 'normal'):
		normal = 1
	elif (data['chestPain'] == 'reversable'):
		reversable = 1
	sugartest = 0
	if (data['sugarTest'] == 'Yes'):
		sugartest = 1
	result = model.predict([[float(data['age']), float(data['bp']), float(data['chol']), sugartest, float(data['hr']), float(data['ca']), asymptomatic, nonanginal, nontypical, typical, fixed, normal, reversable]])
	r = int(result[0])
	res = {'result': r}
	return jsonify(res), 201
if __name__ == "__main__":
	app.run(debug=True)