from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(pdf_paths):
    documents = []

    for path in pdf_paths:
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("vectorstore")


def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("vectorstore", embeddings)


def retrieve_docs(query):
    vectorstore = load_vector_store()
    return vectorstore.similarity_search(query)