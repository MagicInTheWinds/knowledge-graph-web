# System Architecture & Patterns

## High-Level Architecture
[Frontend SPA] <--> [FastAPI Gateway] <--> [Service Layer]
                                            |
                                      [Task Queue]
                                            |
                                     [Worker Nodes]
                                     (Scraping/NLP)

## Data Flow (Ingestion)
1. **Source** (User/File/Web) -> **Raw Data**
2. **Raw Data** -> **Extraction Service** (LLM) -> **Candidate Triples**
3. **Candidate Triples** -> **Review/Merge** -> **Graph Database**

## Design Patterns
- **Repository Pattern**: Abstract database access (Neo4j/Postgres).
- **Adapter Pattern**: For different ingestion sources (FileAdapter, WebAdapter).
- **CQRS**: Separate Reading graph (fast queries) from Writing/Processing (heavy jobs).