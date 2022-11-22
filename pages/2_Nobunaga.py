#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from streamlit_folium import st_folium
import folium

# st.header('Under Construction')

m = folium.Map(
    # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
    location=[36.56583, 139.88361], 
    # タイル、アトリビュートの指定
    tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr='都道府県庁所在地、人口、面積(2016年)',
    # ズームを指定
    zoom_start=10
)
st_data = st_folium(m, width=1200, height=800)

# In[ ]:




