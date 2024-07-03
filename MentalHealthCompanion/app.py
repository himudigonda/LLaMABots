
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getMentalHealthAdvice(current_mood, recent_activities, specific_concerns):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256, 'temperature':0.5})
    template = """
        Provide advice and resources for someone who is currently feeling: {current_mood}. 
        Consider their recent activities: {recent_activities}. 
        Address these specific concerns: {specific_concerns}. 
        Include practical advice, coping strategies, and recommend resources or contacts for further support.
        """
    prompt = PromptTemplate(input_variables=["current_mood", "recent_activities", "specific_concerns"], template=template)
    response = llm.prompt.format(current_mood=current_mood, recent_activities=recent_activities, specific_concerns=specific_concerns)
    print(response)
    return response

st.set_page_config(page_title="Mental Health Companion",
                   page_icon='🧠',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Mental Health Companion 🧠")

current_mood = st.text_input("How are you feeling today?")
recent_activities = st.text_area("Describe your recent activities (e.g., work, hobbies, social interactions):")
specific_concerns = st.text_area("Do you have any specific concerns or issues you'd like to address?")

submit = st.button("Get Advice")

if submit:
    st.write(getMentalHealthAdvice(current_mood, recent_activities, specific_concerns))
