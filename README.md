# Uptime Monitor

A Dockerized uptime monitoring service built with Python, FastAPI, PostgreSQL, and Docker Compose.

The application monitors websites by periodically checking their availability, recording health results, and storing monitoring data in a PostgreSQL database.

## Features

- Add websites to monitor
- Check website availability
- Track HTTP response status
- Store uptime check results
- Background monitoring worker
- PostgreSQL database storage
- Fully containerized with Docker
- Automated CI pipeline with GitHub Actions

## Architecture

```text
                Docker Compose

        ┌──────────────┐
        │   FastAPI    │
        │     API      │
        └──────┬───────┘
               │
               │
        ┌──────▼───────┐
        │ PostgreSQL   │
        │   Database   │
        └──────▲───────┘
               │
        ┌──────┴───────┐
        │   Worker     │
        │ Health Checks│
        └──────────────┘
```

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions

## Running Locally

### Clone the repository

```bash
git clone <repository-url>
cd uptime-monitor
```

### Create environment variables

Create a `.env` file in the project root:

```env
POSTGRES_USER=uptime
POSTGRES_PASSWORD=uptimepassword
POSTGRES_DB=uptimedb
```

### Start the application

```bash
docker compose up --build
```

The API documentation will be available at:

```text
http://localhost:8000/docs
```

## Example Workflow

1. Add a website:

```json
{
  "name": "Google",
  "url": "https://google.com"
}
```

2. The background worker periodically checks each website.

3. The results are stored in PostgreSQL.

## CI Pipeline

GitHub Actions automatically:

- Installs project dependencies
- Builds the Docker image
- Verifies the application builds successfully on every push and pull request
