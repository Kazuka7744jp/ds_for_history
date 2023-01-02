import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)

df_haijin = pd.read_csv("data/data_haijin.csv", keep_default_na=False)
# df_haijin['句集登場回数'] = df_haijin['句集登場回数'].astype("int64")
st.image("pic/logo.jpg")
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
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("登録人数", df_len)
col2.metric("調査済句集", 223)
col3.metric("本名判明率", "{:.1%}".format((df_haijin["本名/別名"]!="").sum()/df_len))
col4.metric("職業判明率", "{:.1%}".format((df_haijin["職業_詳細"]!="").sum()/df_len))
col5.metric("出身判明率", "{:.1%}".format((df_haijin["出身地"]!="").sum()/df_len))

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

st.write("■門下別の職業の割合「卓池」")
st.image("pic/takuchi.png")

st.write("■門下別の職業の割合「卓池以外」")
st.image("pic/monka.png")

st.write('■調査済句集一覧')
df_kusyu = pd.read_csv("data/kusyu.csv", usecols=[["資料名", "年代", "内容", "備考", "所蔵", "チェック"]])
st.write(df_kusyu)
