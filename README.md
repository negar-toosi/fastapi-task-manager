# 🚀 FastAPI Task Manager

A simple task manager API built with FastAPI, PostgreSQL, and Docker, deployed using systemd.

You can access the API documentation at http://91.107.252.113:8000/docs.

---

## 📦 Prerequisites

Make sure the following tools are installed on your system:

- 🐍 Python 3.13 (only if running without Docker)
- 🐳 Docker
- 🐙 Docker Compose

---

## 🛠️ Project Setup

### 1. Clone the repository

```bash
git clone git@github.com:negar-toosi/fastapi-task-manager.git
cd fastapi-task-manager
```

### 2. Create `.env` file

The `.env` file stores configuration variables like database URLs and secret keys outside the code. In this project, you create it by copying `.example.env` and updating the values as needed:

```bash
cp .example.env .env
```
---

## 🐳 Running with Docker

Build and start the project using:

```bash
docker compose up --build
```

This will start:

- PostgreSQL
- The FastAPI backend (on `http://localhost:8000`)

I have created a `docker-compose.dev.yml` file specifically for development purposes. This setup includes:

- PostgreSQL database
- PgAdmin for database management (accessible on `http://localhost:5050`)
- FastAPI backend

You can run the development environment with:

```bash
docker compose -f docker-compose.dev.yml up -d
```

Access the API docs at:

- `http://localhost:8000/docs` (Swagger UI)
- `http://localhost:8000/redoc` (ReDoc)

---

### 3. Start the app

Make sure your PostgreSQL server is running and accessible, then:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Endpoints

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| GET    | `/tasks/`          | Get list of all tasks         |
| POST   | `/tasks/`          | Create a new task             |
| GET    | `/tasks/{id}`      | Retrieve a specific task      |
| PUT    | `/tasks/{id}`      | Update a task                 |
| DELETE | `/tasks/{id}`      | Delete a task                 |

---

## 🧰 Deployment (Optional: systemd + Gunicorn)

Make sure PostgreSQL is installed and running on your server. Then, open the PostgreSQL interactive terminal by running:

```bash
sudo -u postgres psql
```
Once inside the PostgreSQL shell, run the following SQL commands to create a new database user and a database for the project:

-- Create a new user with a password
```ini
CREATE USER user WITH PASSWORD 'password';
```

-- Create a new database named 'task'
CREATE DATABASE task;

-- Grant all privileges on the 'task' database to the new user
GRANT ALL PRIVILEGES ON DATABASE task TO user;

-- Exit the PostgreSQL shell
\q

```ini
# /etc/systemd/system/fastapi-task.service
[Unit]
Description=FastAPI Task Manager app
After=network.target

[Service]
User=YOUR_SERVER_USERNAME
Group=www-data
WorkingDirectory=/var/fastapi-task-manager
ExecStart=/var/fastapi-task-manager/venv/bin/gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Then run:

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi-task
sudo systemctl start fastapi-task
```

---

## 🧩 Notes

- Make sure to run database migrations if needed.
- Adjust your `.env` and database settings based on your environment.
- Always rebuild your Docker containers after changing dependencies.
