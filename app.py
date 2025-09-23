from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(_name_, static_folder='../frontend', static_url_path='/')

CSV_PATH = os.path.join(os.path.dirname(_file_), '..', 'dataset', 'bins.csv')

def read_csv():
    df = pd.read_csv(CSV_PATH, parse_dates=['Timestamp'])
    # convert types if needed
    df['Fill_Level'] = df['Fill_Level'].astype(int)
    return df

@app.route('/api/bins')
def api_bins():
    df = read_csv()
    # return as list of dicts
    data = df.to_dict(orient='records')
    # convert Timestamp to isoformat strings
    for r in data:
        if 'Timestamp' in r and pd.notna(r['Timestamp']):
            r['Timestamp'] = str(r['Timestamp'])
    return jsonify(data)

# serve frontend index.html
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if _name_ == '_main_':
    app.run(debug=True, port=5000)