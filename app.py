from fastapi import FastAPI
from rag_pipeline import create_vector_store, get_answer
import os

app = FastAPI()

# Run only once (avoid re-creating every time)
@app.on_event("startup")
def startup_event():
    if not os.path.exists("vectorstore"):
        create_vector_store()

# Ask question API
@app.get("/ask/")
def ask_question(query: str):
    answer = get_answer(query)
    return {"answer": answer}
