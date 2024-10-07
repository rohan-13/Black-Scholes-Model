import streamlit as st
import math
from scipy.stats import norm
import pandas as pd

st.title('Black Scholes Model')

##puts the numeric inputs into a sidebar
with st.sidebar:
    stock_price = st.number_input("What is the Stock Price", value=42)
    strike_price = st.number_input("What is the Strike Price", value=40)
    time_exp = st.number_input("What is the time of expiration", value=0.5)
    rate = st.number_input("What is the interest rate", value=0.1)
    volatility = st.number_input("What is the volatility", value=0.2) # (σ)


## assigns each input to a variable
S = float(stock_price)
K = float(strike_price)
T = float(time_exp)
R = float(rate)
vol = float(volatility)

##calculates the call and put using the black-scholes model
d1 = (math.log(S/K) + (R + 0.5 * vol**2) * T) / (vol * math.sqrt(T))

d2 = d1 - (vol * math.sqrt(T))

C = (S * norm.cdf(d1)) - (K * math.exp(- R * T) * norm.cdf(d2)) #call price

P = K * math.exp(- R * T) * norm.cdf(-d2) - S * norm.cdf(-d1) #put price

data = pd.DataFrame({
    'stock price': [S],
    'strike price': [K],
    'time to expiration (years)': [T],
    'interest rate': [R],
    'volatility (σ)': [vol],
})


#container for dataset
container1 = st.container()
#container for to display put and call values
container2 = st.container()

container1.dataframe(data, width=1500)

col1, col2 = container2.columns(2)

def local_css(style):
    with open(style) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        col1.markdown('<p class="custom-text">Call Value!</p>', unsafe_allow_html=True)
        col1.markdown('<p class="custom-text">' + str(round(C, 2)) + '</p>', unsafe_allow_html=True)
        col2.markdown('<p class="custom-text">Put Value!</p>', unsafe_allow_html=True)
        col2.markdown('<p class="custom-text">' + str(round(P, 2)) + '</p>', unsafe_allow_html=True)


local_css("style.css")


