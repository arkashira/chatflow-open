# REQUIREMENTS.md

## Project Overview
**Project Name:** chatflow-open  
**Repository:** `arkashira/chatflow-open`  
**Description:** A self‑hostable, open‑source customer support chat platform that delivers Intercom‑like functionality while eliminating vendor lock‑in. The platform will support real‑time messaging, knowledge base integration, automated routing, and analytics, all deployable on-premises or in a private cloud.

---

## 1. Functional Requirements

| ID   | Description | Acceptance Criteria | Priority |
|------|-------------|---------------------|----------|
| **FR‑1** | **Real‑time Messaging** | • Users (customers & agents) can send/receive messages with < 200 ms latency.<br>• Supports text, emojis, and file attachments up to 50 MB.<br>• Message history is persisted and searchable. | High |
| **FR‑2** | **User Authentication & Authorization** | • Supports OAuth2, SAML, and local username/password.<br>• Role‑based access control: Customer, Agent, Admin.<br>• Session tokens expire after 30 min inactivity. | High |
| **FR‑3** | **Chat Routing & Assignment** | • Incoming customer messages are automatically routed to available agents based on skill, workload, and SLA.<br>• Manual reassignment by agents or admins is possible.<br>• Queue metrics (average wait time, ticket count) are exposed via API. | High |
| **FR‑4** | **Knowledge Base & Auto‑Responses** | • Agents can attach knowledge‑base articles to conversations.<br>• Auto‑response engine suggests articles based on message content using a lightweight LLM inference (vLLM).<br>• Suggestions are editable before sending. | Medium |
| **FR‑5** | **Threaded Conversations & Thread History** | • Conversations are displayed as threads with nested replies.<br>• Thread history is stored in a relational DB (PostgreSQL). | Medium |
| **FR‑6** | **File Management** | • Attachments are stored in an object store (S3‑compatible).<br>• Access control ensures only participants can view files.<br>• Files are scanned for malware using an open‑source scanner (ClamAV). | Medium |
| **FR‑7** | **Analytics & Reporting** | • Dashboard shows metrics: tickets resolved, average resolution time, agent performance.<br>• Exportable reports in CSV/JSON.<br>• API endpoints for external BI tools. | Low |
| **FR‑8** | **API & SDK** | • RESTful API for CRUD on messages, users, tickets, and knowledge base.<br>• WebSocket endpoint for real‑time updates.<br>• SDKs for Node.js and Python. | Low |
| **FR‑9** | **Internationalization (i18n)** | • UI supports at least 5 languages (en, es, fr, de, zh).<br>• Date/time formats adapt to locale. | Low |
| **FR‑10** | **Accessibility** | • WCAG 2.1 AA compliance for UI components.<br>• Keyboard navigation and screen‑reader support. | Low |

---

## 2. Non‑Functional Requirements

| ID   | Requirement | Specification | Priority |
|------|-------------|---------------|----------|
| **NFR‑1** | **Performance** | • 95 % of messages delivered within 200 ms under 1,000 concurrent users.<br>• API response time < 300 ms for 95 % of requests. | High |
| **NFR‑2** | **Scalability** | • Horizontal scaling of WebSocket servers via Kubernetes StatefulSets.<br>• Database sharding support for >10 M messages. | High |
| **NFR‑3** | **Reliability & Availability** | • 99.9 % uptime SLA.<br>• Automatic failover for database and message broker.<br>• Daily backups with point‑in‑time recovery. | High |
| **NFR‑4** | **Security** | • TLS 1.3 for all network traffic.<br>• OWASP Top‑10 mitigations (XSS, CSRF, injection).<br>• Role‑based RBAC enforced at API layer.<br>• Data encryption at rest (AES‑256). | High |
| **NFR‑5** | **Compliance** | • GDPR‑ready: data residency, right to erasure, audit logs.<br>• SOC 2 Type II readiness (audit logs, access controls). | Medium |
| **NFR‑6** | **Maintainability** | • Code coverage ≥ 85 % for core modules.<br>• CI/CD pipeline with automated linting, unit tests, and integration tests.<br>• Documentation in Markdown and Swagger/OpenAPI. | Medium |
| **NFR‑7** | **Extensibility** | • Plugin architecture for custom integrations (e.g., CRM, ticketing).<br>• Event bus (Kafka) for external event consumption. | Low |
| **NFR‑8** | **Usability** | • Responsive UI for desktop and mobile browsers.<br>• Live chat widget embeddable via script tag. | Low |

---

## 3. Constraints

1. **Open‑Source Stack** – Must use only permissively licensed libraries (MIT, Apache‑2.0, etc.).  
2. **Self‑Hosted** – No external SaaS dependencies; all services must run within the customer’s infrastructure.  
3. **Language** – Backend in Go (for performance and concurrency). Frontend in React with TypeScript.  
4. **Database** – PostgreSQL 15+; no proprietary extensions.  
5. **Message Broker** – NATS or RabbitMQ (open‑source).  
6. **LLM Inference** – vLLM for auto‑response suggestions; must run locally with GPU or CPU fallback.  
7. **Deployment** – Must support Helm charts for Kubernetes and Docker Compose for local dev.  

---

## 4. Assumptions

- Customers will provision their own object storage (S3‑compatible) and database; the platform will provide configuration templates.  
- The target user base includes small to medium enterprises (SMEs) with up to 500 concurrent agents.  
- External integrations (CRM, ticketing) will be handled via the plugin system; core product will not ship with any proprietary connectors.  
- The platform will be used in regions with varying data residency requirements; data locality will be configurable.  

---

## 5. Deliverables

| Item | Description | Owner | Due |
|------|-------------|-------|-----|
| **Architecture Diagram** | High‑level system components | Lead Architect | 2 weeks |
| **API Spec** | OpenAPI v3.1 document | API Lead | 3 weeks |
| **UI Mockups** | Wireframes for core screens | UX Lead | 3 weeks |
| **CI/CD Pipeline** | GitHub Actions for build, test, deploy | DevOps Lead | 4 weeks |
| **Security Review** | OWASP audit report | Security Lead | 5 weeks |
| **Beta Release** | First production‑ready version | Release Manager | 8 weeks |

---

## 6. Acceptance Criteria

- All functional requirements are fully implemented and pass automated tests.  
- Performance benchmarks meet NFR‑1 under simulated load.  
- Security audit scores ≥ 90 % with no critical findings.  
- Documentation is complete and passes linting checks.  
- Helm chart installs successfully on a fresh Kubernetes cluster (minikube).  

---

## 7. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **LLM inference latency** | High | Medium | Use vLLM with GPU acceleration; fallback to cached responses. |
| **Data residency compliance** | High | Medium | Allow configurable storage endpoints; provide audit logs. |
| **Plugin security** | Medium | Medium | Sandbox plugins; enforce signing and version checks. |
| **Scaling WebSocket** | Medium | Low | Use Kubernetes Horizontal Pod Autoscaler and sticky sessions. |

---

### End of Requirements Document
