# This file will hold all function to be used for analyzing a crypto currency

# functions to include:

# FUNCTION "cryptoPlot" - This is a plotting function that will plot daily close prices for a selected crypto in a line graph. This function will need to accept the input variable "selected". Note that The user will be able to make the selection using streamlit.selectbox. 

# 2. FUNCTION: "cryptoFrame" - A pandas dataframe that show daily open, close, high, low, volume and pct_change fo rthe crypto currency specified by the user.

# FUNCTION: "cryptoChg" - A function that calculates pct_change of the daily close price data



# FUNCTION "nowPrice" returns the current price for the crypto selected.

import streamlit as st
import time
import numpy as np
import datetime
import yfinance as yf

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


option = st.selectbox('Choose a currency to get started.', ('Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

# Just set some loose max and min data parameters.
min_date = datetime.datetime(2010,1,1)
max_date = datetime.datetime(2025,12,12)
st.date_input("Choose the range of dates to be included in your analysis.", (min_date, max_date))

if option =="Bitcoin":
        bitcoin = yf.Ticker("BTC-USD",min_date,max_date) 
elif option =="etheruem":
        ethereum = yf.Ticker("ETH-USD",min_date,max_date)
elif option == tether:
        tether = yf.Ticker("USDT-USD",min_date,max_date)
elif option =="ripple":
        ripple = yf.Ticker("XRP-USD", min_date, max_date)
elif option =="binance":
        binance = yf.Ticker("BNB-USD",min_date, max_date)
else:
    print("oops")
    
# Use the OPTION variable and START, and END variables to pull yf.ticker data
# FOR EXAMPLE:   output = yf.download(option, start=min_date, end=max_date)

if st.button('Execute!'):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    # api dta pull goes here
    st.write("This progress bar will be converted to a function that runs after the user has chosen a specific crypto and a date range.")
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    # execute line chart of daily close prices here
    # execute panda dataframe with pct_change and 7 days of yhat values here.




st.write("""Here is where we will put a line chart that shows daily close prices of the input date range for the selected crypto.""")
st.write("""""")
st.write("""Here is where we will put a dataframe for the selected crypto that includes only those rows from the selected date range. The dataframe will include open, close, high, low, volume, pct_change, and a prediction (yhat)""")

st.write("""Here is where we will put the output from our tweepy sentinment analysis.""")