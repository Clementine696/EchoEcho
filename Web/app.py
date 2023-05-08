from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# con = sqlite3.connect("Audio_DB.db")

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

POSTS = ['hello world', 'how are you', 'you good fam']

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/Soundpad')
def voicechanger():
    return render_template('Soundpad.html',posts = POSTS )

# @app.route('/voicechanger')
# def addAudio():
#     return render_template('voicechanger.html')

@app.route('/modal')
def modal():
    return render_template('modal.html', posts = POSTS)


if __name__ == '__main__':
    app.run(debug=True)