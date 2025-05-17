import streamlit as st
st.set_page_config(layout='wide')
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_excel("Maint_project.xlsx",sheet_name="Report")
df['user_id'] = df['user_id'].astype(str)
df['SR_id'] = df['SR_id'].astype(str)

tab1 , tab2 = st.tabs(["Report" , "Analysis"])

with tab1 :
    df

with tab2:
    custom_colors = {
    "Cairo & Giza": "#EF553B",
    "Delta West": "#FFA15A"}
    fig_scatter = px.scatter(data_frame=df,x="Count_of_pos",y="Total_Revenue",color_discrete_sequence=px.colors.qualitative.Set3,
    range_y=[0, 50000],color='Region',color_discrete_map=custom_colors)
    st.plotly_chart(fig_scatter)

    Region = st.selectbox('Select Region',options=df['Region'].unique())
    st.write(Region)
    s_df = df[df['Region']==Region]
    custom_colors = {
    "Inactive": "#EF553B",
    "One Line": "#FFA15A",
    "Two Lines": "#B6E880",
    "Three Lines": "#00CC96"}

    fig_pie = px.pie(
    data_frame=s_df,
    names="Bunsiness_lines",
    facet_col="AM",
    color="Bunsiness_lines",
    color_discrete_map=custom_colors)
    fig_pie.update_traces(textinfo='label+percent+value')

    st.plotly_chart(fig_pie)

    custom_colors2 = {
    "unUse": "#EF553B",
    "Binding": "#00CC96"}

    fig_pie2 = px.pie(
    data_frame=s_df,
    names="status",
    facet_col="AM",
    color="status",
    color_discrete_map=custom_colors2)
    fig_pie2.update_traces(textinfo='label+percent+value')

    st.plotly_chart(fig_pie2)

    custom_colors3 = {
    "Inactive": "#FF0000",
    "Low Ach": "#FFFF00",
     "Below Avg" : "#FFA500",
      "Above Avg":"#FFFFFF",
        "Near ach" : "#00FFFF",
        "Achieved":"#008000"}

    fig_pie3 = px.pie(
    data_frame=s_df,
    names="Achieving tiers",
    facet_col="AM",
    color="Achieving tiers",
    color_discrete_map=custom_colors3)
    fig_pie3.update_traces(textinfo='percent+value')

    st.plotly_chart(fig_pie3)

    df_melted = df.melt(
    id_vars="Region", 
    value_vars=["Excpected pos", "User_Exp"],
var_name="Client_Soruce",
    value_name="Sales")

    fig_bar = px.histogram(
    df_melted,
    x="Region",
    y="Sales",
    color="Client_Soruce",
    histfunc="sum",
    barmode="group"
)



    st.plotly_chart(fig_bar)
