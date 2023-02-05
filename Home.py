# MIT License

# Copyright (c) 2021 Yash AI

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import streamlit as st
import pandas as pd
from streamlit_card import card
    
# st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", initial_sidebar_state="auto", menu_items=None)


@st.cache
def load_data():
    df_haijin = pd.read_csv("data/data_haijin.csv", keep_default_na=False)
    return df_haijin

df_haijin = load_data()

st.image("pic/logo_small.jpg")
st.header("三河俳人検索データベース")
st.image("pic/head2.jpeg")
st.write("三河俳人に関する情報をお持ちの方は、ぜひ情報提供をお願いいたします。japanhistorydiscovery@gmail.com")

st.write('■俳人検索')
df_len = len(df_haijin)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("登録人数", df_len)
col2.metric("調査済句集", 223)
col3.metric("本名判明率", "{:.1%}".format((df_haijin["本名/別名"]!="").sum()/df_len))
col4.metric("職業判明率", "{:.1%}".format((df_haijin["職業_詳細"]!="").sum()/df_len))
col5.metric("出身判明率", "{:.1%}".format((df_haijin["出身地"]!="").sum()/df_len))

st.subheader("検索条件を入力または選択してください")
haijin_input = st.text_input("俳名または本名・別名")
# location_input = st.text_input("出身地")
job_input = st.text_input("職業")
# haijin_input = st.selectbox("俳名または本名・別名", [""] + sorted(list(df_haijin['俳名'].unique()) + sorted(list(df_haijin['本名/別名'].unique())))
location_input = st.selectbox("出身地", [""] + sorted(list(df_haijin['出身地'].unique())))
# job_input = st.selectbox("職業", [""] + sorted(list(df_haijin['職業_詳細'].unique())))

if haijin_input or location_input or job_input:
    conditions = (df_haijin['俳名'].str.contains(haijin_input) | df_haijin['本名/別名'].str.contains(haijin_input)) &(df_haijin['出身地'].str.contains(location_input)) &(df_haijin['職業'].str.contains(job_input) | df_haijin['職業_詳細'].str.contains(job_input))

    df_selected = df_haijin[conditions]
    st.write(f"{len(df_selected)}件の検索結果がありました。")
    st.write("■検索結果一覧")
    st.dataframe(df_selected)
    st.write("■検索結果個人カード　※黄色い英文字が出る場合は読み込み中です")

#     num_columns = 5
#     num_cards = len(df_selected)
#     num_rows = (num_cards + num_columns - 1) // num_columns

#     for row_index in range(num_rows):
#         st.empty()
#         for column_index in range(num_columns):
#             card_index = row_index * num_columns + column_index
#             if card_index >= num_cards:
#                 break
#             person = df_selected.iloc[card_index]
#             card(
#                 title=person["俳名"],
#                 text="【本名/別名】 " + person["本名/別名"] +
#                 "\n\n【出身地】 " + person["出身地"] +
#                 "\n\n【職業】 " + person["職業_詳細"] +
#                 "\n\n【句集登場回数】" + person["句集登場回数"] + "回" +
#                 "\n\n【備考】 " + person["備考"],
#                 image= person["URL"],
#                 url=""
               
#             )

                              
    for index, person in df_selected.iterrows():
      card(
          title=person["俳名"],
          text="【本名/別名】 " + person["本名/別名"] +
          "\n\n【出身地】 " + person["出身地"] +
          "\n\n【職業】 " + person["職業_詳細"] +
          "\n\n【句集登場回数】" + person["句集登場回数"] + "回" +
          "\n\n【備考】 " + person["備考"],
          image= person["URL"],
          url=""
         
      )


# if not haijin_input:
#   st.write("何か単語を入力してください。")
# else:
#   df_selected = df_haijin[(df_haijin['俳名'].str.contains(haijin_input)) | (df_haijin['本名/別名'].str.contains(haijin_input))]
#   st.write(f"{len(df_selected)}件の検索結果がありました。")
#   st.dataframe(df_selected)

else:
    st.write("条件を入力してください")
    
col6, col7 = st.columns(2)

with col6:
    st.write("test")

with col7:
    st.write("test")
    
st.write('■データベース一覧')
st.dataframe(df_haijin, width=None, height=500)
st.write("■門下・派閥の人数")

st.image("pic/deshi.png")

st.write("■門下別の職業の割合「卓池」")
st.image("pic/takuchi.png")

st.write("■門下別の職業の割合「卓池以外」")
st.write("門下の属性の違いを調査していますが、まだまだ、どの派閥であったかや職業が判明している人数が足りませんので、皆様からの情報お待ちしています。")
st.image("pic/monka.png")

st.write("■ネットワーク図（networkX：spring_layout）")
st.write("以下では、句集登場回数トップ100の俳人たち（＋グラフ作成者の先祖の「東烏」）をネットワーク図にしました。")
st.write("使用しているspring_layoutアルゴリズムは登場回数の多いノード(俳名がある円)が中央に配置され、それ以外のノードがその周りに配置されるようなグラフが生成されることが特徴です。登場回数の多さは、ノードの大きさに反映されています。")
st.write("同じ句集に一度でも登場しているノード同士には引力が発生しますが、その回数の多さは位置関係には反映されていません。")
st.write("（この図で見て取るのは難しいですが、同じ句集に登場する頻度はエッジ(繋ぐ線)の太さに反映）")
st.write("大御所達の中で比較すると、東烏は、やはり末席の末席となることがわかります。")
st.write("派閥の色：　「卓池」…黄色、「秋挙」…緑　「木朶」…水色　「祖風」…紫　「無派閥・不明」…白 師匠にあたる人物のノードの縁は赤色")
st.image("pic/network.png")


st.write('■調査済句集一覧')

@st.cache
def load_data_kusyu():
    df_kusyu = pd.read_csv("data/kusyu.csv", usecols=["資料名", "年代", "内容", "備考", "所蔵", "チェック"])
    return df_kusyu
df_kusyu = load_data_kusyu()    
st.dataframe(df_kusyu)

