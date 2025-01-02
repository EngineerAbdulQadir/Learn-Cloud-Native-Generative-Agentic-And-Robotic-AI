# Agentic AI Series - Class 02

## **Introduction**

Welcome to Class 02 of the Agentic AI Series! In this session, we will focus on creating and configuring agents for financial and web search tasks. We will also integrate these agents with the Phi Data Platform and set up a playground to test and interact with them. By the end of this class, you'll have a fully functional AI application running locally and integrated with external APIs.

---

## **Step 1: Creating `financial_agent.py`**

Create a new file named `financial_agent.py` and add the following code:

```python
# Libraries
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Multi Modal Agent
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
```

### **Running the Agent**

To run the `financial_agent.py`, enter the following command in the terminal:

```bash
python financial_agent.py
```

<h2>Output</h2>
<h4>Thinking -</h4>
<a href="https://ibb.co/r0VqXv9"><img src="https://i.ibb.co/7CqB0bh/Summarizing.png" alt="Summarizing" border="0"></a>
<h4>Response -</h4>
<a href="https://ibb.co/ft2XRLj"><img src="https://i.ibb.co/HYVKv35/Response.png" alt="Response" border="0"></a>
<h4>Latest News -</h4>
<a href="https://ibb.co/q1kBSvy"><img src="https://i.ibb.co/F7g6rFx/Latest-News.png" alt="Latest-News" border="0"></a>


---

## **Step 2: Integrating with Phi Data Platform**

Create another file named `playground.py` with the following code:

```python
import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
import os
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Playground
app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
```

### **Running the Agent**

To run the `playground.py`, enter the following command in the terminal:

```bash
python playground.py
```
<h2>Output</h2>
<h4>Response After IWPDP -</h4>
<a href="https://ibb.co/sCLwQmF"><img src="https://i.ibb.co/MfqVp2R/Response-After-IWPDP.png" alt="Response-After-IWPDP" border="0"></a>

---

## **Step 3: Accessing the Playground**

Once the playground is running, it will be hosted on `localhost:7777`. If it doesn't work, follow these steps:

1. Navigate to the Phi Data dashboard.
2. Go to **Playground > Select an Endpoint**.
3. Select the localhost endpoint and ensure it shows a green signal.
4. Test the application by making queries.

---

## **Class Summary**

By the end of this class, you will have:

- Created agents for financial and web search tasks.
- Integrated these agents with the Phi Data Platform.
- Tested your application using the Phi Playground.

---

### **Notes**

- Ensure all dependencies from Class 01 are installed.
- Keep API keys secure and never share them publicly.

---

Happy coding! See you in the next class! 😊