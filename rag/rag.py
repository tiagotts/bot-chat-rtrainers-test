import os
import traceback

from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_huggingface import HuggingFaceEmbeddings

os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
if __name__ == '__main__':
    try:
        file_path = './rag/data/prompt_rtrainers.md'
        loader = UnstructuredMarkdownLoader(file_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        chunks = text_splitter.split_documents(
            documents=docs,
        )

        persist_directory = './chroma_data'
        os.makedirs(persist_directory, exist_ok=True)

        embedding = HuggingFaceEmbeddings()
        vector_store = Chroma(
            embedding_function=embedding,
            persist_directory=persist_directory,
        )
        vector_store.add_documents(
            documents=chunks,
        )
    except Exception as e:
        print(f"Erro capturado: {e}")
        traceback.print_exc()
