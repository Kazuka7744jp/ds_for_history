# !/usr/bin/env python
# coding: utf-8
# import datetime
# from deta import Deta
# from dotenv import load_dotenv
import streamlit as st
# from time import time
# import os

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)

df_haijin = pd.read_csv("data/data_haijin.csv", keep_default_na=False)

st.header("三河俳人検索データベース")
st.image("pic/header.jpg")
st.write("三河俳人に関する情報をお持ちの方は、ぜひ情報提供をお願いいたします。japanhistorydiscovery@gmail.com")

st.write('■俳人検索')
st.subheader("「俳名」か「本名・別名」を入力してください。")
haijin_input = st.text_input("検索キーワード入力欄")
if not haijin_input:
  st.write("何か単語を入力してください。")
else:
  df_selected = df_haijin[(df_haijin['俳名'].str.contains(haijin_input)) | (df_haijin['本名/別名'].str.contains(haijin_input))]
  st.write(f"{len(df_selected)}件の検索結果がありました。")
  st.table(df_selected)

df_len = len(df_haijin)
st.write('■データベース一覧')
col1, col2, col3, col4 = st.columns(4)
col1.metric("登録人数", df_len)
col2.metric("調査済句集", len(df_haijin.columns)-9)
#   col3, col4 = st.columns(2)
col3.metric("本名判明率", "{:.1%}".format((df_haijin["本名/別名"]!="").sum()/df_len))
col4.metric("職業判明率", "{:.1%}".format((df_haijin["職業_詳細"]!="").sum()/df_len))
st.write(df_haijin)

st.write('■職業別の人数の割合')
# 職業列が空でない行を抽出する
df_job = df_haijin[df_haijin["職業"] != ""]
# 職業列の要素の値が何回登場したかを集計する
df_job = df_job["職業"].value_counts()
# SeriesをDataFrameに変換する
df_job = pd.DataFrame(df_job)
job_pie = px.pie(data_frame=df_job,
   values=df_job["職業"],
   names=df_job.index,
   hover_name=df_job.index)
st.plotly_chart(job_pie)

st.write("■門下別の職業の割合")
st.image("pic/monka.png")
# st.subheader(" 「鬼神もあわれむ俳諧と生きた男」")
# st.image("pic/logo.jpg")
# st.markdown("---")
# st.write(''':seedling: **About this website** :seedling:''')
# st.write('このサイトでは、江戸時代の刈谷の油屋「加塚久右衛門（かづか きゅうえもん　?~1803年?　俳号「東烏」)が残した和歌に\
# 関する日記「和歌芽籠」を読み解きながら、久右衛門の人生や、それから派生した江戸時代の三河俳諧の調査結果をまとめています。あわせて管理人のPythonによるデータ可視化の練習結果も掲載しています。')

# st.write(''':seedling: **ページ一覧** :seedling:''')
# st.write("各ページは、左側のサイドバーから選択してください")
# st.write(''':one:**「Azumagarasu」東烏に関する調査ページ**''')
# st.write(':two:「Nobunaga」信長の野望のデータセットを利用したデータ可視化練習')
# # st.write(':three:「BaseBall」2020年のプロ野球選手データを利用したデータ可視化練習')

# # load_dotenv(".env")
# # DETA_KEY = os.getenv("DETA_KEY")
# # deta = Deta(DETA_KEY)

# # # Deta上のデータベースに接続
# # db = deta.Base("view_count")

# # @st.cache
# # def insert_view(_time):
# #     return db.put({"閲覧日時": _time})

# # @st.cache
# # def fetch_all_poets():
# #     res = db.fetch()
# #     return res.items

# # insert_view(str(datetime.datetime.now()))

# # data = fetch_all_poets()
# # views = pd.DataFrame(data)

# # st.markdown("---")
# # # カウンターを表示
# # st.write(f"これまで、:star:累計{len(views)}人:star:の方に、東烏の生き方に触れていただきました。ありがとうございます:bamboo:")
