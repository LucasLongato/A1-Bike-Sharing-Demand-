import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuração inicial
st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")
st.title("Análise de Dados - Bike Sharing Demand")


@st.cache_data
def load_data():
    # Load and preprocess data
    train = pd.read_csv("train.csv")
    train['datetime'] = pd.to_datetime(train['datetime'])
    train['date'] = train['datetime'].dt.date
    train['year'] = train['datetime'].dt.year
    train['month'] = train['datetime'].dt.month
    train['hour'] = train['datetime'].dt.hour
    train['weekday'] = train['datetime'].dt.weekday

    # Apply mappings for readability
    train["weekday"] = train["weekday"].map({
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    })

    train["season"] = train["season"].map({
        1: "Primavera",
        2: "Verão",
        3: "Outono",
        4: "Inverno"
    })

    train["weather"] = train["weather"].map({
        1: "Claro, Poucas Nuvens, Parcialmente Nublado",
        2: "Névoa + Nublado, Névoa + Nuvens Quebradas",
        3: "Neve Leve, Chuva Leve + Trovoada + Nuvens Dispersas",
        4: "Chuva Forte + Granizo + Trovoada + Névoa"
    })

    return train


def plot_monthly_records(data):
    grouped = data.groupby(data["datetime"].dt.to_period("M")).agg({"temp": "mean", "count": "sum"}).reset_index()
    grouped["month"] = grouped["datetime"].astype(str)

    fig = px.bar(
        grouped,
        x="month",
        y="count",
        title="Registros Mensais com Linha de Crescimento",
        labels={"month": "Mês", "count": "Quantidade de Registros"},
        color_discrete_sequence=["skyblue"]
    )
    fig.add_scatter(
        x=grouped["month"],
        y=grouped["count"],
        mode='lines+markers',
        line=dict(color="red"),
        name="Linha de Crescimento"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_workingday_comparison(data, col: st):
    col.subheader("Dias úteis X Feriados")

    workingday_summary = data.groupby("workingday")["count"].sum().reset_index()
    workingday_summary["workingday"] = workingday_summary["workingday"].map({0: "Feriados", 1: "Dias Úteis"})

    fig = px.pie(
        workingday_summary,
        values="count",
        names="workingday",
        title="Dias Úteis vs Feriados",
        color_discrete_sequence=["lightcoral", "skyblue"]
    )
    col.plotly_chart(fig, use_container_width=True)


def plot_casual_vs_registered(data, col):
    col.subheader("Usuários Casuais vs Registrados")

    casual_registered_summary = data[["casual", "registered"]].sum()

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=["Casual", "Registrados"],
        values=casual_registered_summary,
        marker=dict(colors=["lightcoral", "skyblue"]),
        title="Usuários Casuais vs Registrados"
    ))
    col.plotly_chart(fig, use_container_width=True)


def plot_weather_conditions(data):
    weather_summary = data.groupby("weather")["count"].sum().reset_index()

    fig = px.bar(
        weather_summary,
        x="weather",
        y="count",
        title="Registros por Condições Climáticas",
        labels={"weather": "Condições Climáticas", "count": "Quantidade de Registros"},
        color_discrete_sequence=["skyblue"]
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_hourly_analysis(data):
    # Translation of tab names to Portuguese
    col_temp = {
        'weekday': 'Dia da Semana',
        'workingday': 'Dia Útil',
        'holiday': 'Feriado',
        'season': 'Estação',
        'weather': 'Condição Climática'
    }
    
    # Create tabs with translated names
    tabs = st.tabs(list(col_temp.values()))

    # Geração dinâmica dos gráficos com base na aba selecionada
    for tab, (col, display_name) in zip(tabs, col_temp.items()):
        with tab:
            fig = px.line(
                data,
                x="hour",
                y="count",
                color=col,
                title=f"Contagem horária por {display_name}",
                labels={"hour": "Hora do Dia", "count": "Quantidade"}
            )
            st.plotly_chart(fig, use_container_width=True)

def plot_correlation_heatmap(data):
    # Remove non-numeric columns for correlation
    numeric_data = data.select_dtypes(include=[np.number])

    corr_matrix = numeric_data.corr()

    fig = px.imshow(
        corr_matrix,
        title="Mapa de Calor das Correlações",
        color_continuous_scale="sunset",
        labels={"color": "Correlação"}
    )
    st.plotly_chart(fig, use_container_width=True)


# Load data
data = load_data()

# Estatísticas Descritivas
st.header("1. Estatísticas Descritivas")
st.dataframe(data.describe())

# Gráficos Dinâmicos
st.header("2. Gráficos Dinâmicos")
st.subheader("Registros Mensais")
plot_monthly_records(data)
st.divider()
st.subheader("Gráficos de Pizza Comparativos")
columns = st.columns(2)

# Column 1: Dias Úteis vs Feriados
plot_workingday_comparison(data, columns[0])

# Column 2: Usuários Casuais vs Registrados
plot_casual_vs_registered(data, columns[1])

st.subheader("Condições Climáticas")
plot_weather_conditions(data)

st.subheader("Análise por Hora do Dia")
plot_hourly_analysis(data)

st.subheader("Mapa de Calor das Correlações")
plot_correlation_heatmap(data)
