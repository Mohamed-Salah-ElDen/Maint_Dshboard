import streamlit as st
st.set_page_config(layout='wide')
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import openpyxl as xl

df = pd.read_excel("Maint_project.xlsx",sheet_name="Report")

tab1, tab2 = st.tabs(["Report" , "Analysis"])

with tab1 :
    df

with tab2:
    custom_colors = {
    "Cairo & Giza": "#ff1110",
    "Delta West": "#FFA15A",
    "Delta East": "#106bff",
    "Canal": "#ffeb10",
    "Upper Egypt": "#ff107c"}
    fig_scatter = px.scatter(data_frame=df,x="Count_of_pos",y="Total_user",color_discrete_sequence=custom_colors,
    range_y=[0, 50000],color='Region',color_discrete_map=custom_colors)
    st.plotly_chart(fig_scatter)

    Region = st.selectbox('Select Region',options=df['Region'].unique())
    st.write(Region)
    s_df = df[df['Region']==Region]
    custom_colors = {
    "Inactive": "#ff0000",
    "One Line": "#e07a15",
    "Two Lines": "#158de0",
    "Three Lines": "#15e04f"}

    fig_pie = px.pie(
    data_frame=s_df,
    names="Business_lines",
    facet_col="AM",
    color="Business_lines",
    color_discrete_map=custom_colors)
    fig_pie.update_traces(textinfo='label+percent+value')

    st.plotly_chart(fig_pie)

    custom_colors2 = {
    "unUse": "#ff0000",
    "Binding": "#15e04f"}

    fig_pie2 = px.pie(
    data_frame=s_df,
    names="status",
    facet_col="AM",
    color="status",
    color_discrete_map=custom_colors2)
    fig_pie2.update_traces(textinfo='label+percent+value')

    st.plotly_chart(fig_pie2)

    custom_colors3 = {
    "Inactive": "#ff0000",
    "Low ach": "#b33d05",
     "Above avg":"#b33d05",
        "Achieved":"#15e04f"}

    fig_pie3 = px.pie(
    data_frame=s_df,
    names="Achievment tiers",
    facet_col="AM",
    color="Achievment tiers",
    color_discrete_map=custom_colors3)
    fig_pie3.update_traces(textinfo='percent+value')

    st.plotly_chart(fig_pie3)

    df_melted = df.melt(
    id_vars="Region", 
    value_vars=["Ex_pos", "Ex_user"],
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
