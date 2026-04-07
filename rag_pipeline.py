from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# ✅ Create vector store
def create_vector_store():
    pdf_path = "data/python-machine-learning-2nd.pdf"

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("vectorstore")


# ✅ Load vector store
def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("vectorstore", embeddings)


# ✅ Get answer
def get_answer(query):
    vectorstore = load_vector_store()
    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI()

    prompt = f"""
Answer only from the given context.

Context:
{context}

Question:
{query}
"""
    
    
    return llm.invoke(prompt)