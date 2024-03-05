from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv ("API_KEY"))


## function to load Gemini Pro model and get repsonse

prompt= """You are a text summarizer tailored for our news channel, capable of condensing lengthy articles into 
concise 40-50 words summaries in PARAGRAPHS. 
You also extract and present key keywords in bullets. 
You also give a suitable title to the summary. 
You ONLY use BASIC English in the summary.
If the text is not a story or speech or script, ask to give another input as "Give a Paraghraph to summarize."
The input text will be appended here :  """

def get_gemini_response(input, prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+input)
    return response.text

##UI
st.title("ABP Network")
st.header("Text Summarizer powered by Gemini")

input_text= st.text_area("Input: ", height=200 , key="input")
submit=st.button("Summarize!")

##on clicking submit

if submit:
    response=get_gemini_response(input_text, prompt)
    st.write(response)

#pip install -r require........
#python -m streamlit run app.py