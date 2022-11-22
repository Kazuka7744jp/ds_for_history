#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("東烏に関する調査ページ")

st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["はじめに","残された点帖"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector=="はじめに":
  st.header('はじめに')

elif selector=="page2":
  st.header("残された点帖")
  st.write('点帖とは句会の記録であり、「執筆」が書いたものを「点者」「宗匠」が批点・押印、最終的には、秀逸の者の褒美として贈られるものである')
  st.write('家にこの点帖が残されていたということは、俳号「玄」が当家にまつわる人間である可能性が高い。')
  st.header("点帖1")
  st.image("pic/daikaku1.jpg")
  st.header("点帖2")
  st.image("pic/daikaku2.jpg")
  st.header("点帖3")
  st.image("pic/daikaku3.jpg")
  st.header("点帖4")
  st.image("pic/daikaku4.jpg")
