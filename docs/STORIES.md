# STORIES.md

## Project: chatflow‑open  
**Goal** – Deliver a self‑hostable, open‑source customer‑support chat platform that rivals Intercom while eliminating vendor lock‑in.  
**MVP** – Core messaging, user management, web widget, and admin dashboard.  
**Future Enhancements** – AI‑powered responses, analytics, integrations, and advanced routing.

---

## Epics & Story Backlog

| Epic | Story | Acceptance Criteria |
|------|-------|---------------------|
| **E1 – Core Messaging** | **S1** | **As a** customer support agent, **I want** to send and receive real‑time messages with customers, **so that** I can resolve issues quickly. |
| | **S2** | **As a** customer, **I want** to chat with support from my website, **so that** I can get help without leaving the page. |
| | **S3** | **As a** system admin, **I want** to configure message persistence and retention policies, **so that** data compliance is maintained. |
| **E2 – User & Role Management** | **S4** | **As a** support agent, **I want** to log in with secure credentials, **so that** I can access my ticket queue. |
| | **S5** | **As a** system admin, **I want** to create, edit, and delete agent accounts and assign roles, **so that** I can control access. |
| | **S6** | **As a** system admin, **I want** to enforce MFA for all agents, **so that** security is strengthened. |
| **E3 – Web Widget & Integration** | **S7** | **As a** website owner, **I want** to embed a lightweight chat widget, **so that** visitors can start a conversation instantly. |
| | **S8** | **As a** website owner, **I want** to customize the widget’s branding (logo, colors, greeting), **so that** it matches my site’s look. |
| | **S9** | **As a** developer, **I want** an API to programmatically send messages, **so that** I can integrate with other systems. |
| **E4 – Admin Dashboard** | **S10** | **As a** support manager, **I want** a dashboard that shows active chats, queue lengths, and agent availability, **so that** I can monitor performance. |
| | **S11** | **As a** support manager, **I want** to view chat transcripts and export them as CSV, **so that** I can audit conversations. |
| | **S12** | **As a** support manager, **I want** to set up canned responses, **so that** agents can reply quickly. |
| **E5 – Reliability & Security** | **S13** | **As a** system admin, **I want** end‑to‑end encryption for messages, **so that** privacy is guaranteed. |
| | **S14** | **As a** system admin, **I want** automated backups and disaster‑recovery scripts, **so that** data is never lost. |
| **E6 – Future AI & Analytics** | **S15** | **As a** support manager, **I want** AI‑suggested replies, **so that** agents can resolve tickets faster. |

---

### Detailed Acceptance Criteria

#### S1 – Real‑time Messaging
- WebSocket or long‑polling connection established between client and server.
- Messages are persisted in a relational DB with timestamps.
- Agent receives notification badge for unread messages.
- Message delivery status (sent, delivered, read) is shown.

#### S2 – Customer Chat
- Widget loads within 200 ms on a standard page.
- Customer can type and send messages; agent receives instantly.
- Chat history is visible to both parties after login.

#### S3 – Persistence & Retention
- Admin can set retention period (e.g., 90 days).
- System automatically deletes messages older than the set period.
- Export option for all retained messages.

#### S4 – Agent Login
- OAuth2 or JWT authentication flow.
- Password reset via email.
- Session timeout after 30 min inactivity.

#### S5 – Role Management
- CRUD UI for agents.
- Roles: Agent, Manager, Admin.
- Permissions table stored in DB.

#### S6 – MFA
- Support for TOTP (Google Authenticator) and email OTP.
- MFA enforced on first login and optional for subsequent logins.

#### S7 – Widget Embedding
- `<script src="https://cdn.chatflow-open.com/widget.js"></script>` snippet.
- Widget auto‑detects page language.
- Fallback to iframe if JS disabled.

#### S8 – Widget Customization
- JSON config for colors, logo URL, greeting text.
- Live preview in admin panel.

#### S9 – Messaging API
- REST endpoints: `POST /api/messages`, `GET /api/chats`.
- API key authentication.
- Rate limiting (100 req/min).

#### S10 – Dashboard Overview
- Real‑time counters: active chats, pending chats, idle agents.
- Graph of chat volume over last 7 days.
- Agent status indicators (online, offline, busy).

#### S11 – Transcript Export
- CSV download with columns: timestamp, sender, message, agent ID.
- Filter by date range and agent.

#### S12 – Canned Responses
- CRUD UI for canned replies.
- Agents can insert canned reply via dropdown.
- Auto‑suggest based on conversation context.

#### S13 – End‑to‑End Encryption
- TLS for transport.
- Optional client‑side encryption with public key.
- Message payload stored encrypted in DB.

#### S14 – Backup & DR
- Daily full backup to S3-compatible storage.
- Point‑in‑time restore script.
- Backup retention policy configurable.

#### S15 – AI‑Suggested Replies
- Integration with open‑source LLM (e.g., vLLM) for on‑prem inference.
- Agent sees suggestions in a side panel.
- “Send” button to auto‑populate reply.

---

## MVP Release Order

1. **S1, S2, S3** – Core messaging and persistence.  
2. **S4, S5, S6** – Agent authentication and role management.  
3. **S7, S8** – Widget embedding and customization.  
4. **S9** – Messaging API.  
5. **S10, S11, S12** – Admin dashboard and canned responses.  
6. **S13, S14** – Security hardening and backups.  
7. **S15** – AI‑powered suggestions (post‑MVP).

---

### Notes

- All stories are written to be shippable and testable.  
- Acceptance criteria include both functional and non‑functional requirements.  
- The backlog respects the existing Axentx portfolio; no duplication of previously shipped products.  
- Future epics (AI, analytics, advanced routing) can be added once MVP is stable.
