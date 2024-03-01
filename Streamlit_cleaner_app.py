#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import re
from openpyxl import load_workbook


# In[ ]:


def clean_publication_name(text):
    
    # If the text starts with 'www.', return the text as it is
    if text.startswith('www.'):
        return text
    
    text = re.sub(r"\..*$", "", text)
    text = re.sub(r"[^\w\s-]", "", text).lower()
    text = re.sub(r"\s", "", text)
    return text


# In[ ]:


# Title and description for your app
st.title("Publication Cleaner Tool")
st.write("This tool cleans publication names from Excel files.")

# File upload for 'pub_list.xlsx'
uploaded_file1 = st.file_uploader("Upload 'pub_list.xlsx':", type="xlsx")

# File upload for 'pub_list_client.xlsx'
uploaded_file2 = st.file_uploader("Upload 'pub_list_client.xlsx':", type="xlsx")

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Read the data from uploaded files
    data1 = pd.read_excel(uploaded_file1)
    data2 = pd.read_excel(uploaded_file2)

    # Clean the data
    publications1 = data1['Publications'].tolist()
    cleaned_publications1 = [clean_publication_name(pub) for pub in publications1]
    cleaned_data1 = pd.DataFrame({'Cleaned Publication Name': cleaned_publications1})

    publications2 = data2['Publications'].tolist()
    cleaned_publications2 = [clean_publication_name(pub) for pub in publications2]
    cleaned_data2 = pd.DataFrame({'Cleaned Publication Name': cleaned_publications2})

    # Download cleaned data as Excel files (optional)
    st.download_button(
        label="Download Cleaned 'pub_list.xlsx'",
        data=cleaned_data1.to_excel(index=False),
        file_name="cleaned_pub_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.download_button(
        label="Download Cleaned 'pub_list_client.xlsx'",
        data=cleaned_data2.to_excel(index=False),
        file_name="cleaned_pub_list_client.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info("Please upload both files.")

