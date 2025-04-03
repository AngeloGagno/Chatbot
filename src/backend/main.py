from pathlib import Path
import streamlit as st
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv

from backend.configs import *

_ = load_dotenv(find_dotenv())


PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'

class Chain:

    def __init__(self):
        self.documento = self._importacao_documentos()
        self.criar_chain = self.cria_chain_conversa()
        
    def _chat_model(self):
        return ChatOpenAI(model=get_config('model_name'))
    
    def _importacao_documentos(self):
        documentos = []
        for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
            loader = PyPDFLoader(str(arquivo))
            documentos_arquivo = loader.load()
            documentos.extend(documentos_arquivo)
        return documentos

    def _split_de_documentos(self):
        recur_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2500,
            chunk_overlap=250,
            separators=["/n\n", "\n", ".", " ", ""]
        )
        documentos = recur_splitter.split_documents(self.documento)

        for i, doc in enumerate(documentos):
            doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
            doc.metadata['doc_id'] = i
        return documentos

    def _cria_vector_store(self):
        embedding_model = OpenAIEmbeddings()
        documentos = self._split_de_documentos()  
        vector_store = Chroma.from_documents(
            documents=documentos,
            embedding=embedding_model,
            persist_directory="chroma_db"
        )
        vector_store.persist()
        return vector_store
    
    def _retriever(self):
        retriever = self._cria_vector_store.as_retriever(
            search_type=get_config('retrieval_search_type'),
            search_kwargs=get_config('retrieval_kwargs')
        )
        return retriever
    
    def _memory(self):
        return ConversationBufferMemory(
            return_messages=True,
            memory_key='chat_history',
            output_key='answer'
            )
    
    def _prompt(self):
        return PromptTemplate.from_template(get_config('prompt'))
    
    def cria_chain_conversa(self):
        chat_chain = ConversationalRetrievalChain.from_llm(
            llm=self._chat_model(),
            memory=self._memory(),
            retriever=self._retriever(),
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={'prompt': self._prompt()}
        )

        st.session_state['chain'] = chat_chain
