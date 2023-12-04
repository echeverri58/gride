import streamlit as st
import plotly.express as px
import numpy as np

def generate_random_plot():
    # Generar datos aleatorios
    x = np.arange(10)
    y = np.random.randint(1, 10, size=10)

    # Crear figura con Plotly Express
    fig = px.line(x=x, y=y, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Gráfico Aleatorio')

    return fig

def main():
    # Configurar el sidebar vertical a la izquierda
    st.sidebar.title("Sidebar Vertical")

    # Configurar el sidebar horizontal en la parte superior
    st.markdown("# Sidebar Horizontal")

    # Configurar el grid de 3x4 en el resto de la página
    for i in range(4):
        row_col1, row_col2, row_col3 = st.columns(3)
        
        with row_col1:
            st.plotly_chart(generate_random_plot(), use_container_width=True)

        with row_col2:
            st.plotly_chart(generate_random_plot(), use_container_width=True)

        with row_col3:
            st.plotly_chart(generate_random_plot(), use_container_width=True)

if __name__ == "__main__":
    main()



