#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("Formulario de datos")

# Solicita los datos del usuario
posicion = st.text_input("Ingrese su posición")
usuario = st.text_input("Ingrese su usuario")
contraseña = st.text_input("Ingrese su contraseña", type="password")

# Muestra los datos ingresados por el usuario
st.write("Posición:", posicion)
st.write("Usuario:", usuario)
st.write("Contraseña:", contraseña)

# Guarda los datos en una variable
datos = {"posicion": posicion, "usuario": usuario, "contraseña": contraseña}

