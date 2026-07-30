# System Architecture

## 1. Overview

The Enterprise AI Knowledge Platform follows a modular monolith architecture.

The application consists of:

- Frontend (Next.js)
- Backend (FastAPI)
- PostgreSQL Database
- Redis Cache
- Vector Database (pgvector)
- AI Provider (Claude / OpenAI / Gemini)
- Object Storage (Local Storage → AWS S3 in Production)

The architecture is designed so that individual modules can later be extracted into independent microservices if required.

---

## 2. High-Level Architecture

```

Browser
│
▼
Next.js Frontend
│
▼ REST API
FastAPI Backend
│
├── Authentication Module
├── User Module
├── Workspace Module
├── Document Module
├── AI Module
├── Chat Module
├── Notification Module
└── Admin Module
│
├───────────────┬───────────────┬───────────────┐
│               │               │               │
▼               ▼               ▼               ▼
PostgreSQL     Redis         pgvector     AI Provider
                                               │
                                               ▼
                                    Claude / OpenAI / Gemini

```

---

## 3. Frontend

Technology:

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

Responsibilities:

- Authentication
- Dashboard
- Document Upload
- AI Chat
- Admin Panel
- User Settings

The frontend communicates with the backend using REST APIs.

---

## 4. Backend

Technology:

- FastAPI
- SQLAlchemy
- Alembic

Responsibilities:

- Authentication
- Business Logic
- AI Processing
- File Upload
- Database Operations
- Authorization
- REST APIs

---

## 5. Database

Primary Database:

PostgreSQL

Stores:

- Users
- Workspaces
- Documents
- Chats
- Messages
- Roles
- Permissions

---

## 6. Cache

Technology:

Redis

Purpose:

- Session Cache
- Rate Limiting
- Background Tasks
- Frequently Accessed Data

---

## 7. Vector Database

Technology:

pgvector

Purpose:

- Store document embeddings
- Perform semantic search
- Retrieve relevant document chunks

---

## 8. AI Layer

Supported Providers:

- Claude
- OpenAI
- Gemini

Responsibilities:

- Generate embeddings
- Answer user questions
- Summarize documents
- Generate citations

---

## 9. Storage

Development:

- Local Storage

Production:

- AWS S3

Stores:

- Uploaded documents
- Images
- Attachments

---

## 10. Deployment

Development Environment:

Docker Compose

Production Environment:

- AWS EC2
- Docker
- Nginx
- GitHub Actions

---

## 11. Future Architecture

The current architecture follows a modular monolith approach.

As the system grows, the following modules can be extracted into independent microservices:

- Notification Service
- AI Service
- Search Service

This evolution allows the platform to scale without major changes to the application design.