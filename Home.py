import streamlit as st
import pandas as pd
from streamlit_card import card

card(
 title="Hello World!",
 text="Some description",
 url="https://github.com/gamcoh/st-card"
)
    
# st.set_page_config(page_title="東烏", page_icon="pic/karasu.jpg", layout="wide", initial_sidebar_state="auto", menu_items=None)

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

st.subheader("検索条件を入力してください")
haijin_input = st.text_input("俳名または本名・別名")
location_input = st.text_input("出身地")
job_input = st.text_input("職業")

if haijin_input or location_input or job_input:
    conditions = (df_haijin['俳名'].str.contains(haijin_input) | df_haijin['本名/別名'].str.contains(haijin_input)) &(df_haijin['出身地'].str.contains(location_input)) &(df_haijin['職業_詳細'].str.contains(job_input))
# st.subheader("「俳名」か「本名・別名」を入力してください。")
# haijin_input = st.text_input("検索キーワード入力欄")
    df_selected = df_haijin[conditions]
    st.write(f"{len(df_selected)}件の検索結果がありました。")
    st.dataframe(df_selected)
#     for index, person in df_selected.iterrows():
       
#         st.write(person["俳名"], card=True)
#         st.write("本名/別名: " + person["本名/別名"])
#         st.write("出身地: " + person["出身地"])
#         st.write("職業: " + person["職業_詳細"])
#         st.write("")
else:
    st.write("条件を入力してください")

# if not haijin_input:
#   st.write("何か単語を入力してください。")
# else:
#   df_selected = df_haijin[(df_haijin['俳名'].str.contains(haijin_input)) | (df_haijin['本名/別名'].str.contains(haijin_input))]
#   st.write(f"{len(df_selected)}件の検索結果がありました。")
#   st.dataframe(df_selected)

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
