#!/usr/bin/env python
# coding: utf-8
from deta import Deta
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
# import time
import os

# load_dotenv(".env")

# DETA_KEY = os.getenv("DETA_KEY")

# deta = Deta(DETA_KEY)

# # Deta上のデータベースに接続
# db = deta.Base("view_count")

# def insert_view(_time):
#     return db.put({"閲覧日時": _time})

# def fetch_all_poets():
#     res = db.fetch()
#     return res.items

# insert_view(time.time())
# data = fetch_all_poets()
# poets = pd.DataFrame(data)

# カウンターを表示
# st.write("閲覧人数：", len(poets))

# name = "東烏"
# area = "三河"
# occupation = "油屋"
# detail = "刈谷の今川で油屋を営む。「和歌芽籠」を執筆。"

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.subheader(" 「鬼神もあわれむ俳諧と生きた男」")
st.image("pic/logo.jpg")
st.write('このサイトでは、江戸時代の刈谷の油屋「加塚久右衛門（かづか きゅうえもん　?~1803年?　俳号「東烏」)が残した和歌に\
関する日記「和歌芽籠」を読み解きながら、久右衛門の人生や、それから派生した江戸時代の三河俳諧の調査結果をまとめています。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

st.write('''**■ページ一覧（左のサイドバーから選択してください）**''')
st.write('''**「Azumagarasu」東烏に関する調査ページ**''')
st.write('「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
st.write('「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

# db = deta.Base("azumagarasu")

# def insert_poet(name, area, occupation, detail):
#     return db.put({"名前": name, "地域": area, "職業": occupation, "人物": detail})

# def fetch_all_poets():
#     res = db.fetch()
#     return res.items

# def get_poet(name):
#     return db.get(name)

# submitted = st.button(label="Save Data")

# if submitted:
#     insert_poet(name, area, occupation, detail)
#     # Detaからデータを取得する
#     data = fetch_all_poets()
#     # DataFrameに変換する
#     poets = pd.DataFrame(data)
#     st.write(poets.loc[:, ["名前", "地域", "職業", "人物"]])
