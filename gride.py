import streamlit as st
import plotly.express as px
import numpy as np

def generate_random_bar_chart():
    # Generar datos aleatorios para un gráfico de barras
    categories = [f"Categoria {i}" for i in range(1, 11)]
    values = np.random.randint(1, 20, size=10)

    # Crear gráfico de barras con Plotly Express
    fig = px.bar(x=categories, y=values, labels={'x': 'Categoría', 'y': 'Valor'}, title='Gráfico de Barras Aleatorio')

    return fig

def main():
    # Configurar el sidebar vertical a la izquierda
    st.sidebar.title("Sidebar Vertical")

    # Configurar el sidebar horizontal en la parte superior
    st.markdown("# Sidebar Horizontal")

    # Configurar el grid de 3x4 en el resto de la página
    for i in range(3):
        row = st.beta_container()

        with row:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.plotly_chart(generate_random_bar_chart(), use_container_width=True)

            with col2:
                st.plotly_chart(generate_random_bar_chart(), use_container_width=True)

            with col3:
                st.plotly_chart(generate_random_bar_chart(), use_container_width=True)

            with col4:
                st.plotly_chart(generate_random_bar_chart(), use_container_width=True)

if __name__ == "__main__":
    main()




