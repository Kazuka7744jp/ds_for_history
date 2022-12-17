#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("data/nenpyo.csv")

st.title("東烏に関する調査ページ")

# st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["はじめに", "01.プロローグ", "残された点帖", "三河俳人検索DB"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector=="はじめに":
  st.header("はじめに")
  st.write("このページは、愛知県刈谷市の東海道沿いの家に残された古文書などに基づく、先祖の在りし日の姿の調査記録になります。")
  st.write('''
        調査記録をご覧になる場合は、**左側のサイドバーの「ページ選択」よりプルダウンで選択**をお願いいたします。
        ''')
  st.subheader("調査者")
  st.image("pic/kiyomasa2.jpg")
  st.write("「さとる部長」 －某研究所歴史アーカイブ同好会部長。独学でくずし字を読むすごい人")
  st.image("pic/ryujiemon2.jpg")
  st.write("「りゅうじえもん」 －久右衛門の子孫。当サイト管理人。データ可視化担当")
#   st.scroll(0, 0)
  st.markdown(
  """
  <script>
    window.scrollTo(0, 0);
  </script>
  """,
  unsafe_allow_html=True,
  )

#   st.write("■加塚家年表（随時更新中）")
#   st.table(df)

elif selector=="01.プロローグ":
  st.header(selector)
  st.write("さとる部長は、りゅうじえもんから送られてきた大量の画像に目を通していた。以前、りゅうじえもんの家にある古文書を翻刻した縁で、\
  りゅうじえもんとはその後もやりとりが続いていた。")
  st.write("それは、ざっと見る限り、かなりくせのある崩し字で書かれた100ページ以上の日記で、芭蕉などの著名な俳人のことや\
  自作の俳句などが書かれているようだった。")
  st.write("りゅうじえもんによると、以前、りゅうじえもんの家の古文書目録作成のために市が調査した際は、「雑記録（メモ帳）」と位置づけられたとのことだ。\
  日記の中に、「東烏」という俳号が頻出するため、おそらくこれが日記の書き手の俳号だと推測された。")
  st.write("（しかし、この大量のくせ字を読み解くのは、少々難儀だな…。）")
  st.write("そう思いながら、画像の最後の方まで見たさとる部長の目に、一つの文章が飛び込んできた。")
  st.image("pic/wakamegomo.jpg")
  st.subheader("「和歌芽籠　完　草稿」")
  st.write("（そうか！東烏はこの本を和歌の本として、世に出したかったのだ。）")
  st.write("「これは雑記帳ではない。読んでくれ。」")
  st.write("東烏がそう自分に語りかけてくる気がした。")
  st.write("気が付くと、さとる部長は、一心不乱に翻刻作業に取り掛かっていた。")

elif selector=="残された点帖":
  st.header("残された点帖")
  st.write('当初、これが一体なんなのかが皆目見当がつかなかったため、さとる部長と専門の先生にご相談した結果、句会の「点帖」であることが分かった。')
  st.write('点帖とは句会の記録であり、「執筆」が書いたものを「点者」「宗匠」が批点・押印、最終的には、秀逸の者の褒美として贈られるものである。')
  
  st.write('家にこの点帖が残されていたということは、この句会で入選した俳号「玄」が当家にまつわる人間である可能性が高まった。東烏に加え、「玄」も調査対象に加わることとなった。\
  玄は俳号を省略したものであり、さとる部長に聞くところによると、俳号は「〇玄」である可能性が高いようだ。')
 
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

elif selector=="三河俳人検索DB":
  st.header("三河俳人検索データベース")
  df_haijin = pd.read_csv("data/data_haijin.csv", keep_default_na=False)
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
  col1, col2 = st.columns(2)
  col1.metric("登録人数", df_len)
  col2.metric("調査済句集", len(df_haijin.columns)-9)
  col3, col4 = st.columns(2)
  col3.metric("本名判明率", "{:.1%}".format((df_haijin["本名/別名"]!="").sum()/df_len))
  col4.metric("職業判明率", "{:.1%}".format((df_haijin["職業_詳細"]!="").sum()/df_len))
  st.write(df_haijin)
  
  st.write('■職業別の人数')
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
  
  st.write("■門下別の職業内訳")
  
  @st.cache
  def monka_job_pie(df, group_clm, pie_clm):
    df = df[df[pie_clm]!=""]
    df = df.groupby(group_clm)
    master_list = list(df.groups.keys())[1:-1]
    clms = 2
    rows = len(master_list)//2 + len(master_list)%2
    master_num = len(master_list)
    fig, axes = plt.subplots(rows, clms, figsize=(20,20), tight_layout=True)
    idx = 0
    for master in master_list:
        df_temp = pd.DataFrame(df.get_group(master)[pie_clm].value_counts(dropna=True))
        df_num = len(df.get_group(master))
        axes[idx//2,idx%2].set_title(f"{master}の門下生の職業（n={df_num}）")
        axes[idx//2,idx%2].pie(df_temp.values.flatten(), labels=df_temp.index, autopct='%1.1f%%')
        idx += 1
    plt.show()
    st.write(fig)
    
  monka_job_pie(df_haijin, "門下", "職業")
   
  st.write('■出身別人数')
  df_birth_place = df_haijin[df_haijin["出身地"] != ""]
  df_birth_place = df_birth_place["出身地"].value_counts(ascending=False)
  st.bar_chart(df_birth_place)
  
  st.write('■句集登場回数')
  kusyu_counts = df_haijin["句集登場回数"].value_counts()
  st.bar_chart(kusyu_counts)
