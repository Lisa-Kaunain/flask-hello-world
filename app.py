from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    return '"Hello from PaaS Lab! Lisa Kaunain P (24MID0183) Vit'
