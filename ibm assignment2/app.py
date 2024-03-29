from flask import Flask, render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def blog():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug='true')
