# Agentic AI Series - Class 01

## **Introduction**

Welcome to the first class of the Agentic AI Series! In this session, we will focus on setting up your environment for building AI applications, including installing the necessary dependencies and configuring your project to interact with APIs such as **phidata** and **groq**. By the end of this class, you'll have the foundational setup ready to start working with advanced AI tools.

---

## **Step 1: Creating the Environment**

To get started, we'll create a Python environment using **Conda**. Run the following command to create the environment with Python version 3.13.1:

```bash
conda create -p venv python==3.13.1
```

When prompted, type `Yes` to proceed with the creation of the environment.

Once the environment is created, activate it using the following command:

```bash
conda activate venv
```

---

## **Step 2: Creating the `requirements.txt` File**

Next, we'll create a `requirements.txt` file to list all the dependencies for our project. Here’s what to include in your `requirements.txt`, with a brief explanation for each library:

```
phidata            # A Python library for working with phidata APIs
python-dotenv      # Loads environment variables from a .env file
yfinance           # Provides access to Yahoo Finance data
packaging          # A tool for packaging Python code
duckduckgo-search  # Allows search queries via DuckDuckGo
fastapi            # A web framework for building APIs quickly
uvicorn            # ASGI server for FastAPI applications
groq               # A library to interact with the groq API
openai             # Python client for OpenAI's GPT API
```

Now, install the dependencies by running:

```bash
pip install -r requirements.txt
```

---

## **Step 3: Setting Up Environment Variables**

We are using **python-dotenv** to manage environment variables. In your project directory, create a `.env` file that contains the API keys for **phidata** and **groq**.

```plaintext
PHI_API_KEY=""
GROQ_API_KEY=""
```

Make sure to replace the empty strings with your actual API keys. You can get the API keys by signing up on the respective platforms.

---

## **That's It for Today!**

With the environment set up, dependencies installed, and API keys configured, you're ready to move forward in the Agentic AI Series. In the next class, we’ll dive deeper into interacting with these APIs and building a simple application.

---

### **Notes:**

- Make sure to keep your `.env` file safe and never share it publicly.
- If you encounter any issues while setting up the environment or installing dependencies, double-check the Python version and the installation steps.

---

Happy coding, and see you in the next class! 😊