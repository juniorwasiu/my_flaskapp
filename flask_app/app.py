from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
 
def index():
  return render_template('layout.html')
@app.route('/add', methods=['post'])
def add():
   if request.form['username']== "" :
       return render_template('layout.html', message = "enter your name above in the input-filed")
   else: 
       return render_template('layout.html', message = "Hi   "+ request.form['username'] + "    have a nice day")
    
 


if __name__== '__main__':
  app.run(debug=True)
