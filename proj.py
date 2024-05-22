import streamlit as st

def app():
    st.title("Time Series Analysis using Prophet with Hyperparameter Tuning")

    about = '''This project involves the forecasting of GOLD (XAUUSD) price using Time-Series Analysis with a dataset obtained from Yahoo Finance.
    The dataset spans from January 1, 2010, to the recent date, April 31, 2024. 
    When it comes to the investment oppotunity, GOLD is a major player in terms of Market Dominance, Financial Performance.
    '''

    justified_text = f"<div style='text-align: justify;'>{about}</div>"

    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    st.subheader("Intro to Time-Series Analysis")

    timeseries = '''
    Time series analysis is a statistical method that examines and interprets sequential data points collected over time, allowing for the identification of patterns, trends, and dependencies within the temporal structure.
    '''

    justified_text1 = f"<div style='text-align: justify;'>{timeseries}</div>"

    st.markdown(justified_text1, unsafe_allow_html=True)

    timeseries1 = '''
    It is commonly used for forecasting future values, understanding historical behavior, and making informed decisions based on the temporal evolution of the data. Time series analysis is widely used in various fields, including finance, economics, signal processing, environmental science, and many others. In this project we will use the prophet model developed by facebook research.
    '''

    justified_text2 = f"<div style='text-align: justify;'>{timeseries1}</div>"

    st.markdown(justified_text2, unsafe_allow_html=True)
    st.markdown("#")

    st.subheader("Prophet model")

    proph = '''
    Prophet is a method for forecasting time-series from incorporate algorithms whose linear patterns correlate to seasonal, daily, weekly and holiday events. It is a Python and R-based fully accessible and openly availabe for forecasting by generating predictions automatically.
    '''

    justified_text3 = f"<div style='text-align: justify;'>{proph}</div>"

    st.markdown(justified_text3, unsafe_allow_html=True)
    st.markdown("#")

    st.subheader("Motivation")

    moti = '''
    Predicting stock price is one of significant interest to investors, traders, and financial analysts in terms of making investment decision and risk management.
    '''

    justified_text4 = f"<div style='text-align: justify;'>{moti}</div>"

    st.markdown(justified_text4, unsafe_allow_html=True)
    st.markdown("#")

    st.subheader("Citation")

    cite = '''
    A. Maheshwari, A. Malhotra, S. Tuteja, M. Ranka and M. S. A. Basha, "Prediction of Stock Prices using Prophet Model with Hyperparameters tuning," 2022 IEEE North Karnataka Subsection Flagship International Conference (NKCon), Vijaypur, India, 2022, pp. 1-5, doi: 10.1109/NKCon56289.2022.10126796.
    '''

    justified_text5 = f"<div style='text-align: justify;'>{cite}</div>"

    st.markdown(justified_text5, unsafe_allow_html=True)



    
