import streamlit as st
import plotly.express as px

def generate_custom_bar_chart():
    # Datos personalizados para un gráfico de barras
    data = {
        'Categoría': ['A', 'B', 'C', 'D', 'E'],
        'Valor': [15, 8, 12, 6, 10]
    }

    # Crear gráfico de barras con Plotly Express
    fig = px.bar(data, x='Categoría', y='Valor', labels={'x': 'Categoría', 'y': 'Valor'}, title='Gráfico de Barras Personalizado')

    return fig

def main():
    # Configurar el sidebar vertical a la izquierda
    st.sidebar.title("Sidebar Vertical")

    # Configurar el sidebar horizontal en la parte superior
    st.markdown("# Sidebar Horizontal")

    # Configurar el grid de 3x4 en el resto de la página
    for i in range(3):
        row = st.container()

        with row:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.plotly_chart(generate_custom_bar_chart(), use_container_width=True)

            with col2:
                st.plotly_chart(generate_custom_bar_chart(), use_container_width=True)

            with col3:
                st.plotly_chart(generate_custom_bar_chart(), use_container_width=True)

            with col4:
                st.plotly_chart(generate_custom_bar_chart(), use_container_width=True)

if __name__ == "__main__":
    main()

