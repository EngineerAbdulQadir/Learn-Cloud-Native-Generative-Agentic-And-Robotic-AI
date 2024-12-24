# Langchain Series - Class 01

### Introduction
Welcome to the first class of the **Langchain Series**! In this session, we set up a Python-based project using **Langchain** and **Streamlit**, leveraging the OpenAI API to build a simple demo application.

---

### Requirements
1. **Anaconda** installed on your system.
2. **Python 3.13.1** or compatible.
3. **OpenAI API Key**.

---

### Setup Instructions

#### Step 1: Create and Activate Environment
1. Open Command Prompt (CMD).
2. Run the following commands:

   ```bash
   conda create -p myenv python=3.13.1 -y
   conda activate myenv
   ```

---

#### Step 2: Prepare `requirement.txt`
1. Create a file named `requirement.txt` with the following content:
   ```
   openai
   langchain
   streamlit
   ```
2. Install the required packages:
   ```bash
   pip install -r requirement.txt
   ```

---

#### Step 3: Add Constants
1. Create a file named `constants.py` with the following content:
   ```python
   openai_key = 'Your API Key'
   ```
   Replace `'Your API Key'` with your actual OpenAI API key.

---

#### Step 4: Create Main Application
1. Create a file named `main.py` with the following code:

   ```python
   import os
   from constants import openai_key
   from langchain.llms import OpenAI

   import streamlit as st

   os.environ["OPENAI_API_KEY"] = openai_key

   # Streamlit framework
   st.title('Langchain Demo With OPENAI API')
   input_text = st.text_input("Search the topic you want")

   # OpenAI LLMs
   llm = OpenAI(temperature=0.8)

   if input_text:
       st.write(llm(input_text))
   ```

---

#### Step 5: Run the Application
1. Run the following command in your terminal:
   ```bash
   streamlit run main.py
   ```
2. Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.

---

### Features
- **Interactive Input**: Users can type a query into the input box.
- **LLM Response**: The application uses Langchain and OpenAI's API to generate a response based on the input.

---

### Notes
- Ensure your OpenAI API key has sufficient credits to test the application.

---

Enjoy building intelligent applications with Langchain! 😊