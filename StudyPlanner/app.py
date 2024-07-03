import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getStudyPlan(subject, hours_per_week, study_goals, learning_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256, 'temperature':0.6})
    template = """
        Create a study plan for {subject} with {hours_per_week} hours of study per week. 
        The study plan should aim to achieve the following goals: {study_goals}. 
        The plan should be tailored to a {learning_style} learning style. 
        Include a weekly breakdown of topics, recommended resources, and tips for effective studying.
        """
    prompt = PromptTemplate(input_variables=["subject", "hours_per_week", "study_goals", "learning_style"], template=template)
    response = llm(prompt.format(subject=subject, hours_per_week=hours_per_week, study_goals=study_goals, learning_style=learning_style))
    print(response)
    return response

st.set_page_config(page_title="Study Plan Generator",
                   page_icon='📚',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Study Plan Generator 📚")

subject = st.text_input("Enter the subject you want to study:")
hours_per_week = st.number_input("Enter hours per week:", min_value=1, max_value=40)
study_goals = st.text_area("Enter your study goals:")
learning_style = st.selectbox("Select your learning style:", ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"])

submit = st.button("Generate Study Plan")

if submit:
    st.write(getStudyPlan(subject, hours_per_week, study_goals, learning_style))
