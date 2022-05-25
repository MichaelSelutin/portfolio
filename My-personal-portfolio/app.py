import sqlite3

from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/my_work')
def mywork():
	return render_template('mywork.html')


@app.route('/', methods=['GET', 'POST'])
def form():
	if request.method == 'POST':
		try:
			fname = request.form['fname']
			lname = request.form['lname']

			email = request.form['email']
			comment = request.form['comment']
			with sqlite3.connect('database.db') as cur:
				# cur.execute("INSERT INTO details(fname,lname, email, comment) VALUES(%s,%s,%s,%s)",(fname,lname,email,comment))
				cur.execute('''INSERT INTO details (fname,lname, email, comment) VALUES (?, ?, ?, ?)''',(fname, lname, email, comment))
				cur.commit()

			# Close connection
			flash('Your details are submitted, I will contact you soon, Thanks ', 'success')

			return redirect(url_for('index'))
		except Exception as e:
			return (str(e))

		return redirect(url_for('index'))
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
