import streamlit as st
import numpy as np
from scipy.stats import norm
import datetime

#st.title('-- USDJPY plain vanilla option --')
st.header('USDJPY plain vanilla option')

st.warning('取引条件を入力することでプレインバニラオプション価格が計算できます')

st.sidebar.title('option 条件入力')

options = ["USD Call", "USD Put"] 
CorP = st.sidebar.radio('option type',options, index=0, horizontal=True)
S = st.sidebar.number_input(label='スポットレート', min_value = 0.00, value=100.00)
K = st.sidebar.number_input(label='行使価格', min_value = 0.00, value=100.00)
vol = st.sidebar.number_input(label='ボラティリティ (%)', min_value = 0.00, value = 10.00)
expiry = st.sidebar.date_input(label='権利行使日')
swap_pts = st.sidebar.number_input(label='スワップポイント(JPY/USD)', value = -0.100)
r = st.sidebar.number_input(label='リスクフリーレート (%)', value = 0.00)

F = S + swap_pts

today = datetime.date.today()
T = (expiry - today).days/365
N = norm.cdf
sigma = vol/100

d1 = ((np.log(F/K)) + (sigma**2/2)*T)/(sigma+np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)

Call = np.exp(-r*T)*(F*N(d1) - K*N(d2))
Put = np.exp(-r*T)*(K*N(-d2) - F*N(-d1))

#st.markdown('<span style="color:blue">---</span>', unsafe_allow_html=True)

st.write(f'### {CorP}オプション価格は <span style="color:blue">{Call:.4f}円/ドル</span>です', unsafe_allow_html=True)
