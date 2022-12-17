#!/usr/bin/env python
# coding: utf-8

# import japanize_matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import patches
# import numpy as np
import pandas as pd
# from scipy import stats
# import seaborn as sns
import streamlit as st

df = pd.read_csv("data/taishi.csv")

pagelist = ["0.はじめに", "01.賤ケ岳7本槍（散布図）", "02.猪武者（相関係数）", "03.領土保全と野心（連関係数）"]
st.header("信長の野望データセットのページ")

#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択", pagelist)
if selector==pagelist[0]:
    st.header(selector)
    st.write("このページは、信長の野望「大志」のデータセットに基づき、データの可視化を練習するページです。")
    st.write('''
        練習結果をご覧になる場合は、**左側のサイドバーの「ページ選択」よりプルダウンで選択**をお願いいたします。
        ''')

elif selector==pagelist[1]:
    st.header("「賤ケ岳の7本槍」の能力比較（散布図）")

#     sevens = ["加藤清正", "福島正則", "加藤嘉明", "平野長泰",  "脇坂安治", "糟屋武則", "片桐且元"]

#     #csvから該当する武将のインデックスのリストをつくるための関数
#     def busho_finder(df, list):
#         index_list=[]
#         for idx1, name in enumerate(list):
#             for idx2, row in df.iterrows():
#                 if (row["武将姓"] + row["武将名"]) == name:
#                     index_list.append(idx2)
#         return index_list


#     df = df.iloc[busho_finder(df, sevens)]
    df = pd.read_csv("data/7.csv")
    st.write("■7本槍の能力データ")
    st.dataframe(df)

#     fig, ax = plt.subplots()
#     ax.scatter("戦闘", "政治", s=100, alpha=0.4, data=df)
#     plt.figure(figsize=(10,10))
#     plt.rcParams["font.size"] = 8
#     ax.set_title("賤ヶ岳7本槍の能力値　散布図")
#     ax.set_xlabel("戦闘能力値　合計")
#     ax.set_ylabel("政治能力値　合計")

#     for i, name in enumerate(df["武将姓"]):
#         if name == "加藤":
#             ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], df["武将姓"].iloc[i]+df["武将名"].iloc[i][:1])
#         else:
#             ax.text(df["戦闘"].iloc[i], df["政治"].iloc[i], name)

#     # 2グループを円で囲む
#     circle1 = patches.Circle(xy=(165, 120), radius=25, alpha=0.1)
#     circle2 = patches.Circle(xy=(117, 92), radius=21, alpha=0.1)
#     ax.add_patch(circle1)
#     ax.add_patch(circle2)
                            
    st.write("■戦闘・政治能力に基づく散布図")
#     st.pyplot(fig)
    st.image("pic/7spear.png")

    st.write("■所感")
    st.write("加藤清正・福島正則・加藤嘉明とそれ以外で群が分かれた格好となった。加藤嘉明は、他の二人や片桐に比べ知名度は低いが、\
            秀吉に見いだされ数々の武功を挙げ、秀吉子飼いでありながら、大阪夏の陣も乗り越えた武将。松山城築城でも知られる。")

    st.write("■コード")
    st.code(
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
    )

elif selector==pagelist[2]:
    st.header("猪武者ほどすぐに死ぬ（相関係数）")
    st.write("武勇が高いが、知略が低い武将は、討ち死になどが要因で、寿命が短めなのではないかと思い\
    相関係数を見てみることにした")

    clm1 = "知略"
    clm2 = "武勇"
    clm1_param = 0.25
    clm2_param = 0.5
    df_inoshishi = pd.read_csv("data/df_inoshishi.csv")

#     df_inoshishi = df[(df[clm1] < df[clm1].quantile(q=clm1_param)) & (df[clm2] > df[clm2].quantile(q=clm2_param))]

    st.write("選抜条件は、知略の能力値が、下位25%、かつ、武勇の能力値が上位50％の武将。\
    その結果、全武将2161人の中から、198人の猪武者たちが選抜された。")
    st.write("■選ばれし、猪武者たち")
    st.write(df_inoshishi)
    df_daihyo = df_inoshishi[df_inoshishi["知略"] == df["知略"].min()]
    st.write("■最も「知略」が低い武将")
    st.write(df_daihyo)
    dname = df_daihyo["武将姓"].iloc[0] + df_daihyo["武将名"].iloc[0]
    st.write(f"最も知略の低い（知略20）{dname}は、齢は56歳の時であるものの、実際に天正十年、河合戦で討死している。これは期待（？）ができる。")
    st.write("ちなみに猪武者たちの知略、武勇のヒストグラムは以下のような感じ。歪んだ分布になっている。")

#     fig, (ax1, ax2) = plt.subplots(1, 2)
#     fig.set_size_inches(10, 5)
#     ax1.hist(df_inoshishi[clm1])
#     ax1.set_title(f'「{clm1}」に関するヒストグラム')
#     ax1.set_xlabel(clm1)
#     ax1.set_ylabel("人数")
#     ax2.hist(df_inoshishi[clm2])
#     ax2.set_title(f'「{clm2}」に関するヒストグラム')
#     ax2.set_xlabel(clm2)
#     ax2.set_ylabel("人数")
#     st.write(fig)
    st.image("pic/inoshishi.png")

    st.write("では、知略と武勇の相関係数を求めてみる。仮説は、「知略が低い場合、武勇が高ければ高いほど、\
    自分の力を過信し、命を落としている結果、寿命が短くなる傾向がある」だ。")

#     r = np.corrcoef(df_inoshishi["知略"], df_inoshishi["寿命"])[0, 1]

#     st.subheader(f"相関係数は「{r:.3f}」という結果で、相関は全くなかった。")
    st.subheader(f"相関係数は「0.079」という結果で、相関は全くなかった。")
    

    st.write(f"一応、猪武者たちのすべての能力値の相関を見てみる。")

#     fig, ax = plt.subplots()
#     fig.set_size_inches(8, 5)
#     sns.heatmap(df_inoshishi[["統率", "武勇", "知略", "内政", "外政","寿命", "野心"]].corr(), ax=ax, cmap="coolwarm", annot=True)
    st.image("pic/inoshishi_heatmap.png")
#     st.write(fig)

#     lifespan_all = int(df["寿命"].mean())
#     lifespan_inoshishi = int(df_inoshishi["寿命"].mean())

    st.write("ちなみに、全武将の平均寿命が「57才」に対して、猪武者たちの平均寿命は、「54才」だった。やはり若干早めに亡くなっている。")
    st.write("■コード")
    st.code(
    """
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import streamlit as st
    
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
    )

elif selector==pagelist[3]:
    st.header("「領土保全」ばかり考えている武将に野心はない（連関係数）")
    import numpy as np
    from scipy import stats
    import pandas as pd
    import seaborn as sns
    import streamlit as st

    st.write("信長の野望「大志」には、武将ごとに志という設定があるが、その中で最も多いのが「領地保全」である。\
        領地保全という言葉には、自分の土地に安寧するイメージがあり、天下統一などの「野心」を持たない武将が多いのではと考え、\
            連続データの「野心」をカテゴリ変数に置き換えたうえで、クラメールの連関係数を見てみることにした。")

    st.write("ヒストグラムはこんな感じ。")
    fig, ax = plt.subplots()
    ax.hist(df["野心"])
    ax.set_title(f'「野心に関するヒストグラム')
    ax.set_xlabel("野心")
    ax.set_ylabel("人数")
    st.write(fig)
    
    ambition_ave = df["野心"].mean()
    st.write(f"なお、全武将の野心の平均は{ambition_ave:.2f}であり、平均より上か下かで、それぞれの武将を「野心あり」「野心なし」のカテゴリ変数で分けることにした。")

    # 志が領地保全かどうかの列を追加
    df["志_領地保全"] = df["志"].apply(lambda x: "領地保全" if x=="領地保全" else "領地保全以外")

    # 野心が平均以上かどうかの列を追加
    df["野心有無"] = df["野心"].apply(lambda x: "野心あり" if x >= ambition_ave else "野心なし")

    cont_table = pd.crosstab(df["野心有無"],df["志_領地保全"])
    st.write("■分割表")
    st.write(cont_table)

    expected_table = pd.DataFrame(stats.chi2_contingency(cont_table, correction=False)[3], index=cont_table.index, columns=cont_table.columns).round(0)
    st.write("■期待度数の分割表")
    st.write(expected_table)
    st.subheader("あ、これ連関ないな・・・")
    
    # クラメールの連関係数
    def cramers_v(x, y):
        cont_table = pd.crosstab(x, y)
        chi2 = stats.chi2_contingency(cont_table, correction=False)[0]
        min_d = min(cont_table.shape) - 1
        n = len(x)
        v = np.sqrt(chi2/(min_d*n))
        return v


    cram = cramers_v(df["野心有無"], df["志_領地保全"]).round(4)
    st.write(f"ちなみに、見るまでもなかったのですが、クラメールの連関係数は{cram}でした。")

    df_hozen = df[df["志_領地保全"]=="領地保全"]
    df_not_hozen = df[df["志_領地保全"]=="領地保全以外"]

    std_table = pd.DataFrame([df["野心"].std(), df_hozen["野心"].std(), df_not_hozen["野心"].std()], index=["全体", "志_領地保全", "志_それ以外"], columns=["標準偏差",]).T.round(2)
    st.write("いちおう、ばらつきも見てみる。")
    st.write("■「野心」の能力値の標準偏差")
    st.write(std_table)

    st.write("「領土を保全する」という野心が、みんなあるんですね。")
    amb_max = df_hozen["野心"].max()

    df_daihyo_amb = df_hozen[df_hozen["野心"] == amb_max]
    
    st.write(f"ちなみに「領土保全」で最も野心が高い武将は以下の方々です。(野心の値は{amb_max})。失礼いたしました。")
    st.write(df_daihyo_amb)
    
    st.write("一番上の温井総貞に至っては、能登の国人で、現在の輪島を領しながら、畠山義総・義続・義綱3代にわたり仕え、\
    義総からは「総」の字もらい、筆頭重臣。義続・義綱の時代で専横に振る舞い、畠山七人衆の筆頭。遊佐氏の当主・遊佐続光を蹴落とし、権力をほしいまま。\
    最後は義綱たちに暗殺されるという、保全している領土内で、野心爆発という感じですね。")
 
    st.write("■コード")
    st.code(
    """
    import numpy as np
    from scipy import stats
    import pandas as pd
    import seaborn as sns
    import streamlit as st

    df = pd.read_csv("taishi.csv")

    ambition_ave = df["野心"].mean()

    fig, ax = plt.subplots()
    ax.hist(df["野心"])
    ax.set_title(f'「野心に関するヒストグラム')
    ax.set_xlabel("野心")
    ax.set_ylabel("人数")
    st.write(fig)

    # 志が領地保全かどうかの列を追加
    df["志_領地保全"] = df["志"].apply(lambda x: "領地保全" if x=="領地保全" else "領地保全以外")

    # 野心が平均以上かどうかの列を追加
    df["野心有無"] = df["野心"].apply(lambda x: "野心あり" if x >= ambition_ave else "野心なし")

    cont_table = pd.crosstab(df["野心有無"],df["志_領地保全"])
    st.write(cont_table)

    expected_table = pd.DataFrame(stats.chi2_contingency(cont_table, correction=False)[3], index=cont_table.index, columns=cont_table.columns).round(0)
    st.write(expected_table)
    
    # クラメールの連関係数
    def cramers_v(x, y):
        cont_table = pd.crosstab(x, y)
        chi2 = stats.chi2_contingency(cont_table, correction=False)[0]
        min_d = min(cont_table.shape) - 1
        n = len(x)
        v = np.sqrt(chi2/(min_d*n))
        return v


    cram = cramers_v(df["野心有無"], df["志_領地保全"]).round(4)

    df_hozen = df[df["志_領地保全"]=="領地保全"]
    df_not_hozen = df[df["志_領地保全"]=="領地保全以外"]

    std_table = pd.DataFrame([df["野心"].std(), df_hozen["野心"].std(), df_not_hozen["野心"].std()], index=["全体", "志_領地保全", "志_それ以外"], columns=["標準偏差",]).T.round(2)
    st.write(std_table)

    df_daihyo_amb = df_hozen[df_hozen["野心"] == df_hozen["野心"].max()]
    st.write(df_daihyo_amb)
    """)

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



