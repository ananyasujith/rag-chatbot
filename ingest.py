from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/documents.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

embed = HuggingFaceEmbeddings()

db = FAISS.from_documents(chunks, embed)
db.save_local("vector_store")

print("Vector DB created!")
