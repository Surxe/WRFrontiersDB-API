from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('game_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/items')
def items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

if __name__ == '__main__':
    app.run(debug=True)