from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/contact')
def CONTACTUS():
    return render_template('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
