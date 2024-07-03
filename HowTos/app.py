import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaResponse(input_text,concept,who):

    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    template="""
	Write a how to tutorial on the {input_text}, to ensure we are on the same page, the  concept is {concept}. The style has to be clear and understandable to a {who}.
	Make sure the how to tutorial that you write is factually correct. Write it in points, feel free to use subpoints to make it easier to understand and follow.
	"""
    prompt=PromptTemplate(input_variables=["who","input_text",'concept'],
                          template=template)
    response=llm(prompt.format(who=who,input_text=input_text,concept=concept))
    print(response)
    return response


st.set_page_config(page_title="How To",
                    page_icon='❓',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("How To ❓")

input_text=st.text_input("How to ...")

col1,col2=st.columns([5,5])

with col1:
    concept=st.text_input('Concept')
with col2:
    who=st.selectbox('What do you do?')
    
submit=st.button("How To")

if submit:
    st.write(getLLamaResponse(input_text,concept,who))
