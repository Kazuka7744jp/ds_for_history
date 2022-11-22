#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from streamlit_folium import st_folium
import folium

# st.header('Under Construction')
# https://welovepython.net/streamlit-folium/
m = folium.Map(
    # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
    location=[35.02968298040031, 137.0168353420444], 
    # タイル、アトリビュートの指定
    tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr='都道府県庁所在地、人口、面積(2016年)',
    # ズームを指定
    zoom_start=13
)
st_data = st_folium(m, width=2000, height=1500)

# In[ ]:




