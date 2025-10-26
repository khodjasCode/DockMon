from flask import Flask, jsonify, render_template
from docker_utils import get_containers, get_system_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/containers')
def containers():
    return jsonify(get_containers())

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

