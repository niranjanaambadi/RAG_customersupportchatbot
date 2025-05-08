Here’s a **quickstart guide** for running and deploying the RAG Customer Support Chatbot locally or via Docker.

---

## ✅ **Local Setup**

### 1. **Install Dependencies**

In your terminal:

```bash
cd rag_customer_support_chatbot
python3 -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

### 2. **Set Your OpenAI API Key**

Create a file named `.env` in the project root:

```bash
echo "OPENAI_API_KEY=your_openai_key_here" > .env
```

Make sure your OpenAI key is valid and the environment loads it.

---

### 3. **Run the CLI Chatbot**

```bash
python app/chatbot.py
```

You’ll be able to chat via the command line.

---

### 4. **Run the Streamlit App**

```bash
streamlit run app/streamlit_ui.py
```

Open your browser at `http://localhost:8501`.

---

### 5. **Run the API with FastAPI**

```bash
uvicorn app.api:app --reload
```

Your API will be live at `http://127.0.0.1:8000/ask`.

---

## 🐳 **Docker Deployment**

### 1. **Build the Docker Image**

```bash
docker build -t rag-chatbot .
```

### 2. **Run the Container**

Make sure to pass your OpenAI key into the environment:

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your_openai_key_here rag-chatbot
```

Streamlit will be accessible at `http://localhost:8501`.

---

