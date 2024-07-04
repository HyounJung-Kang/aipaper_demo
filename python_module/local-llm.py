from langchain_openai import ChatOpenAI
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="teddylee777/EEVE-Korean-Instruct-10.8B-v1.0-Q8_0.gguf",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

prompt = PromptTemplate.from_template(
    """You are a helpful, smart, kind and efficient AI assistant. You always fullfill the user's requests to the best of your ability.
    You must generate an answer in Korean.

    #Question:
    {question}

    #Answer:"""
)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"question": "서울?"})

print(response)