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

# Sequential chain with corrected parameters
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
