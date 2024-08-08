import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#st.title('Primeiro dashboard em streamlist')

# Com uma visão mensal
# Faturamento por unidade
# Tipo de produ to mais vendido, contribuição por filial
# Desempenho das formas de pagamento
# Como estão as avaliações das filias
# trabalho em

dados = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Convertendo a coluna "Date" para o tipo datetime
dados["Date"] = pd.to_datetime(dados["Date"])

# Ordenando o DataFrame pela coluna "Date"
dados = dados.sort_values("Date")

dados["Month"] = dados["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Mês", dados["Month"].unique())

dados_filtered = dados[dados["Month"] == month]

col1, col2 = st.columns(2)
col3, col4 , col5 = st.columns(3)

fig_date = px.bar(dados_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(dados_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = dados_filtered.groupby("City")[["Total"]].sum().reset_index
fig_city = px.bar(dados_filtered, x="City", y="Total", 
                  title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(dados_filtered, values="Total", names="Payment", 
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind,use_container_width=True)


city_total = dados_filtered.groupby("City")[["Rating"]].mean().reset_index
fig_rating = px.bar(dados_filtered, y="Rating", x="City", 
                  title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)