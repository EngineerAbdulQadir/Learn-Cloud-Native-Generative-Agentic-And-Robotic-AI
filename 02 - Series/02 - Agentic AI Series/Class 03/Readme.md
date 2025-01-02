# Agentic AI Series - Class 03

## **Introduction**

Welcome to Class 03 of the Agentic AI Series! In this session, we are building a Multi-Agentic AI Retrieval-Augmented Generation (RAG) system with a Vector Database. By the end of this class, you will have a functional PDF assistant powered by a vector database and Groq API.

---

## **Step 1: Setting Up the Environment**

1. **Create and activate the Python environment.**

2. **Create `requirements.txt`**  
   Add the following libraries:
   ```plaintext
   phidata
   python-dotenv
   yfinance
   packaging
   duckduckgo-search
   fastapi
   uvicorn
   groq
   openai
   sqlalchemy
   pgvector
   psycopg[binary]
   pypdf
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Step 2: Configuring Groq API**

1. Create a file named `.env`.
2. Add the Groq API Key:
   ```plaintext
   GROQ_API_KEY=""
   ```

---

## **Step 3: Building `pdf_assistant.py`**

1. Create a new file named `pdf_assistant.py`.
2. Add the following code:

   ```python
   import typer
   from typing import Optional, List
   from phi.assistant import Assistant
   from phi.storage.assistant.postgres import PgAssistantStorage
   from phi.knowledge.pdf import PDFUrlKnowledgeBase
   from phi.vectordb.pgvector import PgVector2

   import os
   from dotenv import load_dotenv
   load_dotenv()

   os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

   db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

   knowledge_base = PDFUrlKnowledgeBase(
       urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
       vector_db=PgVector2(collection="recipes", db_url=db_url)
   )

   knowledge_base.load()

   storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)

   def pdf_assistant(new: bool = False, user: str = "user"):
       run_id: Optional[str] = None

       if not new:
           existing_run_ids: List[str] = storage.get_all_run_ids(user)
           if len(existing_run_ids) > 0:
               run_id = existing_run_ids[0]

       assistant = Assistant(
           run_id=run_id,
           user_id=user,
           knowledge_base=knowledge_base,
           storage=storage,
           show_tool_calls=True,
           search_knowledge=True,
           read_chat_history=True,
       )
       if run_id is None:
           run_id = assistant.run_id
           print(f"Started Run: {run_id}\n")
       else:
           print(f"Continuing Run: {run_id}\n")

       assistant.cli_app(markdown=True)

   if __name__ == "__main__":
       typer.run(pdf_assistant)
   ```

---

## **Step 4: Setting Up PostgreSQL with Docker**

1. Open Docker and VS Code.
2. Open Git Bash terminal in VS Code.
3. Run the following command to start PostgreSQL with pgvector:
   ```bash
   docker run -d \
     -e POSTGRES_DB=ai \
     -e POSTGRES_USER=ai \
     -e POSTGRES_PASSWORD=ai \
     -e PGDATA=/var/lib/postgresql/data/pgdata \
     -v pgvolume:/var/lib/postgresql/data \
     -p 5532:5432 \
     --name pgvector \
     phidata/pgvector:16
   ```

---

## **Step 5: Running the PDF Assistant**

1. Open the command prompt.
2. Run the following command:
   ```bash
   python pdf_assistant.py
   ```

<h2>Output</h2>
<h4>Running -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/9gCQt0q/Running.png" alt="Running" border="0"></a>
<h4>User Prompt 01 -</h4>
<a href="https://ibb.co/jR4xZYH"><img src="https://i.ibb.co/JQkbFTC/User-01.png" alt="User-01" border="0"></a>
<h4>User Prompt 02 -</h4>
<a href="https://ibb.co/SKDBGYW"><img src="https://i.ibb.co/19YTjyh/User-02.png" alt="User-02" border="0"></a>

---

## **Class Summary**

By the end of this class, you will have:

- Set up a Multi-Agentic AI RAG system with a vector database.
- Built a PDF assistant powered by Groq API and PostgreSQL with pgvector.

---

### **Notes**

- Keep API keys secure and never share them publicly.
- Ensure Docker is installed and running before starting PostgreSQL.

---

Happy coding! See you in the next class! 😊