#!/usr/bin/env python
# coding: utf-8

import japanize_matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
import streamlit as st

markdown = """
### 「賤ケ岳の7本槍」の能力比較（散布図）
"""
st.write(markdown)

df = pd.read_csv("data/taishi.csv")
sevens = ["加藤清正", "福島正則", "加藤嘉明", "平野長泰",  "脇坂安治", "糟屋武則", "片桐且元"]

#csvから該当する武将のインデックスのリストをつくるための関数
@st.cache
def busho_finder(df, list):
    index_list=[]
    for idx1, name in enumerate(list):
        for idx2, row in df.iterrows():
            if (row["武将姓"] + row["武将名"]) == name:
                index_list.append(idx2)
    return index_list


df = df.iloc[busho_finder(df, sevens)]
st.write("■7本槍の能力データ")
st.dataframe(df)

fig, ax = plt.subplots()
ax.scatter("戦闘", "政治", s=100, alpha=0.4, data=df)
plt.figure(figsize=(10,10))
plt.rcParams["font.size"] = 8
ax.set_title("賤ヶ岳7本槍の能力値　散布図")
ax.set_xlabel("戦闘能力値　合計")
ax.set_ylabel("政治能力値　合計")

for i, name in enumerate(df["武将姓"]):
    if name == "加藤":
        ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], df["武将姓"].iloc[i]+df["武将名"].iloc[i][:1])
    else:
        ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], name)")

# 2グループを円で囲む
circle1 = patches.Circle(xy=(165, 120), radius=25, alpha=0.1)
circle2 = patches.Circle(xy=(117, 92), radius=21, alpha=0.1)
ax.add_patch(circle1)
ax.add_patch(circle2)
                         
st.write("■戦闘・政治能力に基づく散布図")
st.pyplot(fig)

st.write("■所感")
st.write("加藤清正・福島正則・加藤嘉明とそれ以外で群が分かれた格好となった。加藤嘉明は、他の二人や片桐に比べ知名度は低いが、\
         秀吉に見いだされ数々の武功を挙げ、秀吉子飼いでありながら、大阪夏の陣も乗り越えた武将。松山城築城でも知られる。")

# import streamlit as st
# # from streamlit_folium import st_folium
# # import folium

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import patches
# import japanize_matplotlib

# https://welovepython.net/streamlit-folium/
# m = folium.Map(
#     # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
#     location=[35.02968298040031, 137.0168353420444], 
#     # タイル、アトリビュートの指定
#     tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
#     attr='都道府県庁所在地、人口、面積(2016年)',
#     # ズームを指定
#     zoom_start=13
# )
# st_data = st_folium(m, width=2000, height=1500)


# ページ設定
# st.set_page_config(
#     page_title="streamlit-foliumテスト",
#     page_icon="🗾",
#     layout="wide"
# )

# # 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
# m = folium.Map(
#     # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
#     location=[36.56583, 139.88361], 
#     # タイル、アトリビュートの指定
#     tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
#     attr='都道府県庁所在地、人口、面積(2016年)',
#     # ズームを指定
#     zoom_start=6
# )

# # 表示するデータを読み込み
# df = pd.read_csv('pref.csv')

# # 読み込んだデータ(緯度・経度、ポップアップ用文字、アイコンを表示)
# for i, row in df.iterrows():
#     # ポップアップの作成(都道府県名＋都道府県庁所在地＋人口＋面積)
#     pop=f"{row['都道府県名']}({row['都道府県庁所在地']})<br>　人口…{row['人口']:,}人<br>　面積…{row['面積']:,}km2"
#     folium.Marker(
#         # 緯度と経度を指定
#         location=[row['緯度'], row['経度']],
#         # ツールチップの指定(都道府県名)
#         tooltip=row['都道府県名'],
#         # ポップアップの指定
#         popup=folium.Popup(pop, max_width=300),
#         # アイコンの指定(アイコン、色)
#         icon=folium.Icon(icon="home",icon_color="white", color="red")
#     ).add_to(m)

# st_data = st_folium(m, width=1200, height=800)



