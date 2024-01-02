import streamlit as st
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from PIL import Image
from matplotlib import pyplot

def app():
    data = pd.read_csv("bookingholding.csv")

    st.title("Project Design")

    st.subheader("Time Series Analysis using Hyperparameter Tuning")

    desgn = '''Prophet is a method for forecasting time-series from incorporate algorithms whose nonlinear patterns correlate to seasonal, daily, weekly, 
    and holiday events. '''

    justified_text = f"<div style='text-align: justify;'>{desgn}</div>"

    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    #Build Model

    from prophet import Prophet

    model = Prophet()
    model.fit(data)
    

    explain = '''First we need to import the prophet after installing the package and train the model with five year data that I mentioned in About Data session from 2018 to 2023.'''

    justified_explain = f"<div style='text-align: justify;'>{explain}</div>"

    st.markdown(justified_explain, unsafe_allow_html=True)
    st.markdown("##")

    build_model = """
    from prophet import Prophet

    model = Prophet()
    model.fit(data) """

    st.code(build_model, language='python')

    #Generate last year data

    explain1 = '''Then, the following code is to generate the trading day for 2023 without the weekends since the market closes on weekends. Basically, we will use this 2023 data as test data.'''

    justified_explain1 = f"<div style='text-align: justify;'>{explain1}</div>"

    st.markdown(justified_explain1, unsafe_allow_html=True)
    st.markdown("##")

    generate_date = '''
    from datetime import datetime
    from pandas import DataFrame

    future = list()

    years = [23]

    for i in years:
    year = '20%02d' %i
    for j in range(1, 13):
        year_month = year + '-' + '%02d' % j
        #Feb
        if j == 2:
        for k in range(1, 29):
            year_month_date = year_month + '-' + '%02d' % k
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
            pass
            else:
            future.append([date_obj])
        #Sept, Apr, Jun, Nov
        elif j == 9 or j == 4 or j == 6 or j == 11:
        for p in range(1, 31):
            year_month_date = year_month + '-' + '%02d' % p
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
            pass
            else:
            future.append([date_obj])
        #Rest
        else:
        for q in range(1, 32):
            year_month_date = year_month + '-' + '%02d' % q
            date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
            if date_obj.weekday() >= 5:
            pass
            else:
            future.append([date_obj])

    future =DataFrame(future)
    future.columns = ['ds']
    '''

    st.code(generate_date, language='python')

    future = list()

    years = [23]

    for i in years:
        year = '20%02d' %i
        for j in range(1, 13):
            year_month = year + '-' + '%02d' % j
            #Feb
            if j == 2:
                for k in range(1, 29):
                    year_month_date = year_month + '-' + '%02d' % k
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])
            #Sept, Apr, Jun, Nov
            elif j == 9 or j == 4 or j == 6 or j == 11:
                for p in range(1, 31):
                    year_month_date = year_month + '-' + '%02d' % p
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])
            #Rest
            else:
                for q in range(1, 32):
                    year_month_date = year_month + '-' + '%02d' % q
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])

    future =DataFrame(future)
    future.columns = ['ds']
    st.markdown("Output: ")
    st.write(future)

    #Forecast
    st.markdown('''Now, we can predict the generate dates using the predict method from the model trained.''')

    forecast_code = '''
    forecast = model.predict(future)
    forecast'''

    st.code(forecast_code, language='python')

    forecast = model.predict(future)
    st.write(forecast)

    st.markdown('''As a result, we get a bunch of data as above. But we will only use y_hat, yhat_lower, yhat_upper, and ds columns.''')

    st.subheader ('Finding MAE, MSE, RMSE')
    st.markdown('Now, we need to find the value of Mean Absolute Error, Mean Squared Error, Root Mean Squared Error before Hyperparameter Tuning by adding changepoint range.')

    error_code = '''
    y_true = data['y'][-260:].values
    y_pred = forecast['yhat'].values

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse**(1/2)
    '''

    st.code(error_code, language='python')

    from sklearn.metrics import (mean_absolute_error, mean_squared_error)

    y_true = data['y'][-260:].values
    y_pred = forecast['yhat'].values

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse**(1/2)

    st.write('MAE: %.3f' % mae)
    st.write('MSE: %.3f' % mse)
    st.write('RMSE: %.3f' % rmse)

    st.subheader("Prophet Model Components")

    img = Image.open("model_components.png")

    st.image(img, caption='Yearly, Weekly, Monthly Trend')

    explain3 = '''As we can see in the above plots, when we have a look at the trend (first figure), Booking Holding Inc. stock price has been increasing gradually throughout the year 2023.
    According to the weekly (second figure), price usually go up when the market opens on Monday and go down when the market close on Friday while consolidating during the week.
    Lastly, yearly (third figure) shows that price usually is up during the beginning month of the year while displaying up and down from time to time. But price normally is down(lowest) around November before 
    major increase.'''

    justified_explain3 = f"<div style='text-align: justify;'>{explain3}</div>"

    st.markdown(justified_explain3, unsafe_allow_html=True)
    st.markdown("##")

    st.subheader('Training model using 100 percent of the data using Hyperparameter Tuning')
    tuning_code = '''
    model = Prophet(changepoint_range = 1)
    model.fit(data)
    '''
    st.code(tuning_code, language='python')

    model = Prophet(changepoint_range = 1)
    model.fit(data)

    explain4 = '''Now, we will train our data using the prophet with Hyperparameter and making the changepoint_range to 1. By default, changepoint_range in prophet is 0.8 meaning only 80 percent of the data will be utilized while 1 being the max applying all data.'''

    justified_explain4 = f"<div style='text-align: justify;'>{explain4}</div>"

    st.markdown(justified_explain4, unsafe_allow_html=True)
    st.markdown("##")

    hyper_code = '''
    future = list()

    years = [23]

    for i in years:
        year = '20%02d' %i
        for j in range(1, 13):
            year_month = year + '-' + '%02d' % j
            #Feb
            if j == 2:
                for k in range(1, 29):
                    year_month_date = year_month + '-' + '%02d' % k
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])
            #Sept, Apr, Jun, Nov
            elif j == 9 or j == 4 or j == 6 or j == 11:
                for p in range(1, 31):
                    year_month_date = year_month + '-' + '%02d' % p
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])
            #Rest
            else:
                for q in range(1, 32):
                    year_month_date = year_month + '-' + '%02d' % q
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        future.append([date_obj])

    future =DataFrame(future)
    future.columns = ['ds']

    forecast_aftertuning= model.predict(future)
    model.plot(forecast_aftertuning)
    '''

    st.code(hyper_code, language='python')

    hyperfuture = list()

    year24 = [24]

    for i in years:
        year = '20%02d' %i
        for j in range(1, 13):
            year_month = year + '-' + '%02d' % j
            #Feb
            if j == 2:
                for k in range(1, 29):
                    year_month_date = year_month + '-' + '%02d' % k
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        hyperfuture.append([date_obj])
            #Sept, Apr, Jun, Nov
            elif j == 9 or j == 4 or j == 6 or j == 11:
                for p in range(1, 31):
                    year_month_date = year_month + '-' + '%02d' % p
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        hyperfuture.append([date_obj])
            #Rest
            else:
                for q in range(1, 32):
                    year_month_date = year_month + '-' + '%02d' % q
                    date_obj = datetime.strptime(year_month_date, '%Y-%m-%d').date()
                    if date_obj.weekday() >= 5:
                        pass
                    else:
                        hyperfuture.append([date_obj])

    hyperfuture =DataFrame(hyperfuture)
    hyperfuture.columns = ['ds']

    forecast_aftertuning= model.predict(hyperfuture)
    st.markdown('Outcome: after hyperparameter tuning with changepoint_range = 1')
    st.write(forecast_aftertuning[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

    img1 = Image.open("hyperparameter.png")

    st.image(img1, caption='Predicted and Actual Data for 2023')

    explain4 = '''As you can see in the figure, blue line representing the predicted data(y_hat) and light blue range representing upper(yhat_upper) and lower(yhat_lower) confidence intervals.'''

    justified_explain4 = f"<div style='text-align: justify;'>{explain4}</div>"

    st.markdown(justified_explain4, unsafe_allow_html=True)
    st.markdown("##")

    st.subheader('Finding MAE, MSE, RMSE after Hyperparameter Tuning')

    errorafter_code = '''
    y_true_after = data['y'][-260:].values
    y_pred_after = forecast_aftertuning['yhat'].values

    mae = mean_absolute_error(y_true_after, y_pred_after)
    mse = mean_squared_error(y_true_after, y_pred_after)
    rmse = mse**(1/2)

    print('MAE: %.3f' % mae)
    print('MSE: %.3f' % mse)
    print('RMSE: %.3f' % rmse)
    '''
    st.code(errorafter_code, language='python')

    y_true_after = data['y'][-260:].values
    y_pred_after = forecast_aftertuning['yhat'].values

    mae = mean_absolute_error(y_true_after, y_pred_after)
    mse = mean_squared_error(y_true_after, y_pred_after)
    rmse = mse**(1/2)
    st.write('Outcome: ')
    st.write('MAE: %.3f' % mae)
    st.write('MSE: %.3f' % mse)
    st.write('RMSE: %.3f' % rmse)

    st.markdown('As you can see in here, MAE, MSE and RMSE value reduced after making the change point to 1, utilizing all data.')

    st.subheader('Finding the changepoint')

    change_code = '''
    from prophet.plot import add_changepoints_to_plot

    fig = model.plot(forecast_aftertuning)
    change_points = add_changepoints_to_plot(fig.gca(), model, forecast_aftertuning)
    '''
    st.code(change_code , language='python')

    img2 = Image.open("changepoint.png")

    st.image(img2, caption='Change point detection')

    st.write('Red Lines represents the change points in time when price has a significant movement, up or down.')

    st.header('Comparing the actual data and predicted data')
   
    compare_code = '''
    from matplotlib import pyplot
    pyplot.plot(y_true, label='Actual')
    pyplot.plot(y_pred, label='Predicted')
    pyplot.legend()
    pyplot.show()
    '''

    st.code(compare_code , language='python')

    img3 = Image.open("predictvsactual.png")

    st.image(img3, caption='Predict vs Actual Data')
