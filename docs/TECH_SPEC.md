# TECH_SPEC.md

## chatflow‑open  
*A self‑hostable, open‑source customer‑support chat platform that provides Intercom‑like functionality without vendor lock‑in.*

---

## 1. Overview

chatflow‑open is a modular, event‑driven chat platform designed for rapid deployment in on‑premise or cloud environments. It exposes a REST/GraphQL API for chat, user, and ticket management, and a WebSocket gateway for real‑time messaging. The system is built to be horizontally scalable, highly available, and fully auditable, leveraging the Axentx stack (PostgreSQL, Redis, Kafka, and a lightweight Go micro‑service layer) and a React/TypeScript front‑end.

---

## 2. Architecture

```
┌───────────────────────┐
│  Client (Web / Mobile)│
│  - React SPA          │
│  - WebSocket client   │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  API Gateway (NGINX)   │
│  - TLS termination     │
│  - Rate limiting       │
└───────┬───────┬────────┘
        │       │
        ▼       ▼
┌───────────────┐ ┌───────────────────┐
│  Auth Service │ │  Chat Service     │
│  (OAuth2/JWT) │ │  (WebSocket + REST)│
└───────┬───────┘ └───────┬────────────┘
        │               │
        ▼               ▼
┌───────────────────────┐
│  Event Bus (Kafka)    │
│  - Chat events         │
│  - Ticket events       │
└───────┬───────┬────────┘
        │       │
        ▼       ▼
┌───────────────┐ ┌───────────────────┐
│  Ticket Service│ │  Notification      │
│  (REST)        │ │  Service (Email/SMS│
└───────┬───────┘ │  Webhook)          │
        │       └───────┬────────────┘
        ▼               ▼
┌───────────────────────┐
│  Persistence Layer    │
│  - PostgreSQL         │
│  - Redis (cache)      │
└───────────────────────┘
```

### 2.1 Service Responsibilities

| Service | Primary Function | Key Endpoints |
|---------|------------------|---------------|
| **Auth Service** | OAuth2 / JWT issuance, user identity, role‑based access control | `/auth/login`, `/auth/refresh`, `/auth/validate` |
| **Chat Service** | Real‑time messaging, chat room lifecycle, message history | `/chat/rooms`, `/chat/rooms/{id}/messages`, `/ws/chat` |
| **Ticket Service** | Ticket CRUD, assignment, SLA tracking | `/tickets`, `/tickets/{id}`, `/tickets/{id}/assign` |
| **Notification Service** | Email/SMS/Webhook notifications, push | `/notify/email`, `/notify/sms`, `/notify/webhook` |
| **API Gateway** | TLS, routing, rate‑limiting, CORS | NGINX reverse proxy |

---

## 3. Data Model

### 3.1 PostgreSQL Schema (simplified)

```sql
-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT,
    role TEXT NOT NULL, -- 'agent', 'customer', 'admin'
    created_at TIMESTAMP DEFAULT NOW()
);

-- Chat Rooms
CREATE TABLE rooms (
    id UUID PRIMARY KEY,
    title TEXT,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Messages
CREATE TABLE messages (
    id UUID PRIMARY KEY,
    room_id UUID REFERENCES rooms(id),
    sender_id UUID REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tickets
CREATE TABLE tickets (
    id UUID PRIMARY KEY,
    room_id UUID REFERENCES rooms(id),
    subject TEXT,
    status TEXT DEFAULT 'open',
    assignee_id UUID REFERENCES users(id),
    priority TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Notifications
CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    type TEXT, -- 'email', 'sms', 'webhook'
    payload JSONB,
    sent_at TIMESTAMP,
    status TEXT DEFAULT 'queued'
);
```

### 3.2 Redis Cache

- `room:{id}:messages` – LRU list of recent messages (max 100 per room)
- `user:{id}:online` – Boolean flag for presence

### 3.3 Kafka Topics

| Topic | Purpose | Partition Count |
|-------|---------|-----------------|
| `chat.messages` | Persisted chat events | 3 |
| `ticket.events` | Ticket lifecycle events | 2 |
| `notification.queue` | Notification dispatch queue | 2 |

---

## 4. Key APIs & Interfaces

### 4.1 REST API (JSON)

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| POST | `/auth/login` | Exchange credentials for JWT | Public |
| GET | `/chat/rooms` | List rooms for user | Bearer |
| POST | `/chat/rooms` | Create new room | Bearer |
| GET | `/chat/rooms/{id}/messages?limit=50` | Paginated messages | Bearer |
| POST | `/tickets` | Create ticket from room | Bearer |
| GET | `/tickets/{id}` | Retrieve ticket | Bearer |
| POST | `/tickets/{id}/assign` | Assign ticket to agent | Bearer |
| POST | `/notify/email` | Send email | Bearer |
| POST | `/notify/sms` | Send SMS | Bearer |

### 4.2 WebSocket API

- **Endpoint**: `wss://<host>/ws/chat`
- **Message Types**:
  - `join_room {room_id}`
  - `leave_room {room_id}`
  - `send_message {room_id, content}`
  - `typing {room_id, isTyping}`
- **Server Events**:
  - `message {room_id, message}`
  - `typing {room_id, user_id, isTyping}`
  - `room_update {room_id, data}`

### 4.3 GraphQL (Optional)

- `query rooms { id title }`
- `mutation createMessage(roomId: ID!, content: String!)`

---

## 5. Technology Stack

| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| **Front‑end** | React + TypeScript + Vite | 5.x | Modern SPA, fast dev cycle |
| **WebSocket** | Gorilla WebSocket (Go) | 1.5 | Low‑latency, Go native |
| **Auth** | OAuth2 (OpenID Connect) + JWT | 1.0 | Standard, extensible |
| **API Gateway** | NGINX | 1.27 | TLS, rate limiting |
| **Services** | Go (Gin) | 1.15 | High performance, static binaries |
| **Messaging** | Kafka (Confluent) | 3.7 | Durable event bus |
| **Database** | PostgreSQL | 16 | ACID, JSONB support |
| **Cache** | Redis | 7 | Presence & LRU caching |
| **Deployment** | Docker Compose + Helm | N/A | Containerized, Kubernetes ready |
| **CI/CD** | GitHub Actions | N/A | Automated tests & build |
| **Observability** | Prometheus + Grafana | N/A | Metrics & dashboards |
| **Logging** | Loki + Grafana | N/A | Structured logs |

---

## 6. Dependencies

| Package | Purpose | License |
|---------|---------|---------|
| `github.com/gin-gonic/gin` | HTTP router | MIT |
| `github.com/gorilla/websocket` | WebSocket | BSD-3 |
| `github.com/dgrijalva/jwt-go` | JWT handling | MIT |
| `github.com/segmentio/kafka-go` | Kafka client | MIT |
| `github.com/jackc/pgx/v5` | PostgreSQL driver | BSD-3 |
| `github.com/go-redis/redis/v8` | Redis client | BSD-3 |
| `github.com/go-playground/validator/v10` | Request validation | MIT |
| `github.com/stretchr/testify` | Testing | MIT |
| `github.com/rs/zerolog` | Logging | MIT |

All dependencies are open source and have permissive licenses.

---

## 7. Deployment

### 7.1 Docker Compose (dev)

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: chatflow
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: chatflow
    volumes:
      - pgdata:/var/lib/postgresql/data
  redis:
    image: redis:7
    command: redis-server --save 900 1 --loglevel warning
  kafka:
    image: bitnami/kafka:3.7
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
  zookeeper:
    image: bitnami/zookeeper:3.7
  auth:
    build: ./services/auth
    depends_on: [postgres]
  chat:
    build: ./services/chat
    depends_on: [postgres, redis, kafka]
  ticket:
    build: ./services/ticket
    depends_on: [postgres, kafka]
  notify:
    build: ./services/notify
    depends_on: [postgres, kafka]
  nginx:
    image: nginx:1.27
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on: [auth, chat, ticket, notify]
volumes:
  pgdata:
```

### 7.2 Helm Chart (K8s)

- `values.yaml` exposes image tags, replica counts, resource limits, and external DB/Redis/Kafka endpoints.
- `templates/` includes Deployments, Services, Ingress, ConfigMaps, and Secrets.
- RBAC and NetworkPolicies are defined for isolation.

### 7.3 CI/CD Pipeline

1. **Lint**: `golangci-lint run`, `eslint`, `stylelint`.
2. **Unit Tests**: `go test ./...`, `npm test`.
3. **Integration Tests**: Spin up Docker Compose, run end‑to‑end tests.
4. **Build**: Docker images pushed to `ghcr.io/axentx/chatflow-open`.
5. **Deploy**: Helm upgrade to target namespace.

---

## 8. Security & Compliance

- **Transport**: TLS 1.3 enforced by NGINX.
- **Authentication**: OAuth2 + JWT with short‑lived access tokens (15 min) and refresh tokens.
- **Authorization**: Role‑based access control; RBAC enforced at service layer.
- **Data Protection**: Passwords hashed with Argon2id; PII encrypted at rest (PostgreSQL column encryption).
- **Audit Logging**: All state‑changing API calls logged to Kafka `audit.log` topic.
- **Compliance**: GDPR‑ready – data deletion via `/users/{id}` DELETE, export via `/users/{id}/export`.

---

## 9. Performance & Scaling

| Metric | Target | Notes |
|--------|--------|-------|
| Message latency (WS) | < 50 ms | In‑memory Redis + Go |
| Ticket creation throughput | 200 req/s | Kafka + async workers |
| Horizontal scaling | Stateless services | Docker swarm / K8s |
| Database | 10 k TPS | PostgreSQL with partitioned tables |
| Cache hit rate | > 90 % | Redis LRU eviction |

Auto‑scaling rules:
- **CPU > 70 %** → +1 replica
- **Memory > 80 %** → +1 replica
- **Kafka lag > 1000** → trigger alert

---

## 10. Extensibility

- **Plugins**: Go plugin system for custom notification channels.
- **SDKs**: Auto‑generated TypeScript SDK from OpenAPI spec.
- **Webhook**: External services can subscribe to `ticket.events` via Kafka Connect.

---

## 11. Roadmap (next 6 months)

1. **SSO Integration** – Azure AD / Okta support.
2. **AI‑Powered Auto‑Response** – Integrate vLLM for canned replies.
3. **Mobile SDK** – React Native wrapper.
4. **Analytics Dashboard** – Real‑time KPI metrics.
5. **Marketplace** – Plugin marketplace for third‑party extensions.

---

## 12. Contact & Governance

- **Repo Owner**: `@arkashira`
- **Issue Tracker**: GitHub Issues
- **Slack Channel**: `#chatflow-open`
- **Release Cadence**: Monthly minor releases, quarterly major releases.

---
