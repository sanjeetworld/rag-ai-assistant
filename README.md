# 🚀 RAG AI Assistant (Free Version)

A Retrieval-Augmented Generation (RAG) based AI system that answers questions from PDF documents using local embeddings (no API key required).

---

## 📌 Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using FAISS
* 🤖 AI-based question answering from document context
* 💰 Fully FREE (no OpenAI API required)
* ⚡ FastAPI backend with Swagger UI

---

## 🧠 Tech Stack

* Python
* FastAPI
* LangChain
* FAISS (Vector Database)
* Hugging Face Embeddings (`sentence-transformers`)

---

## 📁 Project Structure

```
rag-ai-assistant/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── data/
│    └── python-machine-learning-2nd.pdf
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/rag-ai-assistant.git
cd rag-ai-assistant
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
uvicorn app:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## ❓ How to Use

1. Start the server
2. Open `/docs`
3. Use `/ask/` endpoint
4. Enter your question

### Example:

```
What is machine learning?
```

---

## 📊 Example Output

```
{
  "answer": "Answer from PDF: Machine learning is a subset of AI..."
}
```

---

## ⚠️ Notes

* No API key required
* First run may take time (model download)
* Works fully offline after setup

---

## 🚀 Future Improvements

* ChatGPT-like UI
* Multi-PDF support
* Voice input/output
* Deployment on cloud

---

## 👨‍💻 Author

**Sanjeet Kumar**
AI/ML Engineer | Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
