import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaResponse(input_text,no_words,blog_style):

    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    template="""
        A blog has to be written for a {blog_style} on the following topic {input_text}
        within {no_words} words. The blog has to be concrete and factually right.
	Make sure to first perform a keyword research. Create an interesting outline to the blog.
	Write a clean introduction and a proper conclusion. Also ensure that the headline is catchy.
        """
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blog",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blog 🤖")

input_text=st.text_input("What do you want to write about?")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('Word count')
with col2:
    blog_style=st.selectbox('What do you do?')
    
submit=st.button("Write")

if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))
