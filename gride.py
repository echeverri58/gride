import streamlit as st
import plotly.express as px
import numpy as np

def generate_random_bar_chart():
    categories = [f"Categoria {i}" for i in range(1, 11)]
    values = np.random.randint(1, 20, size=10)
    fig = px.bar(x=categories, y=values, labels={'x': 'Categoría', 'y': 'Valor'}, title='Gráfico de Barras Aleatorio')
    return fig

def main():
    # Configurar el sidebar vertical a la izquierda
    st.sidebar.title("Sidebar Vertical")

    # Configurar el sidebar horizontal en la parte superior
    st.markdown("# Sidebar Horizontal")

    # Lista de gráficos disponibles
    available_charts = {
        'Gráfico 1': generate_random_bar_chart(),
        'Gráfico 2': generate_random_bar_chart(),
        'Gráfico 3': generate_random_bar_chart(),
        # Agrega más gráficos según sea necesario
    }

    # Selección de gráficos desde el sidebar
    selected_charts = st.sidebar.multiselect('Seleccione los gráficos a comparar', list(available_charts.keys()))

    # Configurar el grid de 2x1 para los gráficos seleccionados
    row = st.container()
    with row:
        col1, col2 = st.columns(2)

        # Mostrar el primer gráfico seleccionado
        if selected_charts:
            with col1:
                st.plotly_chart(available_charts[selected_charts[0]], use_container_width=True)

        # Mostrar el segundo gráfico seleccionado
        if len(selected_charts) > 1:
            with col2:
                st.plotly_chart(available_charts[selected_charts[1]], use_container_width=True)

if __name__ == "__main__":
    main()





