# Created the  Virtual Env.
# Install the lib : Streamlit, Google-generativeai, Langchain
# pip install streamlit langchain goggle-generativeai 


import streamlit as st 
import langchain 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the page -- Title of the page 
st.title("Movie Recommender System Using Google Gemini 🤩 📷 🎮 📸 🥤 🍿 📹 🤳 📼 🎦")
# st.subheader("Please enter a Movie Name")
user_input = st.text_input("Enter a movie title, genre or keywords (e.g. sci-fi)")
   
# LLM Model 

demo_template = f'''Based onn the input here are some movie recommendations\
    for {user_input}:\n'''
template = PromptTemplate(input_variable = ['user input'], template= demo_template)

# Initalise the Gemini Pro Model 
llms = ChatGoogleGenerativeAI(model='gemini-pro',api_key="AIzaSyAKRoh9V5jcewM92oD9SFiPXs4NVMKoitE")

# Generate the recommendation when the user prompt input 

if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llms.predict(text=prompt)
    st.write(F"Recommendations for you:\n {recommendations}")
else:
    st.write("Enter the Movie Name")    
    