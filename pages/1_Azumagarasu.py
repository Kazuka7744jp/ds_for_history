#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import streamlit as st

df = pd.read_csv("data/nenpyo.csv")

st.title("東烏に関する調査ページ")

# st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["はじめに","残された点帖"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector=="はじめに":
  st.header("はじめに")
  st.write("このページは、愛知県刈谷市の東海道沿いの家に残された古文書などに基づく、先祖の在りし日の姿の調査記録になります。")
  st.write('''
        調査記録をご覧になる場合は、**左側のサイドバーの「ページ選択」よりプルダウンで選択**をお願いいたします。
        ''')
  st.subheader("調査者")
  st.write("「さとる部長」（某研究所歴史アーカイ部部長。独学でくずし字を読むすごい人）")
  st.write("「りゅうじえもん」（久右衛門の子孫。当サイト管理人。データ可視化担当）")

  st.write("■加塚家年表（随時更新中）")
  st.table(df)

elif selector=="残された点帖":
  st.header("残された点帖")
  st.write('当初、これが一体なんなのかが皆目見当がつかなかったため、さとる部長と専門の先生にご相談した結果、句会の「点帖」であることが分かった。')
  st.write('点帖とは句会の記録であり、「執筆」が書いたものを「点者」「宗匠」が批点・押印、最終的には、秀逸の者の褒美として贈られるものである。')
  
  st.write('家にこの点帖が残されていたということは、この句会で入選した俳号「玄」が当家にまつわる人間である可能性が高まった。東烏に加え、「玄」も調査対象に加わることとなった。\
  玄は俳号を省略したものであり、俳号は「玄〇」である可能性が高い。')
 
  left_column1, right_column1 = st.columns(2)
  left_column1.write("点帖 表紙")
  left_column1.image("pic/daikaku1.jpg")
  right_column1.write("「玄」入選　「錦ともいふべき形の入日哉」")
  right_column1.image("pic/daikaku2.jpg")
  left_column2, right_column2 = st.columns(2)
  left_column2.write("「玄」未入選　「塩家とは思へぬ形の入日哉」")
  left_column2.image("pic/daikaku3.jpg")
  right_column2.write("点帖 最後")
  right_column2.image("pic/daikaku4.jpg")
  
  st.write("あわせて、専門家の先生により、この句会の点者が、尾張・三河では著名な「竹内（大鶴庵）塊翁」であることが分かった。名のある点者の句会へ参加し、\
           入選していることで、それ相応の実力と関わり方をしていることが分かり、今後の調査の大きな糸口となった。")
  st.write("「竹内（大鶴庵）塊翁」 1764－1829　江戸時代中期-後期の俳人。明和元年生まれ。加藤暁台(きょうたい),井上士朗にまなぶ。名古屋で俳諧(はいかい)点者をつとめた。\
  文政12年10月17日死去。66歳。尾張(おわり)(愛知県)出身。名は春政。通称は九右衛門。別号に竹有,大鶴庵。編著に「あをむしろ」「しまめくり」など。")
  st.write("「デジタル版 日本人名大辞典+Plus」より")
