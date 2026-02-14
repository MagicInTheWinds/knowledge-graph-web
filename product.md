# Product Context: Knowledge Graph Builder

## 1. Product Vision
A full-stack web application designed to construct, manage, and visualize Domain Knowledge Graphs. It acts as a central hub for knowledge aggregation, allowing users to build graphs through manual input, document parsing, and autonomous web agents.

## 2. Core Features

### 2.1 Data Ingestion Sources
- **Manual Input**: UI for creating nodes and relationships (triples) directly.
- **Document Upload**: Support for PDF, Markdown, TXT. System parses and extracts entities/relationships using LLMs.
- **Browser/Web Agent**: Integration with `browser-use` and MCP tools to autonomously browse target websites, scrape content, and extract knowledge.

### 2.2 Knowledge Processing
- **Entity Extraction**: NLP pipeline to identify entities (Nodes).
- **Relationship Extraction**: NLP pipeline to identify predicates (Edges).
- **Resolution**: Merging duplicate nodes/entities.

### 2.3 Visualization & Interaction
- **Graph Explorer**: Interactive 2D/3D visualization of the knowledge graph.
- **Search**: Semantic and keyword search for nodes.

## 3. User Journey
1. User logs in.
2. User creates a "Project" (Domain).
3. User chooses a data source (e.g., "Scrape this URL" or "Upload this PDF").
4. System processes data -> displays extraction candidates.
5. User reviews/approves -> Data commits to Graph DB.
6. User explores the graph.