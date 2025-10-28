from flask import Flask, jsonify, render_template
from docker_utils import get_containers, get_container_by_id, get_system_info
import docker 
app = Flask(__name__)
client = docker.from_env()
@app.route('/')
def index():
    return render_template('index.html' , containers = get_containers())

# @app.route('/containers')
# def containers():
#     return jsonify(get_containers())

@app.route('/stats/<string:id>')
def stats(id):
    # return jsonify(get_container_by_id(id))
    container_stats = get_container_by_id(id)
    print(container_stats)
    return render_template('stats.html', stats = container_stats , container_id=id)

# @app.route('/stats/<string:id>')
# def api_stats(id):
#     container_stats = get_container_by_id(id)
#     if not container_stats:
#         return jsonify({'error': 'not found'}), 404
#     return jsonify(container_stats)

# @app.route('/stats/<string:id>/data')
# def stats_data(id):
#     container_stats = get_container_by_id(id)
    
#     # Верните нужные данные в JSON формате
#     return jsonify({
#         'id': id,
#         'memory': container_stats.get('memory', 'N/A'),
#         'cpu': container_stats.get('cpu', 'N/A'),
#         # добавьте другие поля которые нужны
#     })

@app.route('/container/<string:id>/start', methods=['POST'])
def start_container(id):
    try:
        container = client.containers.get(id)
        container.start()
        return jsonify({'status': 'success', 'message': 'Container started'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/container/<string:id>/stop', methods=['POST'])
def stop_container(id):
    try:
        container = client.containers.get(id)
        container.stop()
        return jsonify({'status': 'success', 'message': 'Container stopped'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/container/<string:id>/remove', methods=['POST'])
def remove_container(id):
    try:
        container = client.containers.get(id)
        container.remove(force=True)
        return jsonify({'status': 'success', 'message': 'Container removed'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/stats/')
def stat():
    sysinfo = get_system_info()
    print(sysinfo)
    return render_template('statsd.html' , stats = sysinfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

