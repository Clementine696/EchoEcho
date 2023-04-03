from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/voicechanger')
def voicechanger():
    return render_template('voicechanger.html')

if __name__ == '__main__':
    app.run(debug=True)