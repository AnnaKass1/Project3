import streamlit as st
import yfinance as yf
import feedparser
import webbrowser
import pandas as pd
import requests

st.set_page_config(page_title="Home")

bitcoin = yf.Ticker("BTC-USD")
ethereum = yf.Ticker("ETH-USD")
tether = yf.Ticker("USDT-USD")
ripple = yf.Ticker("XRP-USD")
binance = yf.Ticker("BNB-USD")

btc_url = "https://api.coincap.io/v2/assets/bitcoin"
eth_url = "https://api.coincap.io/v2/assets/ethereum"
usdt_url = "https://api.coincap.io/v2/assets/tether"
xrp_url = "https://api.coincap.io/v2/assets/xrp"
bnb_url = "https://api.coincap.io/v2/assets/binance-usd"

col1, col2 = st.columns([9,3])

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 150px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("Resources/super_crypto.png", use_column_width =True)


with col1:
    crypto_logos = st.image(["https://cryptologos.cc/logos/bitcoin-btc-logo.png?v=025", 
                            "https://cryptologos.cc/logos/ethereum-eth-logo.png?v=025", 
                            "https://cryptologos.cc/logos/tether-usdt-logo.png?v=025", 
                            "https://cryptologos.cc/logos/xrp-xrp-logo.png?v=025", 
                            "https://cryptologos.cc/logos/bnb-bnb-logo.png?v=025"], width =50)
                  

col1.write("<h1 style= 'text-align: center'>Welcome to Super Crypto!</h1>", unsafe_allow_html=True)


                  
col1.markdown("""
This platform enables users to both analyze and trade the top 5 crpyto currencies by market cap.
They are Bitcoin, Ethereum, Tether, Binance and Ripple. 
Not only can users perform the basic technical analysis of a crypto currency, 
they will see a predictive analysis of each crypto and we have also added a sentimment analysis capability to the platform. 
Users can get a feel for the mood of the public around the crpyto of their choice. 
We do this by analyzing Tweets and producing a categorized output.
""")

with col1:
    source_dict={'btc': btc_url, 
    'eth': eth_url, 
    'usdt': usdt_url, 
    'xrp': xrp_url, 
    'bnb': bnb_url}

    data_dict={}

    for coin in source_dict: 
        data=requests.get(source_dict[coin]).json()
        data_dict[coin]=float(data['data']['changePercent24Hr'])

    max_key = max(data_dict, key=data_dict.get)
    min_key = min(data_dict, key=data_dict.get)
    max_value = max(data_dict.values())
    min_value = min(data_dict.values())

    st.markdown('**:blue[Todays Higlights]**', unsafe_allow_html=False)
    if max_value > 0:
        st.write(max_key, "experienced the best positive change at ",max_value," %")
    elif max_value < 0:
        st.write(max_key, "experienced a least negative change of",max_value,"%")
    else:
        st.write("No changes to report")

    if min_value > 0:
        st.write("The smallest increase on the day was ",min_key, " with a change of",min_value,"%")
    elif min_value < 0:
        st.write("The biggest negative change on the day goes to ",min_key," with a change of ", min_value,"%")
    else:
        st.write("No changes to report")

# *****************************************************************************************************
# This is the current position of every coin we track
# Code works
# Need to change order of columns
# *****************************************************************************************************
    bitcoin_day = bitcoin.history(period="1d")
    bitcoin_day_df = pd.DataFrame(bitcoin_day)
    bitcoin_day_df = bitcoin_day_df.drop(columns=["Dividends", "Stock Splits"])
    bitcoin_chg = bitcoin.history(period="2d")
    bitcoin_day_df['% Change'] = bitcoin_chg["Close"].pct_change() 
    bitcoin_day_df['Coin'] = "Bitcoin"

    ethereum_day = ethereum.history(period="1d")
    ethereum_day_df = pd.DataFrame(ethereum_day)
    ethereum_day_df = ethereum_day_df.drop(columns=["Dividends", "Stock Splits"])
    ethereum_chg = ethereum.history(period="2d")
    ethereum_day_df['% Change'] = ethereum_chg["Close"].pct_change() 
    ethereum_day_df['Coin'] = "Ethereum"

    tether_day = tether.history(period="1d")
    tether_day_df = pd.DataFrame(tether_day)
    tether_day_df = tether_day_df.drop(columns=["Dividends", "Stock Splits"])
    tether_chg = tether.history(period="2d")
    tether_day_df['% Change'] = tether_chg["Close"].pct_change() 
    tether_day_df['Coin'] = "Tether"

    ripple_day = ripple.history(period="1d")
    ripple_day_df = pd.DataFrame(ripple_day)
    ripple_day_df = ripple_day_df.drop(columns=["Dividends", "Stock Splits"])
    ripple_chg = ripple.history(period="2d")
    ripple_day_df['% Change'] = ripple_chg["Close"].pct_change() 
    ripple_day_df['Coin'] = "Ripple"

    binance_day = binance.history(period="1d")
    binance_day_df = pd.DataFrame(binance_day)
    binance_day_df = binance_day_df.drop(columns=["Dividends", "Stock Splits"])
    binance_chg = binance.history(period="2d")
    binance_day_df['% Change'] = binance_chg["Close"].pct_change() 
    binance_day_df['Coin'] = "Binance"

    all_coins_df = pd.DataFrame()
    all_coins_df= pd.concat([bitcoin_day_df,  ethereum_day_df, tether_day_df, ripple_day_df, binance_day_df],axis="rows", join="outer")
    
    st.write(all_coins_df[['Coin', 'Open', 'Close', 'High', 'Low', 'Volume', '% Change']], use_column_width =True)


# ***********************************************************************************
# Column 2 is reserved for the RSS Feed content
# ***********************************************************************************

with col2:
    col2.markdown("<h4 style= 'text-align: center'>NEWS</h4>", unsafe_allow_html=True)
    feed = feedparser.parse("https://cointelegraph.com/rss")
    feed_title = feed['feed']['title']
    feed_entries = feed.entries
    for entry in feed.entries:
       article_title = entry.title
       article_link = entry.link
    #df = pd.DataFrame(feed_entries, columns=["Crypto", "link"])
    data = {}
    for entry in feed.entries:
        #data.setdefault("Crypto",[])
        #data.setdefault("link",[])
        data.setdefault("What is happening today in crypto   ",[])
        #data["Crypto"].append(entry.title)
        #data["link"].append(entry.link)
        data["What is happening today in crypto   "].append(f'<a href = "{entry.link}">{entry.title}</a>')

    st.write(pd.DataFrame(data).to_html(escape=False, index=False), unsafe_allow_html = True)