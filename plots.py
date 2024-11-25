import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st

class Plots:
    @staticmethod
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

    @staticmethod
    def plot_workingday_comparison(data, col):
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def plot_hourly_analysis(data):
        col_temp = {
            'weekday': 'Dia da Semana',
            'workingday': 'Dia Útil',
            'holiday': 'Feriado',
            'season': 'Estação',
            'weather': 'Condição Climática'
        }
        tabs = st.tabs(list(col_temp.values()))
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

    @staticmethod
    def plot_correlation_heatmap(data):
        numeric_data = data.select_dtypes(include=[np.number])
        corr_matrix = numeric_data.corr()
        fig = px.imshow(
            corr_matrix,
            title="Mapa de Calor das Correlações",
            color_continuous_scale="sunset",
            labels={"color": "Correlação"}
        )
        st.plotly_chart(fig, use_container_width=True)
