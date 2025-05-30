import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo entrenado
modelo = joblib.load("modelo_ligero_nuevo.pkl")

# Título de la app
st.title("Predicción de Enfermedad Cardíaca")

st.write("Introduce la información del paciente para predecir la probabilidad de enfermedad cardíaca.")

# Crear los inputs del usuario
gender = st.selectbox("Género", ["Femenino", "Masculino"])
age_category = st.selectbox("Rango de edad", [
    "18-24", "25-29", "30-34", "35-39", "40-44", "45-49",
    "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 o más"
])
smoking = st.selectbox("¿Fuma?", ["Sí", "No"])
bmi = st.slider("IMC (Índice de Masa Corporal)", 10.0, 50.0, 25.0)
physical_activity = st.selectbox("Actividad física", ["Sí", "No"])
sleep_time = st.slider("Horas de sueño diarias", 0, 24, 7)

# Procesar entradas
gender_val = 1 if gender == "Masculino" else 0
smoking_val = 1 if smoking == "Sí" else 0
activity_val = 1 if physical_activity == "Sí" else 0

# Mapear edad a número
edad_map = {
    "18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-44": 4,
    "45-49": 5, "50-54": 6, "55-59": 7, "60-64": 8, "65-69": 9,
    "70-74": 10, "75-79": 11, "80 o más": 12
}
age_val = edad_map[age_category]

# Construir el array de entrada en el mismo orden del modelo
input_data = np.array([[gender_val, age_val, smoking_val, bmi, activity_val, sleep_time]])

# Botón para predecir
if st.button("Predecir"):
    prediccion = modelo.predict(input_data)[0]
    if prediccion == 1:
        st.error("⚠️ Riesgo alto de enfermedad cardíaca.")
    else:
        st.success("✅ Bajo riesgo de enfermedad cardíaca.")
