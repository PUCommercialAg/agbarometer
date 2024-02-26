import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px # for visualization 
import plotly.offline as py 
import plotly.graph_objs as go 
from plotly.figure_factory import create_table # for creating nice table

st.title('Ag Economy Barometer')
chart = st.container()
changes = st.container()
footnote = st.container()

st.markdown(
    """
    <style>
    .main{
    background-color: #cfb991
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Start of Chart (Line Chart) Area:
with chart:
    st.header('Charts')
    
    df = pd.read_csv('/Users/smithse/Desktop/Streamlit_AgBarometer/data/Barometer_Indices.csv')
    fig = px.line(df, x="Month", y="Barometer_Index", title='Ag Economy Barometer')

    fig.show()

    tab1, tab2 = st.tabs(["Ag Economy Barometer (main)", "Theme2"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)

    
##Start of Month-to-Month/Year-to-Year Changes (Bar Chart Area):
with changes:
    st.subheader('Changes:')


#Footnotes
with footnote:
    st.text('Source: Purdue University Center for Commercial Agriculture, Producer Survey')
