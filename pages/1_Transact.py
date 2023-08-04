import streamlit as st
import yfinance as yf
import requests
import os
import json
from decimal import Decimal

st.set_page_config(page_title="Transact")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

cash_balance = 1000

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

# create a two column page. First column will be BUY. Second column will be SELL.
col1, col2 = st.columns(2)

picks = ['Buy','Sell']
transaction = st.radio("Please choose a transaction type",(picks))
if transaction =='Buy':
    st.write('You have $',cash_balance,' in USD cash available')
elif transaction == 'Sell':
    wallet_id = st.text_input("Enter your Wallet ID")
else:
    print("Error")

#Enter your crypto wallet ID here: st.input() STR
# If the buy amount exceeds the amount of cash the user has, then throw an error
# If the sell amount exceeds the amount of the selected crypto currency possessed by the user then throw an error.

options = ['Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance']
choice = st.selectbox('Choose a cryptocurrency to get started.', options)

if choice == "Bitcoin":
    output = requests.get(btc_url).json()
elif choice == "Ethereum":
    output = requests.get(eth_url).json()
elif choice == "Tether":
    output = requests.get(usdt_url).json()
elif choice == "Ripple":
    output = requests.get(xrp_url).json()
elif choice == "Binance":
    output = requests.get(bnb_url).json()
else: 
    print("Pick something!!")

# Once a crpyto is chosen we also need to calculate how muchof that particular crpyto the user owns. We will print it out in a statement after they make the selection.

# Grabbing the current price in USD
now_price = output['data']['priceUsd']
now_price = Decimal(now_price)
print(now_price)

amt = st.number_input("Amount")
amt = Decimal(amt)

st.button('Execute!')

value = now_price * amt
print(value)

st.write('Confirmation of transaction goes down here')