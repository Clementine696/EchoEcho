from flask import Flask, render_template, url_for, request, redirect, send_file, jsonify
import base64
import sqlite3

# เชื่อมต่อ database
db_local = "Audio_DB.db"

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/Soundpad')
def voicechanger():
    conn = sqlite3.connect(db_local)
    cursor = conn.cursor()
    cursor.execute("SELECT id, audio_name, duration FROM Soundpad")
    data = cursor.fetchall()
    conn.close()
    return render_template('soundpad.html', audio_files=data)
    # return render_template('soundpad.html')

# @app.route('/voicechanger')
# def addAudio():
#     return render_template('voicechanger.html')

@app.route('/modal')
def modal():
    return render_template('modal.html')

@app.route('/addAudio', methods=['GET','POST'])
def addAudio():
    if request.method == 'POST':
        audio_name = request.form['audio_name']
        audio_src = request.form['audio_src']
        duration = request.form['duration']
        
        conn = sqlite3.connect(db_local)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Soundpad (audio_name, audio_src, duration) VALUES (?, ?, ?)", (audio_name, audio_src, duration))
        conn.commit()
        conn.close()
        
    return "Add Audio Success!"

@app.route('/download/<int:index>')
def download(index):
    print("index: ", index)
    conn = sqlite3.connect(db_local)
    cursor = conn.cursor()
    cursor.execute("SELECT audio_name, audio_src FROM Soundpad WHERE id=?", (index,))
    data = cursor.fetchone()
    conn.close()
    audio_name = data[0]
    audio_src = data[1]
    print("audio_name: ", audio_name)
    try:
        return jsonify({'audio_name': audio_name, 'audio_src': audio_src})
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(debug=True)