import docker

client = docker.from_env()

def get_containers():
    containers = client.containers.list(all=True)
    return [
        {
            "id": c.short_id,
            "name": c.name,
            "status": c.status,
            "ports": c.ports,
        } for c in containers
    ]

def get_container_by_id(container_id):
    try:
        container = client.containers.get(container_id)
        return {
            "id": container.short_id,
            "name": container.name,
            "status": container.status,
            "image": container.image.tags,
            "created": container.attrs["Created"]
        }
    except Exception as e:
        return {"error": str(e)}

def get_system_info():
    info = client.info()
    return {
        "cpu_count": info["NCPU"],
        "mem_total": round(info["MemTotal"] / 1024**3, 2),
        "docker_version": info["ServerVersion"]
    }

