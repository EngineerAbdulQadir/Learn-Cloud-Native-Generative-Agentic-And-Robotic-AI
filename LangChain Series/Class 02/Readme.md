# LangChain Series - Class 02

## **Introduction**

Welcome to the second class of the LangChain Series! In this session, we build upon the foundations established in Class 1. We'll focus on creating more advanced LangChain-based applications by integrating multiple prompt templates, sequential chains, and memory buffers. The goal is to develop a **celebrity search application** that showcases LangChain's capabilities in dynamic prompt management and interactive conversation.

---

## **Step 1: Creating `practice.py`**

Start by creating a new Python file called `practice.py`. This will be where you experiment with LangChain concepts.

```python
# practice.py
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")


# OpenAI LLMs
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(chain.run(input_text))
```


---

## **Step 2: Building the Celebrity Search Application**

Now we’ll create a prompt template for searching celebrity details.

```python
# practice.py (Step 2)
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Template for celebrity search
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

### **Output Section**
<h4>Asking -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/LZNqd6w/STEP-TWO-1.png" alt="STEP-TWO-1" border="0"></a>
<h4>Output -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/gZGGt63/STEP-TWO-2.png" alt="STEP-TWO-2" border="0"></a>

---

## **Step 3: Combining Multiple Prompt Templates**

In this step, we’ll combine two different prompt templates to handle multiple queries.

```python
# practice.py (Step 3)
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Template for celebrity search
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Prompt Template for birth date
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

if input_text:
    st.write(chain.run(input_text))
    st.write(chain2.run(chain.run(input_text)))
```

### **Output Section**
<h4>Asking -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/HzPbbYr/STEP-THREE-1.png" alt="STEP-THREE-1" border="0"></a>
<h4>Output -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/5kc0nbd/STEP-THREE-2.png" alt="STEP-THREE-2" border="0"></a>

---

## **Step 4: Switching to SequentialChain**

In this step, we use a SequentialChain to process multiple prompts in sequence.

```python
# practice.py (Step 4)
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

# Prompt Template for celebrity search
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Prompt Template for birth date
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

parent_chain = SequentialChain(
    chains=[chain, chain2],
    input_variables=['name'],
    output_variables=['person', 'dob'],
    verbose=True
)

if input_text:
    st.write(parent_chain({'name': input_text}))
```

### **Output Section**
<h4>Output -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/gZwhb91/STEP-FOUR-1.png" alt="STEP-FOUR-1" border="0"></a>

---

## **Step 5: Adding a Third Prompt Template**

We add a third template to include even more detailed information.

```python
# practice.py (Step 5)
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

# Prompt Template for celebrity search
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Prompt Template for birth date
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

# Prompt Template for major events
third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world."
)

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description')

parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

if input_text:
    st.write(parent_chain({'name': input_text}))
```

### **Output Section**
<h4>Asking -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/7493016/STEP-FIVE-1.png" alt="STEP-FIVE-1" border="0"></a>
<h4>Output -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/Byn6TVg/STEP-FIVE-2.png" alt="STEP-FIVE-2" border="0"></a>

---

## **Step 6: Adding Memory Buffers**

Now we’ll add memory buffers to retain the conversation context between each step.

```python
# practice.py (Step 6)
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
st.title('Celebrity Search Application')
input_text = st.text_input("Enter Anything You Want To Ask?")

# Prompt Template for celebrity search
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Prompt Template for birth date
second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

# Prompt Template for major events
third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world."
)

# Memory Buffers
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='dob_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# OpenAI LLMs
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=descr_memory)

# Sequential chain
parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

if input_text:
    st.write(parent_chain({'name': input_text}))

    # Expander for memory history
    with st.expander('Person History'):
        st.info(person_memory.buffer)

    with st.expander('Major Events History'):
        st.info(descr_memory.buffer)

```

### **Output Section**
<h4>Output -</h4>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/Fwbpjjg/STEP-SIX-1.png" alt="STEP-SIX-1" border="0"></a>

---

## **Features**

- **Prompt Templates**: Create dynamic and customized prompts for different tasks.
- **Sequential Chains**: Process multiple prompts in sequence for complex workflows.
- **Memory Buffers**: Retain context to enhance the user experience in interactive applications.

---

## **Notes**

- Remember to replace `openai_key` in `constants.py` with your OpenAI API key.
- You can adjust the prompt templates based on your needs.
- The memory buffers allow you to track and utilize prior interactions for more meaningful results.

---

Enjoy building intelligent applications with LangChain! 😊