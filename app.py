#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import subprocess

# Install openpyxl
subprocess.run(["pip", "install", "openpyxl"])

# Now you can import and use openpyxl
import openpyxl

st.title("Streamlit App with openpyxl")

# Your Streamlit app code here...
import pandas as pd

# Excel file URL on GitHub
excel_file_url = 'https://github.com/sharman1209/app/raw/main/data.xlsx'

# Read data from the URL
school_df = pd.read_excel(excel_file_url, sheet_name='List TM Interim Sites')

# Display the DataFrame
st.write(school_df)

# Export DataFrame to HTML for embedding in your web app
html_code = school_df.to_html()

# Function to toggle the search method and update the interface accordingly
def toggle_search_method():
    search_method = st.sidebar.selectbox("Search Method:", ['Select', 'By School Code', 'By School Name', 'By State'])
    
    if search_method == 'By School Code':
        school_code_input = st.text_input("Enter School Code:")
        manual_search_code_button = st.button("Search")
        if manual_search_code_button:
            search_school_info_by_code(school_code_input)
    
    elif search_method == 'By School Name':
        school_name_input = st.text_input("Enter School Name:")
        manual_search_name_button = st.button("Search")
        if manual_search_name_button:
            search_school_info_by_name(school_name_input)
    
    elif search_method == 'By State':
        selected_state = st.sidebar.selectbox("Select State:", ['Select'] + school_df['NEGERI'].unique().tolist())
        manual_search_state_button = st.button("Search")
        if manual_search_state_button and selected_state != 'Select':
            search_school_info_by_state(selected_state)

# Function to filter school codes based on the entered query (case-insensitive)
def filter_school_codes(query):
    query_lower = query.lower()
    return school_df[school_df['KOD SEKOLAH'].str.lower().str.contains(query_lower)]['KOD SEKOLAH'].tolist()

# Function to filter school names based on the entered query (case-insensitive)
def filter_school_names(query):
    query_lower = query.lower()
    return school_df[school_df['NAMA SEKOLAH'].str.lower().str.contains(query_lower)]['NAMA SEKOLAH'].tolist()

# Function to filter schools based on the selected state
def filter_schools_by_state(selected_state):
    return school_df[school_df['NEGERI'] == selected_state]

# Function to capitalize the input text
def capitalize_text(text):
    return text.upper()

# Function to handle code dropdown selection
def handle_code_dropdown_selection(selected_code):
    if selected_code:
        st.text(f"Selected School Code: {selected_code}")

# Function to handle name dropdown selection
def handle_name_dropdown_selection(selected_name):
    if selected_name:
        st.text(f"Selected School Name: {selected_name}")

# Function to handle state dropdown selection
def handle_state_dropdown_selection(selected_state):
    if selected_state:
        search_school_info_by_state(selected_state)

# Function to search for and display school information based on the selected school code
def search_school_info_by_code(selected_code):
    selected_school_info = school_df[school_df['KOD SEKOLAH'] == selected_code]
    display_search_results(selected_school_info)

# Function to search for and display school information based on the selected school name
def search_school_info_by_name(selected_name):
    selected_school_info = school_df[school_df['NAMA SEKOLAH'] == selected_name]
    display_search_results(selected_school_info)

# Function to search for and display school information based on the selected state
def search_school_info_by_state(selected_state):
    selected_schools_by_state = filter_schools_by_state(selected_state)
    display_search_results(selected_schools_by_state)

# Function to display search results as a list
def display_search_results(results_df):
    if not results_df.empty:
        st.text("Selected School Information:")
        for _, row in results_df.iterrows():
            for column_name, value in row.items():
                st.text(f"{column_name}: {value}")
            st.text("---")
    else:
        st.text("No matching school found")

# Create sidebar for search method selection
toggle_search_method()

# Create layout for the widgets


# In[ ]:




