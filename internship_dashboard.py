import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from datetime import datetime
import pytz


st.set_page_config(layout="wide")
st.title("Google Playstore Analytics Dashboard")

task_choice = st.sidebar.selectbox("Choose Analysis", [
    "Task 1","Task 2","Task 3","Task 4","Task 5","Task 6"
])

apps = pd.read_csv("playstore_data.csv")


apps['Installs']=pd.to_numeric(apps['Installs'].astype(str).str.replace(r'[+,]', '', regex=True), errors='coerce')
apps['Reviews']=pd.to_numeric(apps['Reviews'], errors='coerce')
apps['Rating']=pd.to_numeric(apps['Rating'], errors='coerce')
apps=apps[apps['Size'].str.contains('M', na=False)]
apps['Size_MB']=apps['Size'].str.replace('M','').astype(float)
apps['Last Updated']=pd.to_datetime(apps['Last Updated'], errors='coerce')

ist=pytz.timezone('Asia/Kolkata')
current_time=datetime.now(ist)

st.write("Current IST Time:", current_time.strftime("%H:%M"))


if task_choice == "Task 1":

    df1 = apps[(apps['Rating'] >= 4.0) &
               (apps['Size_MB'] >= 10) &
               (apps['Last Updated'].dt.month == 1)]

    stats = df1.groupby('Category').agg(
        Avg_Rating=('Rating','mean'),
        Total_Reviews=('Reviews','sum'),
        Installs=('Installs','sum')
    ).reset_index()

    top10 = stats.sort_values('Installs', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10,5))
    pos = np.arange(len(top10))

    ax.bar(pos-0.2, top10['Avg_Rating'], width=0.4, label="Avg Rating")
    ax.bar(pos+0.2, top10['Total_Reviews'], width=0.4, label="Reviews")
    ax.set_xticks(pos)
    ax.set_xticklabels(top10['Category'], rotation=45)
    ax.legend()

    if 15 <= current_time.hour < 17:
        st.pyplot(fig)

 
    #if 0 <= current_time.hour < 24:   
     # st.pyplot(fig)
   
    

if task_choice == "Task 2":

    df2 = apps.copy()
    df2['Price'] = df2['Price'].str.replace('$','').astype(float)
    df2['Revenue'] = df2['Installs'] * df2['Price']

    df2 = df2[(df2['Installs'] > 10000) &
              (df2['Revenue'] > 10000) &
              (df2['Size_MB'] > 15) &
              (df2['Content Rating'] == 'Everyone') &
              (df2['App'].str.len() <= 30)]

    top3 = df2.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(3).index
    df2 = df2[df2['Category'].isin(top3)]

    df2['Type'] = np.where(df2['Price']==0,'Free','Paid')

    summary = df2.groupby('Type').agg(
        Avg_Installs=('Installs','mean'),
        Revenue=('Revenue','sum')
    ).reset_index()

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.bar(summary['Type'], summary['Avg_Installs'])
    ax2.plot(summary['Type'], summary['Revenue'], marker='o', color='red')

    if 13 <= current_time.hour < 14:
        st.pyplot(fig)

    
    #if 0 <= current_time.hour < 24:   # TEST MODE
    # st.pyplot(fig)


if task_choice == "Task 3":

    import plotly.express as px

    df3 = apps[~apps['Category'].str.startswith(('A','C','G','S'), na=False)]

    top5 = df3.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(5).reset_index()

    countries = ["United States","India","Germany","Brazil","Australia"]
    top5['Country'] = countries[:len(top5)]

    fig = px.choropleth(top5, locations="Country",
                        locationmode="country names",
                        color="Installs",
                        hover_name="Category")

    if 18 <= current_time.hour < 20:
        st.plotly_chart(fig)

    

if task_choice == "Task 4":

    df4 = apps[(apps['Rating'] >= 4.2) &
               (~apps['App'].str.contains(r'\d')) &
               (apps['Category'].str.startswith(('T','P'))) &
               (apps['Reviews'] > 1000) &
               (apps['Size_MB'].between(20,80))]

    df4['Month'] = df4['Last Updated'].dt.to_period('M')
    pivot = df4.groupby(['Month','Category'])['Installs'].sum().unstack().fillna(0)

    pivot.plot.area(figsize=(10,5))
    if 16 <= current_time.hour < 18:
        st.pyplot(plt)


if task_choice == "Task 5":

    allowed = ['GAME','Beauty','Business','Comics','Communication','Dating','Entertainment','Social','Events']

    df5 = apps[(apps['Rating'] > 3.5) &
               (apps['Category'].isin(allowed)) &
               (apps['Reviews'] > 500) &
               (~apps['App'].str.contains('S')) &
               (apps['Installs'] > 50000)]

    fig, ax = plt.subplots()
    colors = ['pink' if c=='GAME' else 'blue' for c in df5['Category']]

    ax.scatter(df5['Size_MB'], df5['Rating'], s=df5['Installs']/10000, c=colors, alpha=0.6)

    if 17 <= current_time.hour < 19:
        st.pyplot(fig)


if task_choice == "Task 6":

    df6 = apps[(~apps['App'].str.startswith(('x','y','z'))) &
               (apps['Category'].str.startswith(('E','C','B'))) &
               (apps['Reviews'] > 500) &
               (~apps['App'].str.contains('S'))]

    df6['Month'] = df6['Last Updated'].dt.to_period('M')
    trend = df6.groupby(['Month','Category'])['Installs'].sum().unstack().fillna(0)

    trend.plot(figsize=(10,5))
    if 18 <= current_time.hour < 21:
        st.pyplot(plt)