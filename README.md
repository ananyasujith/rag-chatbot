# 📌 Retrieval-Augmented Generation (RAG) Chatbot

A GenAI chatbot that uses RAG to generate accurate and context-aware answers using
FAISS vector search + LLMs.

## 🚀 Features
- Document ingestion and chunking
- Embedding generation using HuggingFace
- FAISS vector database for semantic search
- RAG pipeline: Retrieve → Generate
- Flask API for chatbot usage

## 🗂️ Project Structure
rag-chatbot/
│── app.py
│── ingest.py
│── vector_store/
│── data/
│   └── documents.pdf
│── requirements.txt

## 🧠 How It Works
1. Documents are split into chunks  
2. Embeddings created using HF models  
3. Stored in FAISS vector DB  
4. User query → semantic search → nearest chunks  
5. LLM generates answer using retrieved context  

## ▶️ Run
pip install -r requirements.txt  
python ingest.py  
python app.py

## 📘 Model Used
- HuggingFace Embeddings
- OpenAI GPT / HuggingFace LLM
