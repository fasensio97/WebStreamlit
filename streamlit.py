#!/usr/bin/env python
# coding: utf-8

# In[1]:


st.markdown("<h1 style='text-align: center;'>Formulario</h1>", unsafe_allow_html=True)

with st.form("Datos de Usuario"):
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")
    puesto = st.selectbox("Puesto de trabajo", ["Gerente", "Analista", "Desarrollador"])
    cantidad_hojas = st.slider("Cantidad de hojas", min_value=1, max_value=10, value=5)

    submitted = st.form_submit_button("Enviar")

if submitted:
    # Guardar los datos ingresados en variables
    datos_usuario = {
        "email": email,
        "password": password,
        "puesto": puesto,
        "cantidad_hojas": cantidad_hojas
    }
    st.write("Los datos ingresados son:", datos_usuario)

