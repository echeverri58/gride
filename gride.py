import streamlit as st

# Configurar el sidebar vertical a la izquierda
st.sidebar.title("Sidebar Vertical")

# Configurar el sidebar horizontal en la parte superior
st.markdown("# Sidebar Horizontal")

# Configurar el grid de 3x4 en el resto de la página
# Puedes personalizar esto según tus necesidades
grid_col1, grid_col2, grid_col3 = st.beta_columns(3)

# Columna 1 del grid
with grid_col1:
    st.write("Columna 1")

# Columna 2 del grid
with grid_col2:
    st.write("Columna 2")

# Columna 3 del grid
with grid_col3:
    st.write("Columna 3")

# Segunda fila del grid
grid_col4, grid_col5, grid_col6 = st.beta_columns(3)

# Columna 4 del grid
with grid_col4:
    st.write("Columna 4")

# Columna 5 del grid
with grid_col5:
    st.write("Columna 5")

# Columna 6 del grid
with grid_col6:
    st.write("Columna 6")

# Tercera fila del grid
grid_col7, grid_col8, grid_col9 = st.beta_columns(3)

# Columna 7 del grid
with grid_col7:
    st.write("Columna 7")

# Columna 8 del grid
with grid_col8:
    st.write("Columna 8")

# Columna 9 del grid
with grid_col9:
    st.write("Columna 9")

# Cuarta fila del grid
grid_col10, grid_col11, grid_col12 = st.beta_columns(3)

# Columna 10 del grid
with grid_col10:
    st.write("Columna 10")

# Columna 11 del grid
with grid_col11:
    st.write("Columna 11")

# Columna 12 del grid
with grid_col12:
    st.write("Columna 12")
