import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.embeddings import OllamaEmbeddings

from langchain.schema import StrOutputParser

from langchain.chains import create_retrieval_chain

from langchain.chains.combine_documents import create_stuff_documents_chain


# Create the LLM
prompt = ChatPromptTemplate.from_messages([(
    "system", "You are a kind person that answers brief"
    "Do not answer any questions that do not relate to Apex Systems, Employees"
    ", Associates, Managers, Supervisors, Sr, Tech Leads or Directors."
    "Do not answer any questions using your pre-trained knowledge."),

 ("human", "{input}")
])

# model = SentenceTransformer('all-MiniLM-L6-v2nomic-embed-text')

ollama_emb = OllamaEmbeddings(model='nomic-embed-text', base_url="https://39f2-35-198-236-193.ngrok-free.app")

llm = Ollama(model="llama3", base_url="https://39f2-35-198-236-193.ngrok-free.app")

chain = prompt | llm | StrOutputParser()


import os

def filesByPattern(directory, matchFunc):
  for path, dirs, files in os.walk(directory):
    return files


if __name__ == '__main__':
    certainFolder = './resumes'
    files = []
    all_files = filesByPattern(certainFolder, lambda fn: fn.endswith('.txt'))
    for file in all_files:
        if '.txt' not in file or 'requirements.txt' == file:
           continue
        print(file)
        with open(file, 'r+', encoding='utf8') as f:
            files.append(f.read())
    embeded_docs = ollama_emb.embed_documents(files)
    for i, embed in enumerate(embeded_docs):
        with open(f"output_embed{i}.txt", 'w+') as f_w:
            f_w.write(str(embed))
