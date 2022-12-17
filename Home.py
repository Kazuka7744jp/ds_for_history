# !/usr/bin/env python
# coding: utf-8
# import datetime
# from deta import Deta
# from dotenv import load_dotenv
import streamlit as st
# from time import time
# import os

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.subheader(" 「鬼神もあわれむ俳諧と生きた男」")
st.image("pic/logo.jpg")
st.markdown("---")
st.write(''':seedling: **About this website** :seedling:''')
st.write('このサイトでは、江戸時代の刈谷の油屋「加塚久右衛門（かづか きゅうえもん　?~1803年?　俳号「東烏」)が残した和歌に\
関する日記「和歌芽籠」を読み解きながら、久右衛門の人生や、それから派生した江戸時代の三河俳諧の調査結果をまとめています。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

st.write(''':seedling: **ページ一覧** :seedling:''')
st.write("各ページは、左側のサイドバーから選択してください")
st.write(''':one:**「Azumagarasu」東烏に関する調査ページ**''')
st.write(':two:「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
# st.write(':three:「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

# load_dotenv(".env")
# DETA_KEY = os.getenv("DETA_KEY")
# deta = Deta(DETA_KEY)

# # Deta上のデータベースに接続
# db = deta.Base("view_count")

# @st.cache
# def insert_view(_time):
#     return db.put({"閲覧日時": _time})

# @st.cache
# def fetch_all_poets():
#     res = db.fetch()
#     return res.items

# insert_view(str(datetime.datetime.now()))

# data = fetch_all_poets()
# views = pd.DataFrame(data)

# st.markdown("---")
# # カウンターを表示
# st.write(f"これまで、:star:累計{len(views)}人:star:の方に、東烏の生き方に触れていただきました。ありがとうございます:bamboo:")
