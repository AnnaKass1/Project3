# **************************************************************************************
# Detailed analysis and predictions using whatever coin and dat range the user selects
# **************************************************************************************

import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
import time
import numpy as np
import datetime
from prophet import Prophet
import matplotlib.pyplot as plt

bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

st.set_page_config(page_title="Analyze", page_icon="📈")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)


# st.sidebar.header("Analyze")
st.header("Cryptocurrency Performance Analysis")

st.write("""Go deep! Try our expert technical analysis and sentinment analysis tools below!""")

# *****************************************************************************************
# User inputs drives analysis. User picks coin and date range.
# This code could be improved using st.cache
# *****************************************************************************************

option = st.selectbox('Choose a currency to get started.', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

# Just set some loose max and min data parameters.
min_date = datetime.datetime(2013,1,1)
max_date = datetime.datetime(2025,12,12)

st.date_input("Choose the range of dates to be included in your analysis.", (min_date, max_date))

if option =="Bitcoin":
        query = bitcoin.history(start=min_date, end=max_date) 
elif option =="Ethereum":
        query = ethereum.history(start=min_date, end=max_date) 
elif option == "Tether":
        query = tether.history(start=min_date, end=max_date)
elif option =="Ripple":
        query = ripple.history(start=min_date, end=max_date) 
elif option =="Binance":
        query = binance.history(start=min_date, end=max_date)
else:
    print("oops")

if st.button('Execute!'):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    # api dta pull goes here
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

query_result = pd.DataFrame(query)
query_result = query_result.drop(columns=["Dividends", "Stock Splits"])
query_result['% Change'] = query_result["Close"].pct_change() 
st.dataframe(query_result)

chart_data = query_result['Close']
st.line_chart(chart_data, use_container_width=True)

# *************************************************************************
# Predictions using Prophet
# *************************************************************************

days = int(st.selectbox('Choose how many days to predict', [7, 14, 30, 60,90,180])) 
days_ago=int(st.selectbox('Choose how many days of data you want to look back', [7, 14, 30, 60,90,180,360,720])) 
#st.write("""Here is where we will put a chart that shows the predicted yhat values""")

if st.button('Predict!'):

        crypto_data = query_result[['Open']]
        crypto_data.reset_index(inplace=True)

        crypto_data=crypto_data.tail(days_ago)

        crypto_data['Date'] = pd.to_datetime(crypto_data['Date'])
        crypto_data['Date'] =crypto_data['Date'].dt.tz_localize(None)
        # Step 2: Prepare the data for Prophet
        # Prophet requires the columns to be named 'ds' for timestamps and 'y' for the target variable (price)
        crypto_data_prophet = crypto_data.rename(columns={'Date': 'ds', 'Open': 'y'})

        # Step 3: Create a Prophet model and fit it to the data
        model = Prophet()
        model.fit(crypto_data_prophet)

        # Step 4: Create a dataframe with future timestamps for prediction
        future = model.make_future_dataframe(periods=days)  # Predict for the next 180 days

        # Step 5: Make predictions using the Prophet model
        forecast = model.predict(future)

        # Visualize the results
        st.title('Cryptocurrency Price Prediction with Prophet')

        # Display historical prices
        st.subheader('Historical Prices')
        st.line_chart(crypto_data_prophet.set_index('ds'))

        # Display predicted prices
        st.subheader('Predicted Prices')
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(crypto_data_prophet['ds'], crypto_data_prophet['y'], label='Historical Prices', color='blue')
        ax.plot(forecast['ds'], forecast['yhat'], label='Predicted Prices', color='red')
        ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], alpha=0.3, color='orange')
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Price')
        ax.set_title('Cryptocurrency Price Forecast')
        ax.legend()
        st.pyplot(fig)

# **************************************************************************************************************
# Crypto values are driven in part by sentiment. Therefore, we have included our approach to sentinment analysis below.
# **************************************************************************************************************
st.write("""Here is where we will put the output from our tweepy sentinment analysis.""")