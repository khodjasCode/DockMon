import docker

client = docker.from_env()

def get_containers():
    containers = []
    for c in client.containers.list(all=True):
        containers.append({
            "name": c.name,
            "status": c.status,
            "ports": c.attrs.get("NetworkSettings", {}).get("Ports", {})
        })
    return containers

def get_system_info():
    info = client.info()
    return {
        "containers_running": info.get("ContainersRunning"),
        "containers_stopped": info.get("ContainersStopped"),
        "images": info.get("Images"),
        "server_version": info.get("ServerVersion"),
    }

