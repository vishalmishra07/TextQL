## my application
from dorenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3


import google.generativeai as geenrativeai

## Configure our API key
## for api creation go to makesuite.google.com/app/apikey
# genai.configure(api_key=os.getenv(" google api key"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to Load Google Gemini Model and Provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,question])
    return response.text ##Sql query
    

