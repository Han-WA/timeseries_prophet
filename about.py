import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from prophet import Prophet
from datetime import datetime

def app():
    st.title("Data Overview")

    mydata = pd.read_csv(r"D:\dashboard\bkholding.csv")
    df = pd.read_csv(r"D:\dashboard\bookingholding.csv")

    # Printing the dataswet shape
    st.subheader("Data Collection")
    collec = '''We have looked and tested thoroughly several datasets types across internet in order to build a comprehensive foundation for model. When it comes to Yahoo Finance, it provide the information properly oragnised and many of the attributes are widely used by share price enthusiast and experts.'''
    justified_text = f"<div style='text-align: justify;'>{collec}</div>"

    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("#")

    st.subheader('Dataset Obtained from Yahoo Finance')
    st.write(mydata)
    st.markdown("##")
    st.markdown("##")

    st.subheader("Data Labelling")
    labe = '''In this project, we will perform a time-series analysis on Close price data. Therefore, we will drop all the attributes except Date as ds and Close as y.'''
    justified_text1 = f"<div style='text-align: justify;'>{labe}</div>"

    st.markdown(justified_text1, unsafe_allow_html=True)
    st.markdown("#")

    st.write(df)


    st.subheader("Relationship between Close Price with Time")
    line1 = px.line(mydata, x= mydata['Date'] , y=mydata['Close'])
    line1.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(line1,use_container_width=True)
    st.markdown("##")
    st.markdown("##")

    st.header("Area Chart")
    st.caption("Compare the open, high, low, and close prices for a specific date or time period.")
    fig_area = px.area(mydata, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Cumulative Prices', labels={'value': 'Cumulative Price'})
    st.plotly_chart(fig_area)
    st.markdown("##")
    st.markdown("##")

    st.header("Scatter Plot")
    st.caption("Show the relationship between two variables, such as open and close prices.")
    fig_scatter = px.scatter(mydata, x='Open', y='Close', title='Scatter Plot of Open vs. Close Prices')
    st.plotly_chart(fig_scatter)
    st.markdown("##")
    st.markdown("##")

    st.header("Histogram")
    st.caption("Display the distribution of a single variable, like the daily price changes.")
    mydata['Price Change'] = mydata['Close'] - mydata['Open']
    fig_hist = px.histogram(mydata, x='Price Change', title='Distribution of Daily Price Changes')
    st.plotly_chart(fig_hist)
    st.markdown("##")
    st.markdown("##")

    st.header("Box Plot")
    st.caption("Visualize the distribution of the open, high, low, and close prices.")
    fig_box = px.box(mydata, y=['Open', 'High', 'Low', 'Close'], title='Box Plot of Open, High, Low and Close Prices')
    st.plotly_chart(fig_box)
    st.markdown("##")
    st.markdown("##")



