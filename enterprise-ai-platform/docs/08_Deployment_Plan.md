# Deployment Plan

## Development Environment

Local Machine

Frontend

↓

Backend

↓

PostgreSQL

↓

Redis

↓

pgvector

Run everything using Docker Compose.

---

## Production Environment

User

↓

Internet

↓

Nginx

↓

Next.js

↓

FastAPI

↓

PostgreSQL

↓

Redis

↓

pgvector

↓

AWS S3

↓

Claude/OpenAI/Gemini

---

# Deployment Steps

1.

Build Docker Images

↓

2.

Run Docker Compose

↓

3.

Configure Environment Variables

↓

4.

Setup Reverse Proxy (Nginx)

↓

5.

Enable HTTPS

↓

6.

Deploy on AWS EC2

↓

7.

Configure GitHub Actions

↓

8.

Automatic Deployment

---

# CI/CD

GitHub

↓

GitHub Actions

↓

Build

↓

Test

↓

Docker Build

↓

Deploy AWS

---

# Future Improvements

- Kubernetes

- Helm Charts

- Terraform

- Monitoring

- Prometheus

- Grafana

- Auto Scaling