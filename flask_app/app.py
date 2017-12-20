from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
 
def index():
  return render_template('home.html')
@app.route('/add', methods=['post'])
def add():
   return render_template('home.html', message = "Hi   "+ request.form['username'] + "    have a nice day")
    
 


if __name__== '__main__':
  app.run(debug=True)
