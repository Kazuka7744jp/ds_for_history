#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("東烏に関する調査ページ")

# st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["はじめに","残された点帖"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector=="はじめに":
  st.header("はじめに")
  st.write("このページは、愛知県刈谷市の東海道沿いの家に残された古文書などに基づく、先祖の在りし日の姿の調査記録になります。")
  st.write("調査者：さとる部長（某研究所歴史アーカイ部部長）、りゅうじえもん（子孫）")
  st.write("調査記録をご覧になる場合は、左側のサイドバーの「ページ選択」よりプルダウンで選択をお願いいたします。")
  st.write("■先祖の年表（随時更新中）")
  

elif selector=="残された点帖":
  st.header("残された点帖")
  st.write('点帖とは句会の記録であり、「執筆」が書いたものを「点者」「宗匠」が批点・押印、最終的には、秀逸の者の褒美として贈られるものである')
  st.write('家にこの点帖が残されていたということは、俳号「玄」が当家にまつわる人間である可能性が高い。')
 
  left_column1, right_column1 = st.beta_columns(2)
  left_column1.header("点帖1")
  left_column1.image("pic/daikaku1.jpg")
  right_column1.header("点帖2")
  right_column1.image("pic/daikaku2.jpg")
  st.header("点帖3")
  st.image("pic/daikaku3.jpg")
  st.header("点帖4")
  st.image("pic/daikaku4.jpg")
