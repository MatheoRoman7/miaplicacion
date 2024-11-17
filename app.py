import streamlit as st
import Modulo1 as m1
import pandas as pd
import plotly.express as px

st.title("Mi Aplicación")
st.sidebar.title("Parámetros")
st.sidebar.image("Logo.png",width=100)

modulo=st.sidebar.selectbox("Seleccione un módulo",["Módulo 1","Módulo 2","Módulo 3"])

if modulo=="Módulo 1":
    st.write("Usted está en el Módulo 1")
    GE=st.number_input("Ingrese el valor de la gravedad específica",min_value=0.1,max_value=1.0,value=0.8)
    API=m1.gradoAPI(GE)
    st.write("Si el grado API es: ",round(API,2))
elif modulo=="Módulo 2":
    col1,col2=st.columns(2)
    with col1:
        st.write("Usted está en el Módulo 2")
        df=pd.read_excel("resultados.xlsx")
        st.write(df)
    with col2:
        
        fig=px.line(df,x=df.index,y="API")
        st.write(fig)
else:
    st.write("Usted está en el Módulo 3")
    add_file=st.file_uploader("Sube tu archivo csv o excel",type=["csv","xlsx"])
    if add_file is not None:
        st.write("El archivo ha sido cargado")
        if add_file.name.endswith (".csv"):
            df=pd.read_csv(add_file)
        elif add_file.name.endswith (".xlsx"):
            df=pd.read_excel(add_file)
        st.write(df)
    else:
        st.write("Cargue el archivo csv o excel")