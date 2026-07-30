# Project Structure

enterprise-ai-platform/

├── backend/
│
│   ├── app/
│   │
│   ├── api/
│   ├── auth/
│   ├── users/
│   ├── workspace/
│   ├── documents/
│   ├── ai/
│   ├── chat/
│   ├── notification/
│   ├── database/
│   ├── services/
│   ├── middleware/
│   ├── core/
│   ├── utils/
│   ├── schemas/
│   ├── models/
│   ├── repositories/
│   ├── tests/
│   └── main.py
│
├── frontend/
│
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── store/
│   ├── styles/
│   ├── types/
│   └── middleware.ts
│
├── docs/
│
├── infrastructure/
│
│   ├── docker/
│   ├── nginx/
│   ├── kubernetes/
│   └── terraform/
│
├── scripts/
│
├── .github/
│
│   └── workflows/
│
├── docker-compose.yml

├── README.md

└── LICENSE

---

## Architecture Style

Modular Monolith

Future:

Notification Service

↓

Microservice

AI Service

↓

Microservice

Search Service

↓

Microservice