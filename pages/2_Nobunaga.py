#!/usr/bin/env python
# coding: utf-8

import japanize_matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

df = pd.read_csv("data/taishi.csv")

pagelist = ["はじめに", "賤ケ岳7本槍（散布図）", "猪武者（相関係数）"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector==pagelist[0]:
    st.header(selector)
    st.write("このページは、信長の野望「大志」のデータベースに基づき、データの可視化を練習するページです。")
    st.write('''
        練習結果をご覧になる場合は、**左側のサイドバーの「ページ選択」よりプルダウンで選択**をお願いいたします。
        ''')

elif selector==pagelist[1]:
    st.header("「賤ケ岳の7本槍」の能力比較（散布図）")


    sevens = ["加藤清正", "福島正則", "加藤嘉明", "平野長泰",  "脇坂安治", "糟屋武則", "片桐且元"]

    #csvから該当する武将のインデックスのリストをつくるための関数
    @st.cache
    def busho_finder(df, list):
        index_list=[]
        for idx1, name in enumerate(list):
            for idx2, row in df.iterrows():
                if (row["武将姓"] + row["武将名"]) == name:
                    index_list.append(idx2)
        return index_list


    df = df.iloc[busho_finder(df, sevens)]
    st.write("■7本槍の能力データ")
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.scatter("戦闘", "政治", s=100, alpha=0.4, data=df)
    plt.figure(figsize=(10,10))
    plt.rcParams["font.size"] = 8
    ax.set_title("賤ヶ岳7本槍の能力値　散布図")
    ax.set_xlabel("戦闘能力値　合計")
    ax.set_ylabel("政治能力値　合計")

    for i, name in enumerate(df["武将姓"]):
        if name == "加藤":
            ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], df["武将姓"].iloc[i]+df["武将名"].iloc[i][:1])
        else:
            ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], name)

    # 2グループを円で囲む
    circle1 = patches.Circle(xy=(165, 120), radius=25, alpha=0.1)
    circle2 = patches.Circle(xy=(117, 92), radius=21, alpha=0.1)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
                            
    st.write("■戦闘・政治能力に基づく散布図")
    st.pyplot(fig)

    st.write("■所感")
    st.write("加藤清正・福島正則・加藤嘉明とそれ以外で群が分かれた格好となった。加藤嘉明は、他の二人や片桐に比べ知名度は低いが、\
            秀吉に見いだされ数々の武功を挙げ、秀吉子飼いでありながら、大阪夏の陣も乗り越えた武将。松山城築城でも知られる。")

    st.write("■コード")
    """
    ```python
    import japanize_matplotlib
    import matplotlib.pyplot as plt
    from matplotlib import patches
    import numpy as np
    import pandas as pd
    import streamlit as st

    df = pd.read_csv("data/taishi.csv")
    sevens = ["加藤清正", "福島正則", "加藤嘉明", "平野長泰",  "脇坂安治", "糟屋武則", "片桐且元"]

    #csvから該当する武将のインデックスのリストをつくるための関数
    @st.cache
    def busho_finder(df, list):
        index_list=[]
        for idx1, name in enumerate(list):
            for idx2, row in df.iterrows():
                if (row["武将姓"] + row["武将名"]) == name:
                    index_list.append(idx2)
        return index_list


    df = df.iloc[busho_finder(df, sevens)]
    st.write("■7本槍の能力データ")
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.scatter("戦闘", "政治", s=100, alpha=0.4, data=df)
    plt.figure(figsize=(10,10))
    plt.rcParams["font.size"] = 8
    ax.set_title("賤ヶ岳7本槍の能力値　散布図")
    ax.set_xlabel("戦闘能力値　合計")
    ax.set_ylabel("政治能力値　合計")

    for i, name in enumerate(df["武将姓"]):
        if name == "加藤":
            ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], df["武将姓"].iloc[i]+df["武将名"].iloc[i][:1])
        else:
            ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], name)

    # 2グループを円で囲む
    circle1 = patches.Circle(xy=(165, 120), radius=25, alpha=0.1)
    circle2 = patches.Circle(xy=(117, 92), radius=21, alpha=0.1)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
                            
    st.write("■戦闘・政治能力に基づく散布図")
    st.pyplot(fig)

    ```
    """
elif selector==pagelist[2]:
    st.header("猪武者ほどすぐに死ぬ（相関係数）")
    st.write("武勇が高いが、統率能力が平均以下の武将は、討ち死になどが要因で、寿命が短めなのではないかと思い\
    相関係数を見てみることにした")

    clm1 = "知略"
    clm2 = "武勇"
    clm1_param = 0.25
    clm2_param = 0.5

    df_inoshishi = df[(df[clm1] < df[clm1].quantile(q=clm1_param)) & (df[clm2] > df[clm2].quantile(q=clm2_param))]

    st.write(f"選抜条件は、{clm1}の能力値が、下位{int(clm1_param*100)}%、かつ、{clm2}の能力値が平均以上の武将。\
    その結果、全武将{len(df)}人の中から、{len(df_inoshishi)}人の猪武者たちが選抜された。")
    st.write("■選ばれし、猪武者たち")
    st.write(df_inoshishi)
    df_daihyo = df_inoshishi[df_inoshishi["知略"] == df["知略"].min()]
    st.write("■最も「知略」が低い武将")
    st.write(df_daihyo)
    dname = df_daihyo["武将姓"].iloc[0] + df_daihyo["武将名"].iloc[0]
    st.write(f"最も知略の低い（知略20）{dname}は、齢は56歳の時であるものの、実際に天正十年、河合戦で討死している。これは期待（？）ができる。")
    st.write(f"ちなみに猪武者たちの{clm1}、{clm2}のヒストグラムは以下のような感じ。歪んだ分布になっている。")

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(10, 5)
    ax1.hist(df_inoshishi[clm1])
    ax1.set_title(f'「{clm1}」に関するヒストグラム')
    ax1.set_xlabel(clm1)
    ax1.set_ylabel("人数")
    ax2.hist(df_inoshishi[clm2])
    ax2.set_title(f'「{clm2}」に関するヒストグラム')
    ax2.set_xlabel(clm2)
    ax2.set_ylabel("人数")
    st.write(fig)

    st.write(f"では、{clm1}と{clm2}の相関係数を求めてみる。仮説は、「知略が低い場合、武勇が高ければ高いほど、\
    自分の力を過信し、命を落としている結果、寿命が短くなる傾向がある」だ。")

    r = np.corrcoef(df_inoshishi["知略"], df_inoshishi["寿命"])[0, 1]

    st.subheader(f"相関係数は「{r:.3f}」という結果で、相関は全くなかった。")

    st.write(f"一応、猪武者たちのすべての能力値の相関を見てみる。")

    fig, ax = plt.subplots()
    fig.set_size_inches(8, 5)
    sns.heatmap(df_inoshishi[["統率", "武勇", "知略", "内政", "外政","寿命", "野心"]].corr(), ax=ax, cmap="coolwarm", annot=True)
    st.write(fig)

    lifespan_all = int(df["寿命"].mean())
    lifespan_inoshishi = int(df_inoshishi["寿命"].mean())

    st.write(f"ちなみに、全武将の平均寿命が「{lifespan_all}才」に対して、猪武者たちの平均寿命は、「{lifespan_inoshishi}才」だった。やはり若干早めに亡くなっている。")
    st.write("■コード")
    """
    ```python
    
    # パラメーターを指定
    clm1 = "知略" 
    clm2 = "武勇"
    clm1_param = 0.25
    clm2_param = 0.5
    
    # 猪武者だけのデータを抽出
    df_inoshishi = df[(df[clm1] < df[clm1].quantile(q=clm1_param)) & (df[clm2] > df[clm2].quantile(q=clm2_param))]
    st.write(df_inoshishi)
    
    # 最も知略が低い武将を抽出
    df_daihyo = df_inoshishi[df_inoshishi["知略"] == df["知略"].min()]
    st.write(df_daihyo)
    
　　# 武勇と知略に関するヒヒストグラムを作成 
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_size_inches(10, 5)
    ax1.hist(df_inoshishi[clm1])
    ax1.set_title(f'「{clm1}」に関するヒストグラム')
    ax1.set_xlabel(clm1)
    ax1.set_ylabel("人数")
    ax2.hist(df_inoshishi[clm2])
    ax2.set_title(f'「{clm2}」に関するヒストグラム')
    ax2.set_xlabel(clm2)
    ax2.set_ylabel("人数")
    st.write(fig)
    
    # 相関係数（R）
    r = np.corrcoef(df_inoshishi["知略"], df_inoshishi["寿命"])[0, 1]

    # ヒートマップで全相関係数を表示
    fig, ax = plt.subplots()
    fig.set_size_inches(8, 5)
    sns.heatmap(df_inoshishi[["統率", "武勇", "知略", "内政", "外政","寿命", "野心"]].corr(), ax=ax, cmap="coolwarm", annot=True)
    st.write(fig)

    ♯ 平均寿命を算出
    lifespan_all = int(df["寿命"].mean())
    lifespan_inoshishi = int(df_inoshishi["寿命"].mean())
    """
# import streamlit as st
# # from streamlit_folium import st_folium
# # import folium

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import patches
# import japanize_matplotlib

# https://welovepython.net/streamlit-folium/
# m = folium.Map(
#     # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
#     location=[35.02968298040031, 137.0168353420444], 
#     # タイル、アトリビュートの指定
#     tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
#     attr='都道府県庁所在地、人口、面積(2016年)',
#     # ズームを指定
#     zoom_start=13
# )
# st_data = st_folium(m, width=2000, height=1500)


# ページ設定
# st.set_page_config(
#     page_title="streamlit-foliumテスト",
#     page_icon="🗾",
#     layout="wide"
# )

# # 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
# m = folium.Map(
#     # 地図の中心位置の指定(今回は栃木県の県庁所在地を指定)
#     location=[36.56583, 139.88361], 
#     # タイル、アトリビュートの指定
#     tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
#     attr='都道府県庁所在地、人口、面積(2016年)',
#     # ズームを指定
#     zoom_start=6
# )

# # 表示するデータを読み込み
# df = pd.read_csv('pref.csv')

# # 読み込んだデータ(緯度・経度、ポップアップ用文字、アイコンを表示)
# for i, row in df.iterrows():
#     # ポップアップの作成(都道府県名＋都道府県庁所在地＋人口＋面積)
#     pop=f"{row['都道府県名']}({row['都道府県庁所在地']})<br>　人口…{row['人口']:,}人<br>　面積…{row['面積']:,}km2"
#     folium.Marker(
#         # 緯度と経度を指定
#         location=[row['緯度'], row['経度']],
#         # ツールチップの指定(都道府県名)
#         tooltip=row['都道府県名'],
#         # ポップアップの指定
#         popup=folium.Popup(pop, max_width=300),
#         # アイコンの指定(アイコン、色)
#         icon=folium.Icon(icon="home",icon_color="white", color="red")
#     ).add_to(m)

# st_data = st_folium(m, width=1200, height=800)



