# Product Requirements Document – chatflow-open

---

## 1. Problem Statement

Customer support teams increasingly rely on proprietary SaaS chat platforms (e.g., Intercom, Zendesk Chat, Drift). These solutions lock teams into vendor pricing, data residency constraints, and limited extensibility. Small to mid‑size businesses and open‑source communities need a **self‑hostable, open‑source** alternative that delivers comparable features—live chat, ticketing, knowledge base, and analytics—while giving full control over data and integration flexibility.

## 2. Target Users

| Persona | Role | Pain Points | Desired Outcomes |
|---------|------|-------------|------------------|
| **SMB Customer Support Manager** | Oversees support ops for 10–200 users | • High SaaS costs<br>• Limited customization<br>• Data residency concerns | • Reduce monthly spend<br>• Deploy on existing infra<br>• Integrate with in‑house tools |
| **Open‑Source Project Maintainer** | Maintains community support portal | • No budget for paid chat<br>• Need to keep data open<br>• Want to embed chat in docs site | • Free, self‑hosted chat<br>• Easy embed & API<br>• Community analytics |
| **DevOps Engineer** | Deploys & maintains infra | • Security & compliance<br>• Scalability<br>• CI/CD integration | • Docker/K8s ready<br>• Zero‑downtime updates<br>• Observability hooks |

## 3. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Launch a production‑ready, self‑hostable platform** | Time to first deployment (from repo clone to live chat) | ≤ 30 min |
| **Match Intercom feature set** | Feature parity score (based on internal checklist) | ≥ 90 % |
| **Enable rapid onboarding** | Avg. onboarding time for new team | ≤ 2 hrs |
| **Achieve community adoption** | Number of public GitHub stars / forks | ≥ 500 stars, 200 forks |
| **Demonstrate performance** | Avg. response latency (client → server) | ≤ 200 ms under 1k concurrent users |
| **Ensure extensibility** | Number of supported integrations (CRM, ticketing, analytics) | ≥ 5 core integrations |

## 4. Key Features (Prioritized)

| Rank | Feature | Description | Acceptance Criteria |
|------|---------|-------------|---------------------|
| **1** | **Self‑hostable Docker/K8s stack** | Full stack (frontend, backend, DB, Redis, WebSocket) bundled in Docker Compose and Helm chart | • `docker-compose up` runs in <30 s<br>• Helm chart deploys in <5 min |
| **2** | **Live Chat UI** | Responsive web widget with typing indicators, file upload, and emoji support | • Widget loads in <1 s<br>• File uploads ≤ 10 MB |
| **3** | **Ticketing System** | Convert chat to ticket, assign, SLA tracking, status workflow | • Ticket creation auto‑populates from chat<br>• SLA breach alerts |
| **4** | **Knowledge Base Integration** | Searchable FAQ, article suggestions during chat | • Search returns top 3 results within 200 ms |
| **5** | **Analytics Dashboard** | Real‑time metrics (sessions, response time, CSAT) | • Dashboard updates within 5 s of event |
| **6** | **API & Webhooks** | REST/GraphQL API for external systems, webhook triggers | • API docs available, 200 ms latency |
| **7** | **Multi‑tenant & Role‑based Access Control** | Separate orgs, admin/agent/visitor roles | • Role permissions enforced in UI & API |
| **8** | **Security & Compliance** | TLS, OAuth2, audit logs, GDPR data export | • All traffic TLS‑encrypted, logs retained 90 days |
| **9** | **Plugin Architecture** | Allow community plugins (CRM, ticketing, AI) | • Plugin can register a new endpoint |
| **10** | **Chatbot/AI Assistant** | Optional integration with open‑source LLM (vLLM, SGLang) | • Bot responds within 1 s, fallback to human |

## 5. Scope

### In Scope
- Core chat, ticketing, and knowledge base features.
- Docker/K8s deployment artifacts.
- Basic integrations: email, Slack, and a generic CRM.
- Documentation (README, deployment guide, API spec).
- CI/CD pipeline for automated tests and releases.

### Out of Scope
- Native mobile app (will be addressed in a future release).
- Advanced AI chatbot (basic integration only; full LLM training not included).
- Enterprise‑grade compliance (PCI‑DSS, SOC‑2) – will be community‑driven.
- Graphical UI customizer (theme builder) – will be a plugin.

## 6. Dependencies & Constraints

| Dependency | Source | Notes |
|------------|--------|-------|
| **Database** | PostgreSQL | Must support JSONB for flexible data. |
| **Cache** | Redis | For session store and pub/sub. |
| **WebSocket** | Socket.IO | Real‑time communication. |
| **LLM inference** | vLLM / SGLang | Optional, community‑contributed. |
| **Open‑Source Licenses** | MIT/Apache‑2.0 | Ensure all third‑party libs are compatible. |
| **Hosting** | Any self‑hosted environment (VM, K8s) | No cloud‑only deployment. |

## 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Security vulnerabilities** | High | Conduct OWASP Top‑10 scan, enable automated SAST/DAST. |
| **Performance under load** | Medium | Load test with k6; optimize Redis pub/sub. |
| **Community adoption** | Medium | Provide clear docs, example deployments, and a plugin SDK. |
| **License conflicts** | Low | Verify all dependencies; maintain a license compliance file. |

## 8. Timeline (High‑Level)

| Phase | Duration | Milestones |
|-------|----------|------------|
| **Discovery & Design** | 2 weeks | Feature spec, architecture diagram |
| **Core Development** | 6 weeks | Chat, ticketing, knowledge base |
| **Deployment & Ops** | 2 weeks | Docker Compose, Helm chart, CI/CD |
| **Testing & QA** | 2 weeks | Unit, integration, load tests |
| **Documentation & Release** | 1 week | Docs, GitHub release, marketing |
| **Post‑Launch Support** | Ongoing | Bug triage, community feedback |

## 9. Deliverables

1. **Source Code** – `chatflow-open` repo with all features.
2. **Docker Compose & Helm Chart** – ready for production.
3. **API Documentation** – OpenAPI spec, example calls.
4. **User Guides** – Installation, configuration, admin panel.
5. **Testing Suite** – Unit, integration, performance tests.
6. **Release Notes** – Versioned changelog.

---

*Prepared by: Senior Product/Engineering Lead – Axentx*
