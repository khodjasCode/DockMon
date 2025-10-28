# 🚢 DockMon — Docker Monitoring Dashboard

**DockMon** is a lightweight **Flask + Nginx** dashboard for monitoring and managing Docker containers.  
It shows live stats (CPU, RAM, uptime) and lets you control containers directly from the web UI: start, stop, remove;

---

## ⚙️ Features

- View all containers with their ports and statuses  
- Live CPU/RAM/uptime stats  
- Start / Stop / Remove containers  
- Auto-refresh every few seconds  
- `/health` endpoint for Docker healthcheck  
- `.env` config support via `python-dotenv`  
- Logging volume `./logs:/app/logs`  
- Ready for CI/CD setup  

---

## 🧱 Tech Stack

Flask · Docker SDK · Nginx · HTML/JS · Makefile · Python-dotenv

---
