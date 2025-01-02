# Project 1: LangChain Hello World Project

### LangChain Is A Python Library
"""

!pip install langchain

"""### LangChain Software Development Kit"""

!pip install langchain-google-genai # LangChain SDK

"""### Importing LangChain SDK As GenAI"""

import langchain_google_genai as genai

"""### Importing Google Generative AI Chat From LangChain SDK"""

from langchain_google_genai import ChatGoogleGenerativeAI

"""### Granting Access To API Key"""

from google.colab import userdata
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

"""### Selecting Model And API Key"""

model = langchain_google_genai = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    api_key=GOOGLE_API_KEY
)

"""### Taking Response"""

response = model.invoke("What is the founder of PIAIC?")

"""### Printing Response"""

print(response.content)

"""# Aggregated Chunks"""

!pip install langchain
!pip install langchain-google-genai

import langchain_google_genai as genai

from langchain_google_genai import ChatGoogleGenerativeAI

from google.colab import userdata
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

model = langchain_google_genai = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    api_key=GOOGLE_API_KEY
)

response = model.invoke("What is the founder of PIAIC?")

print(response.content)

"""## The End...

"""