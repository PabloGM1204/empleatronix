import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título y descripción
st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Datos de ejemplo
data = pd.read_csv("csv/employees.csv")
df = pd.DataFrame(data)

# Mostrar tabla interactiva
st.dataframe(df)

# Configuración para gráfico
st.write("### Configura el gráfico")
color = st.color_picker("Elige un color para las barras", "#1f77b4")
mostrar_nombre = st.checkbox("Mostrar el nombre")
mostrar_sueldo = st.checkbox("Mostrar sueldo en la barra")

# Crear gráfico de barras
fig, ax = plt.subplots()
bars = ax.barh(df["full name"], df["salary"], color=color)

# Configurar del eje X
ax.set_xlim(0, 4500)
ax.tick_params(axis='x', labelrotation=90)

# Opciones interactivas
if mostrar_sueldo:
    ax.bar_label(bars, labels=[f" {salary} €" for salary in df["salary"]], label_type="edge")

# Mostrar gráfico
st.pyplot(fig)

st.write("© Pablo García Muñoz - Especialización en IA y Big Data")