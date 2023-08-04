import streamlit as st
import yfinance as yf
import requests

# The purpose of this page is to help users calulate how much of a crypto they could buy for X dollars.
# This will require the CURREN tprice of whatever crypto they select. 

st.set_page_config(page_title="Calculator")

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)

st.markdown("""## Conversion Calculator""")

from_price = 0
to_price = 0

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

with st.form("user_form"):
    amt = st.number_input("Amount to convert")
    from_opt = st.selectbox('Convert', ('USD','Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))
    to_opt = st.selectbox('To', ('USD', 'Bitcoin', 'Ethereum', 'Tether', 'Ripple', 'Binance'))

    submitted = st.form_submit_button("Calculate")
    if submitted:        
       st.write("Converting W amount of X to Y comes to Z dollars" )
    
source_dict={'btc': btc_url, 
'eth': eth_url, 
'usdt': usdt_url,
'xrp': xrp_url, 
'bnb': bnb_url}

data_dict={}

for coin in source_dict: 
    data=requests.get(source_dict[coin]).json()
    data_dict[coin]=float(data['data']['priceUsd'])
    
if from_opt =="Bitcoin":
    from_price = data_dict.get('btc')
elif from_opt =="USD":
    from_price = 1
elif from_opt =="Ethereum":
    from_price = data_dict.get('eth')
elif from_opt == "Tether":
    from_price = data_dict.get('usdt')
elif from_opt =="Ripple":
    from_price = data_dict.get('xrp')
elif from_opt =="Binance":
    from_price = data_dict.get('bnb')
else:
    print("oops")

if from_opt =="Bitcoin":
    to_price = data_dict.get('btc')
elif from_opt =="USD":
    to_price = 1
elif from_opt =="Ethereum":
    to_price = data_dict.get('eth')
elif from_opt == "Tether":
    to_price = data_dict.get('usdt')
elif from_opt =="Ripple":
    to_price = data_dict.get('xrp')
elif from_opt =="Binance":
    to_price = data_dict.get('bnb')
else:
    print("oops")

from_total = amt*from_price
calculated = from_total/to_price

st.write(calculated)
     

# st.write("For reference only")
# st.write(data_dict)