import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getRecipeSuggestions(ingredients, cuisine_type, dietary_restrictions):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256, 'temperature':0.5})
    template = """
        Suggest a recipe using the following ingredients: {ingredients}. 
        The recipe should be of {cuisine_type} cuisine and adhere to these dietary restrictions: {dietary_restrictions}. 
        Provide a detailed list of ingredients, step-by-step instructions, and any tips for preparation.
        """
    prompt = PromptTemplate(input_variables=["ingredients", "cuisine_type", "dietary_restrictions"], template=template)
    response = llm(prompt.format(ingredients=ingredients, cuisine_type=cuisine_type, dietary_restrictions=dietary_restrictions))
    print(response)
    return response

st.set_page_config(page_title="Recipe Suggestion Bot",
                   page_icon='🍽️',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Recipe Suggestion Bot 🍽️")

ingredients = st.text_area("Enter the ingredients you have:")
cuisine_type = st.selectbox("Select the cuisine type:", ["Italian", "Chinese", "Indian", "Mexican", "American"])
dietary_restrictions = st.text_input("Enter any dietary restrictions:")

submit = st.button("Get Recipe Suggestions")

if submit:
    st.write(getRecipeSuggestions(ingredients, cuisine_type, dietary_restrictions))
