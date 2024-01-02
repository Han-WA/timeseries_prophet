import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px
from datetime import datetime
from pandas import DataFrame

data = pd.read_csv("bookingholding.csv")

model = Prophet(changepoint_range = 1)
model.fit(data)

def app():
    st.title("Prophet Model Test")

    st.subheader('How does it work and Limitation')

    st.write('User can select the month to get predicted value for it without weekends (market close).')
    st.write('Although the year can be adjusted up to 2025, it is important to note that in time-series analysis, the accuracy of predicted results tends to diminish as you move further from the last data point used for model training')

    pre_month = st.number_input("Select Month", min_value=1, max_value=12, value=1)
    pre_year = st.number_input("Select Year", min_value=2024, max_value=2025, value=2024)
    futuretime = list()
    
    year = str(pre_year)
    month = "%02d" % pre_month

    if pre_year == 2024 and pre_month == 2:
        for k in range(1, 30):
            year_month_date = year + '-' + month + '-' +'%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    elif pre_month == 2:
        for k in range(1, 29):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    elif pre_month == 9 or pre_month == 4 or pre_month == 6 or pre_month == 11:
        for k in range(1, 31):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    else:
        for k in range(1, 31):
            year_month_date = year + '-' + month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
                pass
            else:
                futuretime.append([date_obj])
    
    futuretime = DataFrame(futuretime)
    futuretime.columns = ['ds']

    forecast = model.predict(futuretime)

    df = pd.DataFrame(forecast)

    st.title("One Month Prediction Data")

    st.dataframe(df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

    # Streamlit app title
    st.title("One Month Prediction Plot")

    # Plot the forecast
    # st.line_chart(forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']])

    # Use Plotly Express to create an interactive line chart for the forecast
    fig = px.line(forecast, x='ds', y=['yhat', 'yhat_lower', 'yhat_upper'],
              title='Gold Price Prediction for '+ month + "-"+ year,)
    
    fig.for_each_trace(lambda t: t.update(name=t.name.replace("yhat", "Predicted Price").title()))
    fig.update_layout(legend_title_text='Legend')
    fig.update_layout(xaxis_rangeslider_visible=True)

    # Display the Plotly chart using st.plotly_chart
    st.plotly_chart(fig)


    

    



