#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install streamlit


# In[2]:


import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st


# In[3]:


df1 = pd.read_pickle("data/taishi.pkl")
df2 = pd.read_pickle("data/bb.pkl")


# In[20]:


markdown = """
### プロ野球選手の年俸のヒストグラム
2020年のプロ野球選手の年俸からヒストグラムを作成しました
"""
st.write(markdown)


# In[5]:


df2 = df2[df2["年俸"]!="#VALUE!"]
df2 = df2.reset_index(drop=True)


# In[6]:


df2["年俸"] = df2["年俸"].apply(lambda x:x.replace(",",""))


# In[7]:


df2["年俸"] = df2["年俸"].astype('int')


# In[8]:


df2["年俸"] = df2["年俸"].apply(lambda x: x/10000)


# In[9]:


bins = np.linspace(0, df2["年俸"].max(), 91)


# In[10]:


freq = df2["年俸"].value_counts(bins=bins, sort=False)


# In[12]:


class_value = (bins[:-1] + bins[1:]) / 2  # 階級値
rel_freq = freq / df2["年俸"].count()  # 相対度数
cum_freq = freq.cumsum()  # 累積度数
rel_cum_freq = rel_freq.cumsum()  # 相対累積度数


# In[13]:


pd.set_option('display.max_rows', 101)


# In[1]:


dist = pd.DataFrame(
    {
        "階級値(万円)": class_value,
        "度数(人数)": freq,
        "相対度数": rel_freq,
        "累積度数": cum_freq,
        "相対累積度数": rel_cum_freq,
    },
    index=freq.index
)
st.dataframe(dist)


# In[21]:


fig, ax1 = plt.subplots(figsize=(30, 10))
dist.plot.bar(x="階級値(万円)", y="度数(人数)", ax=ax1, width=1, ec="k", lw=2)

ax2 = ax1.twinx()
ax2.plot(np.arange(len(dist)), dist["相対累積度数"], "--o", color="k")
ax2.set_ylabel("累積相対度数")
ax2.legend()
st.pyplot(fig)


# ## ローレンツ曲線

# In[16]:


df2["年俸"].mean()


# In[17]:


df2["年俸"].mode()


# ## 共分散

# In[18]:


df1.cov()

