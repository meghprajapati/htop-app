from flask import Flask
from datetime import datetime
import pytz
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"

    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> Megh Prajapati</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
