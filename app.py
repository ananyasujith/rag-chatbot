from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from flask import Flask, request, jsonify

embed = HuggingFaceEmbeddings()
db = FAISS.load_local("vector_store", embed)

llm = OpenAI(api_key="YOUR_OPENAI_KEY")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json["query"]

    docs = db.similarity_search(query, k=3)
    context = " ".join([d.page_content for d in docs])

    prompt = f"Use this context:\n{context}\n\nAnswer the question:\n{query}"

    response = llm(prompt)

    return jsonify({"response": response})

app.run(port=5000)
