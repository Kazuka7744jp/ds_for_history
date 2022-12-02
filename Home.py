#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import sqlite3

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.subheader(" 「鬼神もあわれむ俳諧と生きた男」")
st.image("pic/logo.jpg")
st .write('このサイトでは、江戸時代の刈谷の油屋「加塚久右衛門（かづか きゅうえもん　?~1803年?　俳号「東烏」)が残した和歌に\
関する日記「和歌芽籠」を読み解きながら、久右衛門の人生や、それから派生した江戸時代の三河俳諧の調査結果をまとめています。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

st.write('''**■ページ一覧（左のサイドバーから選択してください）**''')
st.write('''**「Azumagarasu」東烏に関する調査ページ**''')
st.write('「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
st.write('「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

# # カウンターの初期値を0に設定
# counter = 0

# # カウンターを表示
# st.write("閲覧人数：", counter)

# # カウンターをインクリメント
# @st.cache
# def increment_counter():
#     global counter
#     counter += 1

# increment_counter()

# # qliteのデータベースと接続
# conn = sqlite3.connect("counter.db")

# # カーソルを生成
# cur = conn.cursor()

# # counterテーブルを作成
# cur.execute("CREATE TABLE IF NOT EXISTS counter (count INTEGER)")

# # counterテーブル



