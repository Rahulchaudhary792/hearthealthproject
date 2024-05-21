from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS
app=Flask(__name__)
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
	print(f"Received data: {data}")
	return jsonify(data), 201
if __name__ == "__main__":
	app.run(debug=True)