Here’s the updated README for **LangChain Series: Class 2**, with the introduction, features, and notes sections added:

---

# LangChain Series: Class 2 - README

## **Introduction**

Welcome to the second class of the LangChain Series! In this session, we build upon the foundations established in Class 1. We'll focus on creating more advanced LangChain-based applications by integrating multiple prompt templates, sequential chains, and memory buffers. The goal is to develop a **celebrity search application** that showcases LangChain's capabilities in dynamic prompt management and interactive conversation.

---

## **Step 1: Creating `practice.py`**

Start by creating a new Python file called `practice.py`. You will use this file to experiment with LangChain concepts.  

---

### **Step 2: Building a Celebrity Search Application**

The first task is to use **Prompt Templates** to create a basic celebrity search application.

```python
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Template
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))
```

---

### **Step 3: Combining Multiple Prompt Templates**

Now, extend your application to use multiple prompt templates by combining them.

```python
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

parent_chain = SimpleSequentialChain(chain=[chain, chain2], verbose=True)

if input_text:
    st.write(parent_chain.run(input_text))
```

---

### **Step 4: Switching to SequentialChain**

To include intermediate outputs, replace `SimpleSequentialChain` with `SequentialChain`.

```python
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

parent_chain = SequentialChain(chain=[chain, chain2], input_variable=['name'], output_variables=['person', 'dob'], verbose=True)

if input_text:
    st.write(parent_chain({'name': input_text}))
```

---

### **Step 5: Adding a Third Prompt Template**

Add a third prompt template to the chain to extract major world events around the celebrity's birth year.

```python
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description')

parent_chain = SequentialChain(chain=[chain, chain2, chain3], input_variable=['name'], output_variables=['person', 'dob', 'description'], verbose=True)

if input_text:
    st.write(parent_chain({'name': input_text}))
```

---

### **Step 6: Adding Memory Buffers**

Finally, implement memory buffers to retain conversation history.

```python
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world"
)

# Memory Buffers
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=descr_memory)

parent_chain = SequentialChain(chain=[chain, chain2, chain3], input_variable=['name'], output_variables=['person', 'dob', 'description'], verbose=True)

if input_text:
    st.write(parent_chain({'name': input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(descr_memory.buffer)
```

---

## **Features**

- **Prompt Templates**: Design dynamic prompts for specific tasks.
- **Sequential Chains**: Process tasks sequentially with intermediate outputs.
- **Memory Buffers**: Retain context and enhance conversational applications.

---

## **Notes**

- Remember to replace `openai_key` in `constants.py` with your OpenAI API key.
- Customize prompts to suit your application needs.
- Experiment with different chain configurations to unlock more complex workflows.

---

Enjoy building intelligent applications with LangChain! 😊