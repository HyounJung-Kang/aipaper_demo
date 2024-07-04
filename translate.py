# https://python.langchain.com/v0.1/docs/expression_language/get_started/
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 애플리케이션 제목 설정
st.title("번역기")

# 사이드바에 OpenAI API 키 입력 필드 추가
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요:", type="password")

# 요약할 텍스트 입력 필드 추가
text_to_summarize = st.text_area("번역할 텍스트를 입력하세요:", "")

# 프롬프트 템플릿 정의
template = """
당신은  번역 전문가입니다. 주어진 텍스트를 이해가 쉽도록 명확하게 번역해 주세요.
텍스트: {text}
요약:
"""
prompt = PromptTemplate.from_template(template)

# OpenAI 채팅 모델 초기화
if api_key:
    model = ChatOpenAI(
        model="gpt-4o",
        max_tokens=1024,
        temperature=0.5,
        api_key=api_key,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )

    # 문자열 출력 파서 초기화
    output_parser = StrOutputParser()

    # 프롬프트, 모델, 출력 파서를 연결하여 처리 체인 구성
    chain = prompt | model | output_parser

    # 버튼 클릭 시 체인 실행
    if st.button("번역 시작"):
        result = chain.invoke({"text": text_to_summarize})
        st.write("### 번역 결과:")
        st.write(result)
else:
    st.warning("사이드바에서 API 키를 입력하세요.")