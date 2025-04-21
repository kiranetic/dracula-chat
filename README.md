# Dracula Chat

Dracula Chat is a lightweight, intelligent, and modular AI-based dialogue engine designed for customer support use cases. It combines fast semantic search with an OpenAI fallback to deliver accurate, human-like responses.

---

## ✨ Features

- 🔍 **Semantic Matching** using Sentence Transformers
- 🤖 **GPT Fallback** for non-FAQ queries
- 🧠 **Qdrant Vector Store** to manage embeddings
- 📋 **FAQ Ingestion** from JSON
- 🧪 **Similarity Scoring** with configurable threshold
- 📦 **FastAPI Backend**
- 📈 **Real-Time Logging** in JSONL format
- 🖥️ **Modern UI** using Streamlit

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/kiranetic/dracula-chat.git
cd dracula-chat
```

---

### 2. Install Python dependencies

Make sure you have **Python 3.10+** and **pip** installed.

```bash
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

---

### 3. Set up environment

Create a `.env` file at the root using `.env.example` as template:

```env
OPENAI_API_KEY=your-openai-key
OPENAI_MODEL=gpt-4o
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your-qdrant-key-if-any
COLLECTION_NAME=dracula-chat
EMBEDDING_MODEL=all-MiniLM-L6-v2
TIMEZONE=UTC
```

> **Note**: Use **only SentenceTransformers-compatible models**

---

### 4. Start Qdrant Vector DB

Run Qdrant as a local service (via Docker or standalone binary):

```bash
docker run -p 6333:6333 qdrant/qdrant
```

> Make sure it’s reachable at `http://localhost:6333`.

---

### 5. Start the FastAPI backend

```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

### 6. Start the Streamlit frontend

```bash
streamlit run streamlit_app.py
```

---

### 6. Access the application

- **API Endpoint**: `http://<IP>:8000/chat`

- **Web UI**: `http://<IP>:8501`
    - **Chatbot** — Live interaction
    - **History** — Shows chat log entries
    - **Logs** — Reads structured logs in table format
    - **README** — Renders this file within app

---

## 📄 Example Request

```bash
curl -X POST http://<IP>:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I forgot my login info"}'
```

Response:
```json
{
  "reply": "To reset your password, click on 'Forgot Password' at the login page."
}
```

---

## 🗂 Project Structure

```
dracula-chat/
├── app/
│   ├── main.py            # FastAPI app
│   ├── vector.py          # Embedding + Qdrant
│   ├── fallback.py        # OpenAI fallback
│   ├── config.py          # .env loader
│   ├── logger.py          # JSONL logger
│   ├── faq.py             # Static FAQ dataset
├── streamlit_app.py       # Streamlit UI
├── requirements.txt       # Dependencies
├── .env.sample            # Sample environment vars
└── README.md              # You're here!
```

---

## 📚 Coming Soon

- [ ] Support for Open-source LLMs
- [ ] LangChain pipeline
- [ ] Mini RAG implementation
- [ ] Training models
- [ ] Containerization
- [ ] Better error handling
- [ ] Better UI dashboard

---

## 🤝 Collaboration

Dracula Chat is **open for feedback, collaboration, and extension**.  
Licensing will be added later.  
Feel free to fork, experiment, or reach out.

