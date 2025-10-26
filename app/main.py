from flask import Flask, jsonify, render_template
from docker_utils import get_containers, get_container_by_id, get_system_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/containers')
def containers():
    return jsonify(get_containers())

@app.route('/containers/<id>')
def container_detail(id):
    return jsonify(get_container_by_id(id))

@app.route('/stats')
def stats():
    return jsonify(get_system_info())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

