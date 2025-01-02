# Agentic AI Series - Class 04  

## Building End-to-End Agentic AI RAG with Langflow and DataStax VectorDB  

This project demonstrates the process of building a Retrieval-Augmented Generation (RAG) system using Langflow, Groq API, DataStax VectorDB, and additional integrations like DuckDuckGo and PDF handling.

---

### Prerequisites  

- Langflow account ([Sign up here](https://langflow.org/))  
- Groq API Key  
- DataStax VectorDB account  
- NVIDIA embedding model  
- Basic understanding of Langflow components  

---

### Steps to Build  

#### 1. **Set up Langflow**  
   - Go to the [Langflow website](https://langflow.org) and sign up.  
   - After signing up, switch from **Astra** to **Langflow**.  

#### 2. **Create a New Flow**  
   - Click on "New Flow" and select "Blank Flow."  
   - Open the **Components** section on the left.

#### 3. **Add Components**  
   - Drag **Chat Input** (from Input section).  
   - Drag **Chat Output** (from Output section).  
   - Drag **Agent** (from Agent section) and rename it to `Recipe Chef`.  
     - Set:
       - **Model Provider**: Groq  
       - **Agent Instruction**: `You are a helpful assistant that can use tools to answer questions and perform tasks.`  
     - Set up your **Groq API Key**.  
   - Add another **Agent** for extended functionality.  

#### 4. **Design Prompt**  
   - From the **Template section**, add the following prompt:  
     ```plaintext
     Your goal is to answer the question asked from the company database. Use RAG to fetch the details and provide the most relevant output. 

     Question: {question}

     In your response, incorporate the recipe points: {results}
     ```  
   - Check and save your configuration.

#### 5. **Connect Components**  
   - Connect the components as follows:  
     - `Chat Input` → `Message Point` → `Agent` → `Question Point`  
     - `Prompt` → `Prompt Message Point` → `Agent` → `Agent Instruction Point`  
     - `Agent` → `Response Point` → `Recipe Chef` → `Input Point`  
     - `Recipe Chef` → `Response Point` → `Chat Output` → `Text Point`  

#### 6. **Integrate Vector Database**  
   - Drag **Astra DB** into the flow from the **Vector Stores** section.  
   - Create a database and a collection.  
   - Connect:  
     - `Chat Input` → `Message Point` → `Astra DB` → `Search Input`  

#### 7. **Set Up Embedding Models**  
   - Use the default embedding model **Astra Vectorize**.  
   - Select the embedding provider **NVIDIA** (no need to select another model).

#### 8. **Add Parsing and File Handling**  
   - Drag **Parse Data** from the **Processing** section.  
     - Connect:
       - `Astra DB` → `Search Results Point` → `Parse Data` → `Data Point`  
       - `Parse Data` → `Text Point` → `Prompt` → `Results Point`  
   - Drag **File** and **Split Text** components:  
     - Connect:
       - `File` → `Data Point` → `Split Text` → `Data Inputs Point`  
   - Drag another **Astra DB** for ingestion:
     - Connect:
       - `Split Text` → `Chunks Point` → `Astra DB (2)` → `Ingest Data Point`  

#### 9. **Test with Uploaded File**  
   - Upload a file in the **File** component.  
   - Start **Astra DB (2)** and verify the output.  

#### 10. **DuckDuckGo Integration**  
   - Drag **DuckDuckGo Search**:  
     - Connect:
       - `Chat Input` → `Message Point` → `DuckDuckGo Search` → `Search Query`  
       - `DuckDuckGo Search` → `Tool Point` → `Recipe Agent` → `Tools Point`  

#### 11. **Test in Playground**  
   - Open the Playground.  
   - Test the system with user prompts. For example:  
     ```plaintext
     User: Direction to make Som Tum.  
     <h2>Output</h2>
     <h4>Running -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/9gCQt0q/Running.png" alt="Running" border="0"></a>  
     ```

---

### Results  

By following these steps, you will have a fully functional RAG system integrated with Langflow, Groq API, Astra VectorDB, and DuckDuckGo. This system can process user queries, fetch data from the database, and provide relevant responses.

---

### Features Added in Class 04  

- Enhanced **Agentic AI RAG System** with multi-agent setup.  
- Integration with **DataStax VectorDB** for storage and retrieval.  
- Support for **PDF handling** with Astra DB ingestion.  
- Added **DuckDuckGo Search** for web-based queries.

---

### Next Steps  

- Continue testing and refining the agent in the Playground.  
- Experiment with additional Langflow components.  

---  
 

Happy Building! 🚀