from flask import Flask, request, jsonify
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

# Connect to SQLite
conn = sqlite3.connect('data.db', check_same_thread=False)

# Create table if it does not exist
def create_table():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS human_data (
            instance_id TEXT,
            timestamp DATETIME,
            pos_x REAL,
            pos_y REAL
        )
    ''')
    conn.commit()

create_table()

def save_to_db(data):
    cursor = conn.cursor()
    for instance_id, instance in data['Instances'].items():
        timestamp = datetime.utcfromtimestamp(int(data['timestamp']['$date']['$numberLong']) / 1000)
        pos_x = instance['pos_x']
        pos_y = instance['pos_y']
        cursor.execute("INSERT INTO human_data (instance_id, timestamp, pos_x, pos_y) VALUES (?, ?, ?, ?)",
                       (instance_id, timestamp, pos_x, pos_y))
    conn.commit()

@app.route('/publish', methods=['POST'])
def publish_data():
    data = request.get_json()
    save_to_db(data)
    return jsonify({'status': 'success'}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM human_data")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({
            'instance_id': row[0],
            'timestamp': row[1],
            'pos_x': row[2],
            'pos_y': row[3]
        })
    return jsonify(data)

@app.route('/api/heatmap', methods=['GET'])
def get_heatmap():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT pos_x, pos_y, COUNT(*) as count
        FROM human_data
        GROUP BY pos_x, pos_y
    ''')
    rows = cursor.fetchall()
    heatmap_data = []
    for row in rows:
        heatmap_data.append({
            'pos_x': row[0],
            'pos_y': row[1],
            'count': row[2]
        })
    return jsonify(heatmap_data)
    
if __name__ == '__main__':
    app.run(debug=True)
