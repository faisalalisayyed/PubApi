from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/api')
def api():
    return render_template('apidocs.html')

if __name__ == '__main__':
    app.run(debug=True)