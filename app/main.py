from flask import Flask, jsonify, render_template
from docker_utils import get_containers, get_container_by_id, get_system_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/containers')
def containers():
    return jsonify(get_containers())

@app.route('/stats/<string:id>')
def stats(id):
    # return jsonify(get_container_by_id(id))
    container_stats = get_container_by_id(id)
    print(container_stats)
    return render_template('stats.html', stats = container_stats)

@app.route('/stats/')
def stat():
    sysinfo = get_system_info()
    print(sysinfo)
    return render_template('statsd.html' , stats = sysinfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

