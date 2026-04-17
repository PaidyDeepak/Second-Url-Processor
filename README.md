It collects data from the url's given by the user and answers user's query.
# 🧠 Deepak: News Research Tool

A powerful **RAG-based (Retrieval-Augmented Generation)** web application that allows users to extract insights from news articles by simply providing URLs and asking questions.

Built using **Streamlit, LangChain, ChromaDB, and Gemini AI**.

---

## 🚀 Features

* 🔗 Input multiple news article URLs
* 📰 Automatic web scraping and content extraction
* ✂️ Intelligent text chunking and deduplication
* 🧠 Hybrid retrieval:

  * Semantic search (vector embeddings)
  * Keyword search (BM25)
* 🤖 AI-powered answers using Google Gemini
* ⚡ Fast and interactive UI with Streamlit

---

## 🏗️ Architecture

1. **Scraping**

   * Extracts full text from URLs using Scrapling

2. **Processing**

   * Splits text into chunks
   * Removes duplicate content

3. **Storage**

   * Stores embeddings in ChromaDB
   * Saves documents for BM25 retrieval

4. **Retrieval (Hybrid Search)**

   * Combines:

     * Vector similarity search
     * BM25 keyword search

5. **Generation**

   * Uses Gemini to generate contextual answers

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **LLM**: Google Gemini
* **Vector DB**: ChromaDB
* **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
* **Retrieval**: LangChain (BM25 + EnsembleRetriever)
* **Web Scraping**: Scrapling

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-research-tool.git
cd news-research-tool
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Enter 1–3 news article URLs in the sidebar
2. Click **"Process"**
3. Wait for indexing to complete
4. Ask questions about the articles
5. Get detailed AI-generated answers

---

## 📁 Project Structure

```
.
├── app.py              # Streamlit UI
├── main.py             # Scraping + indexing
├── rag.py              # Retrieval + generation
├── requirements.txt
├── scraped3.json       # Stored scraped data
├── docs.pkl            # Processed documents
└── vector_db/          # Chroma database
```

---

## ⚠️ Notes

* Works best with **news/blog articles**
* Avoid very short or JavaScript-heavy pages
* First run may take time due to embedding generation

---

## 🔥 Future Improvements

* ✅ Add reranking for better accuracy
* ⚡ Optimize retrieval speed
* 💬 Add conversational memory
* 🌐 Deploy online (Streamlit Cloud / Render)
* 📊 Source highlighting in answers

---

## 👨‍💻 Author

**Deepak Paidy**

* GitHub: https://github.com/PaidyDeepak


---

## ⭐ If you like this project

Give it a star ⭐ and share it!
