from fastapi import HTTPException
from llm.llmTools.LlmTools import LlmTools
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS


class EmbedVectorFAISSTool(LlmTools):
    def main(self, userText, config):
        try:
            text = config.text 
            embed_model = OpenAIEmbeddings()

            # res = embed_model.embed_query(text)

            text_splitter = RecursiveCharacterTextSplitter(
                # Set a really small chunk size, just to show.
                chunk_size = 2000,
                chunk_overlap  = 0,
                length_function = len,
            )

            book_texts = text_splitter.create_documents([text])

            for i in range(0, len(book_texts)):
                book_texts[i].metadata["title"] = config.inputDocTitle

            db = FAISS.from_documents(book_texts, embed_model)
            db.save_local("/wanda-backend/faiss_index")

            return "success"
        except Exception as error:
            # handle the exception
            print("An exception occurred:", error) # An exception occurred: division by zero
            raise HTTPException(status_code=500, detail="Backend error")
        
