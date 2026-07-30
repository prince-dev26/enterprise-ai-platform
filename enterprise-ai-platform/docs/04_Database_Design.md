# Database Design

## Overview

The Enterprise AI Knowledge Platform uses PostgreSQL as the primary relational database.

The database is designed using normalization principles while keeping scalability and performance in mind.

---

# Core Entities

## Users

Stores user account information.

Fields:

- id (UUID)
- first_name
- last_name
- email
- password_hash
- avatar
- status
- created_at
- updated_at

---

## Workspaces

Represents an organization or team.

Fields:

- id
- name
- slug
- owner_id
- created_at
- updated_at

---

## Workspace Members

Maps users to workspaces.

Fields:

- id
- workspace_id
- user_id
- role
- joined_at

Roles:

- Owner
- Admin
- Member

---

## Documents

Stores uploaded documents.

Fields:

- id
- workspace_id
- uploaded_by
- file_name
- file_type
- file_size
- storage_path
- upload_status
- created_at

---

## Document Chunks

Stores text chunks extracted from uploaded documents.

Fields:

- id
- document_id
- chunk_number
- content
- embedding_id

---

## Chats

Stores chat sessions.

Fields:

- id
- workspace_id
- user_id
- title
- created_at

---

## Messages

Stores conversation messages.

Fields:

- id
- chat_id
- sender
- content
- created_at

---

## Notifications

Stores notifications.

Fields:

- id
- user_id
- type
- title
- message
- is_read
- created_at

---

# Relationships

User

↓

Workspace

↓

Documents

↓

Document Chunks

↓

Embeddings

User

↓

Chats

↓

Messages

---

# Database Diagram (Simplified)

Users
│
├──── Workspace Members ─── Workspaces
│                              │
│                              │
│                         Documents
│                              │
│                       Document Chunks
│
└──── Chats
      │
      Messages

---

# Future Tables

- Audit Logs
- API Keys
- Billing
- AI Usage
- Prompt Templates
- AI Agents