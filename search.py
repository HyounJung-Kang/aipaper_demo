import streamlit as st
import requests

def fetch_papers_from_paperswithcode(query, max_results):
    base_url = 'https://paperswithcode.com/api/v1/papers/'
    params = {
        'q': query,
        'page_size': max_results
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        papers = response.json().get('results', [])
        return papers
    else:
        return None

def papers_with_code_search():
    st.title('Papers with Code 논문 검색')
    query = st.text_input('논문 검색어 입력')
    max_results = st.number_input('결과 수', min_value=1, max_value=100, value=10)
    if query:
        st.write(f"'{query}'에 대한 논문 검색 결과를 표시합니다.")
        papers = fetch_papers_from_paperswithcode(query, max_results)
        if papers:
            for paper in papers:
                st.subheader(paper['title'])
                st.write(paper['abstract'])
                if paper.get('code_url'):
                    st.write(f"[코드 링크]({paper['code_url']})")
                else:
                    st.write("코드가 없습니다.")
        else:
            st.write("검색 결과가 없습니다.")

if __name__ == "__main__":
    papers_with_code_search()
