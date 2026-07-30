# API Specification

## Base URL

/api/v1

---

# Authentication

POST /auth/register

POST /auth/login

POST /auth/logout

POST /auth/refresh

GET /auth/profile

PUT /auth/profile

---

# Workspace

POST /workspaces

GET /workspaces

GET /workspaces/{id}

PUT /workspaces/{id}

DELETE /workspaces/{id}

POST /workspaces/{id}/invite

GET /workspaces/{id}/members

DELETE /workspaces/{id}/members/{id}

---

# Documents

POST /documents/upload

GET /documents

GET /documents/{id}

DELETE /documents/{id}

GET /documents/search

---

# AI Chat

POST /chat

GET /chat/history

GET /chat/{id}

DELETE /chat/{id}

---

# Notifications

GET /notifications

PUT /notifications/{id}

DELETE /notifications/{id}

---

# Admin

GET /admin/users

GET /admin/workspaces

GET /admin/analytics

GET /admin/logs

---

# Health

GET /health

GET /ready

GET /live