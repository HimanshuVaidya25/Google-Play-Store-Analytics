import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 
from datetime import datetime
import pytz

st.title("Google Play Store Analytics Dashboard")

df=pd.read_csv("Play Store Data.csv")

df['Installs']=df['Installs'].astype(str)
df['Installs']=df['Installs'].str.replace('[+,]','',regex=True)
df['Installs']=pd.to_numeric(df['Installs'],errors='coerce')
df['Reviews']=pd.to_numeric(df['Reviews'],errors='coerce')
df['Rating']=pd.to_numeric(df['Rating'], errors='coerce')

df=df[df['Size'].str.contains('M',na=False)]
df['Size_MB']=df['Size'].str.replace('M','').astype(float)
df['Last Updated']=pd.to_datetime(df['Last Updated'],errors='coerce')

filtered_df=df[ 
               (df['Rating']>=4.0)&
               (df['Size_MB']>=10)&
               (df['Last Updated'].dt.month==1)]

grp=filtered_df.groupby('Category').agg({
    'Rating':'mean',
    'Reviews':'sum',
    'Installs':'sum'
}).reset_index()

top10=grp.sort_values(by='Installs', ascending=False).head(10)

labels=top10['Category']
x=np.arange(len(labels))

fig,ax=plt.subplots(figsize=(12,6))
ax.bar(x-0.2,top10['Rating'],width=0.4,label='Average Rating')
ax.bar(x+0.2,top10['Reviews'],width=0.4,label='Total Reviews')

ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.set_title("Top 10 Categories: Avg rating vs Reviews")
ax.legend()

ist=pytz.timezone('Asia/Kolkata')
now=datetime.now(ist)

if 15<=now.hour<17:
    st.pyplot(fig)
else:
    st.warning("This chart is visible only between 3Pm and 5PM IST")
