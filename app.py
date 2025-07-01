from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyAW3k6M8TOu_xG8It_Aks6Xo-yQxta5mzs")

# model = genai.GenerativeModel("gemini-pro")
# response = model.generate_content("Write a SQL query to get all students with marks > 90.")
# print(response.text)

# Define Prompt (as a plain string, not a list)
prompt = """
You are an expert in converting English questions to SQL queries.
The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION, MARKS.

Example 1: 
Q: How many students are there?
A: SELECT COUNT(*) FROM STUDENT;

Example 2: 
Q: Show all students in Data Science class.
A: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

Note:
Only return the SQL query.
Do not include triple backticks.
No explanation, just the SQL code.
"""

# Function to get SQL query from Gemini
def get_gemini_response(question):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content(prompt + "\n" + question)
    return response.text.strip()

# Function to execute SQL query
def read_sql_query(sql, db_path):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        return [("Error:", str(e))]

# Streamlit UI
st.set_page_config(page_title="SQL Query Generator")
st.title("Gemini App: Convert Questions to SQL")

question = st.text_input("Input your question about the student database:")

if st.button("Ask the question"):
    response = get_gemini_response(question)
    st.subheader("Generated SQL Query:")
    st.code(response)

    data = read_sql_query(response, "student.db")
    st.subheader("Query Results:")
    for row in data:
        st.write(row)