# News Curator

## Overview

**News Curator** is a web-based application for searching, curating, and managing news articles using Google News RSS feeds. It features a FastAPI backend for querying news and a Streamlit frontend for an interactive user experience, including term management, search, and article grouping.

---

## Features

- **Backend (FastAPI):**
  - Exposes a `/search` API endpoint for querying Google News RSS feeds.
  - Parses and structures news results using BeautifulSoup.
  - Accepts flexible search parameters (term, time span, search type).

- **Frontend (Streamlit):**
  - Manage search terms (add/delete).
  - Search news by term, time span, and in title/body.
  - View, filter, and group search results.
  - Save, remove, and delete article groups for later review.
  - All data (terms, groups) is persisted in shared JSON files.

- **Persistence:**
  - Search terms and article groups are stored in `/shared_models/terms.json` and `/shared_models/articles.json` (shared between backend and frontend).

---

## Project Structure

```
news-curator/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── query_logic.py
│   └── requirements.txt
├── front/
│   ├── app/
│   │   ├── main.py
│   │   ├── ui/
│   │   │   ├── terms.py
│   │   │   ├── search.py
│   │   │   └── groups.py
│   │   └── services/
│   │       ├── terms.py
│   │       └── groups.py
│   └── requirements.txt
├── shared_models/
│   ├── classes.py
│   ├── terms.json
│   └── articles.json
├── docker-compose.yml
├── docker-compose-autoupdate.yml
├── Makefile
└── README.md
```

---

## Quick Start (with Docker)

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Build and Run

1. **Build and start all services:**
   ```sh
   make build
   make run
   ```
   Or, directly:
   ```sh
   docker compose up --build
   ```

2. **Access the application:**
   - **Frontend:** [http://localhost:8523](http://localhost:8523)
   - **Backend API:** [http://localhost:8527/docs](http://localhost:8527/docs) (FastAPI docs)

3. **Persistent Data:**
   - Terms and article groups are stored in `shared_models/` and shared between containers.

---

## Usage

- **Manage Terms:** Add or remove search terms in the sidebar.
- **Search News:** Select a term, time span, and search type (title/body) to fetch news.
- **Group Articles:** Save search results into named groups, remove articles, or delete groups.
- **All changes are saved automatically.**

---

## Development

- **Frontend:** Streamlit app in `front/app/main.py`
- **Backend:** FastAPI app in `backend/app/main.py`
- **Shared Models:** Data classes and JSON files in `shared_models/`

### Run Frontend Locally

```sh
cd front
pip install -r requirements.txt
streamlit run app/main.py
```

### Run Backend Locally

```sh
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8527
```

---

## Configuration

- **Ports:**
  - Frontend: `8523`
  - Backend: `8527`
- **Shared Data:** `shared_models/terms.json`, `shared_models/articles.json`

---

## Dependencies

- **Backend:** FastAPI, Uvicorn, Pydantic, Requests, BeautifulSoup4, lxml
- **Frontend:** Streamlit, Requests, Pydantic, Pandas, BeautifulSoup4, lxml, streamlit-tags