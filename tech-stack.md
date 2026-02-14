# Technology Stack

## Frontend (Web Client)
- **Framework**: Next.js 14+ (React)
- **Language**: TypeScript
- **Styling**: Tailwind CSS + Shadcn/UI
- **State Management**: Zustand or React Context
- **Graph Viz**: React Flow or Cosmograph

## Backend (API & Workers)
- **Language**: Python 3.11+ (Chosen for AI/NLP ecosystem)
- **Framework**: FastAPI
- **Task Queue**: Celery or ARQ (Redis backed) - for long-running scrapes/processing
- **Agent Framework**: LangChain / LangGraph
- **Browser Automation**: `browser-use` (Playwright)

## Database / Storage
- **Graph Database**: Neo4j (Community Edition)
- **Vector Database**: ChromaDB (Local) or PGVector
- **Relational DB**: SQLite (Dev) / PostgreSQL (Prod) - for user/project metadata
- **Cache**: Redis

## DevOps & Tools
- **Containerization**: Docker & Docker Compose
- **Testing**: Pytest (Backend), Jest/React Testing Library (Frontend)
- **Linting**: Ruff (Python), ESLint (TS)