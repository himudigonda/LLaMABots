import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getSummary(news_article, keyword_focus, summary_length):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256, 'temperature':0.01})
    template = """
        Summarize the following news article: {news_article}. 
        The summary should focus on the following keywords: {keyword_focus}. 
        The length of the summary should be approximately {summary_length} words. 
        Ensure the summary captures the main points and is concise.
        """
    prompt = PromptTemplate(input_variables=["news_article", "keyword_focus", "summary_length"], template=template)
    response = llm(prompt.format(news_article=news_article, keyword_focus=keyword_focus, summary_length=summary_length))
    print(response)
    return response

st.set_page_config(page_title="News Summarizer",
                   page_icon='📰',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("News Summarizer Bot 📰")

news_article = st.text_area("Paste the news article here:")
keyword_focus = st.text_input("Enter keywords to focus on:")
summary_length = st.number_input("Desired summary length (words):", min_value=50, max_value=300)

submit = st.button("Summarize")

if submit:
    st.write(getSummary(news_article, keyword_focus, summary_length))
