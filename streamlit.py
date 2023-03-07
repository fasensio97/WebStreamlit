#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.markdown("<h1 style='text-align: center;'>Web Scrapper</h1",unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    st.form_submit_button("Search")

