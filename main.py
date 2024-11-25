import streamlit as st
import pandas as pd
from plots import Plots

st.set_page_config(page_title="Bike Sharing Analysis", layout="wide", page_icon='🚲')
st.title("Análise de Dados - Bike Sharing Demand")

@st.cache_data
def load_data(file_path=None, uploaded_file=None):
    try:
        if file_path:
            data = pd.read_csv(file_path)
        elif uploaded_file:
            data = pd.read_csv(uploaded_file)
        else:
            st.error("No data source provided.")
            return None

        data['datetime'] = pd.to_datetime(data['datetime'], errors='coerce')
        if data['datetime'].isnull().any():
            st.warning("Invalid datetime values detected and removed.")
            data = data.dropna(subset=['datetime'])

        data['date'] = data['datetime'].dt.date
        data['year'] = data['datetime'].dt.year
        data['month'] = data['datetime'].dt.month
        data['hour'] = data['datetime'].dt.hour
        data['weekday'] = data['datetime'].dt.weekday

        data["weekday"] = data["weekday"].map({
            0: "Segunda-feira",
            1: "Terça-feira",
            2: "Quarta-feira",
            3: "Quinta-feira",
            4: "Sexta-feira",
            5: "Sábado",
            6: "Domingo"
        })
        data["season"] = data["season"].map({
            1: "Primavera",
            2: "Verão",
            3: "Outono",
            4: "Inverno"
        })
        data["weather"] = data["weather"].map({
            1: "Claro, Poucas Nuvens, Parcialmente Nublado",
            2: "Névoa + Nublado, Névoa + Nuvens Quebradas",
            3: "Neve Leve, Chuva Leve + Trovoada + Nuvens Dispersas",
            4: "Chuva Forte + Granizo + Trovoada + Névoa"
        })

        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

data = load_data(file_path="train.csv")

uploaded_file = st.file_uploader("Carregue um CSV com o mesmo formato do dataset", type="csv")
if uploaded_file:
    custom_data = load_data(uploaded_file=uploaded_file)
    if custom_data is not None:
        data = custom_data
        st.success("Arquivo personalizado carregado com sucesso!")

if data is not None:
    st.header("1. Estatísticas Descritivas")
    st.dataframe(data.describe())

    st.header("2. Gráficos Dinâmicos")
    st.subheader("Registros Mensais")
    Plots.plot_monthly_records(data)

    st.divider()
    st.subheader("Gráficos de Pizza Comparativos")
    columns = st.columns(2)
    Plots.plot_workingday_comparison(data, columns[0])
    Plots.plot_casual_vs_registered(data, columns[1])

    st.subheader("Condições Climáticas")
    Plots.plot_weather_conditions(data)

    st.subheader("Análise por Hora do Dia")
    Plots.plot_hourly_analysis(data)

    st.subheader("Mapa de Calor das Correlações")
    Plots.plot_correlation_heatmap(data)
else:
    st.error("Nenhum dado disponível para exibição.")
