#!/usr/bin/env python
# coding: utf-8

import streamlit as st

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title("東烏")
st.subheader(" 「鬼神にもあわれと思わせる俳諧と生きた男の生きざま」")
left_column1, right_column1 = st.columns(2)
left_column1.image("pic/wakamegomo.jpg")
right_column1 .write('このページでは、江戸時代の刈谷の油屋「久右衛門（?~1803年?　俳号「東烏」)が残した和歌に関する日記「和歌芽籠」を読み解きながら、江戸時代の三河俳諧を調査するページです。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

right_column1.write("■ページ一覧（左のサイドバーから選択してください）")
right_column1.write('「Azumagarasu」東烏に関する調査ページ')
right_column1.write('「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
right_column1.write('「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

