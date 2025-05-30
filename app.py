import streamlit as st
import joblib
import numpy as np

# Cargar modelo
modelo = joblib.load("modelo_ligero_nuevo.pkl")

# Título
st.title("Predicción de Enfermedad Cardíaca")

# Formulario de entrada
st.subheader("Ingrese los datos del paciente:")

campos = {
    'HighBP': st.selectbox('¿Presión arterial alta?', [0, 1]),
    'HighChol': st.selectbox('¿Colesterol alto?', [0, 1]),
    'CholCheck': st.selectbox('¿Chequeo de colesterol?', [0, 1]),
    'BMI': st.number_input('Índice de masa corporal (BMI)', min_value=10.0, max_value=60.0, value=25.0),
    'Smoker': st.selectbox('¿Fumador?', [0, 1]),
    'Stroke': st.selectbox('¿Ha sufrido un derrame?', [0, 1]),
    'Diabetes': st.selectbox('¿Tiene diabetes?', [0, 1]),
    'PhysActivity': st.selectbox('¿Realiza actividad física?', [0, 1]),
    'Fruits': st.selectbox('¿Consume frutas regularmente?', [0, 1]),
    'Veggies': st.selectbox('¿Consume verduras regularmente?', [0, 1]),
    'HvyAlcoholConsump': st.selectbox('¿Consumo excesivo de alcohol?', [0, 1]),
    'AnyHealthcare': st.selectbox('¿Tiene cobertura médica?', [0, 1]),
    'NoDocbcCost': st.selectbox('¿Ha evitado al médico por costo?', [0, 1]),
    'GenHlth': st.slider('Salud general (1=Muy buena, 5=Muy mala)', 1, 5, 3),
    'MentHlth': st.slider('Días de mala salud mental en el último mes', 0, 30, 0),
    'PhysHlth': st.slider('Días de mala salud física en el último mes', 0, 30, 0),
    'DiffWalk': st.selectbox('¿Tiene dificultad para caminar?', [0, 1]),
    'Sex': st.selectbox('Sexo (0=Femenino, 1=Masculino)', [0, 1]),
    'Age': st.slider('Grupo de edad (1=18-24, ..., 13=80+)', 1, 13, 5),
    'Education': st.slider('Nivel educativo (1=menos a 9 grado, 6=graduado universitario)', 1, 6, 3),
    'Income': st.slider('Nivel de ingreso (1=menos de $10k, 8=mayor a $75k)', 1, 8, 4)
}

# Botón de predicción
if st.button("Predecir"):
    valores = np.array([list(campos.values())])
    resultado = modelo.predict(valores)[0]
    if resultado == 1:
        st.error("⚠️ Riesgo de enfermedad cardíaca detectado.")
    else:
        st.success("✅ Bajo riesgo de enfermedad cardíaca.")
