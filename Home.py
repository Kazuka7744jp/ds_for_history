#!/usr/bin/env python
# coding: utf-8

import streamlit as st

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)
# st.image("pic/logo.jpg")
st.subheader(" 「鬼神もあわれむ俳諧と生きた男」")
left_column1, right_column1 = st.columns(2)
left_column1.image("pic/wakamegomo.jpg")
right_column1 .write('このページでは、江戸時代の刈谷の油屋「加塚久右衛門（かづか きゅうえもん　?~1803年?　俳号「東烏」)が残した和歌に\
関する日記「和歌芽籠」を読み解きながら、久右衛門の人生や、それから派生した江戸時代の三河俳諧の調査結果をまとめたサイトです。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

right_column1.write('''**■ページ一覧（左のサイドバーから選択してください）**''')
right_column1.write('''**「Azumagarasu」東烏に関する調査ページ**''')
right_column1.write('「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
right_column1.write('「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

st.sidebar.st.image("pic/logo.jpg")

