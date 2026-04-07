# setx OPENAI_API_KEY "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"


from fastapi import FastAPI, UploadFile, File
from rag_pipeline import create_vector_store, get_answer

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = f"data/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    create_vector_store(file_location)
    return {"message": "PDF processed successfully"}

@app.get("/ask/")
def ask_question(query: str):
    answer = get_answer(query)
    return {"answer": answer}