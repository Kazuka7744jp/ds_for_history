#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st


# In[8]:


df1 = pd.read_pickle("data/taishi.pkl")
df2 = pd.read_pickle("data/bb.pkl")


# ## ４．ヒストグラム・ローレンツ曲線

# ## プロ野球選手の年俸のヒストグラム

# In[10]:


# https://pystyle.info/statistics-frequency-table-and-histogram/
fig = plt.figure(figsize=(30,10))
plt.title("プロ野球選手の年俸")
plt.xlabel("年収")
plt.ylabel("人数")
plt.hist(df2["年俸"],alpha=0.5, bins=50)
plt.show()


# In[11]:


df2 = df2[df2["年俸"]!="#VALUE!"]
df2 = df2.reset_index(drop=True)


# In[12]:


df2["年俸"] = df2["年俸"].apply(lambda x:x.replace(",",""))


# In[13]:


df2["年俸"] = df2["年俸"].astype('int')


# In[14]:


df2["年俸"] = df2["年俸"].apply(lambda x: x/10000)


# In[15]:


bins = np.linspace(0, df2["年俸"].max(), 91)
print(bins)


# In[16]:


freq = df2["年俸"].value_counts(bins=bins, sort=False)
freq


# In[17]:


bins[1:]


# In[18]:


class_value = (bins[:-1] + bins[1:]) / 2  # 階級値
rel_freq = freq / df2["年俸"].count()  # 相対度数
cum_freq = freq.cumsum()  # 累積度数
rel_cum_freq = rel_freq.cumsum()  # 相対累積度数


# In[19]:


pd.set_option('display.max_rows', 101)


# In[20]:


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
dist


# In[21]:


fig, ax1 = plt.subplots(figsize=(30, 10))
dist.plot.bar(x="階級値(万円)", y="度数(人数)", ax=ax1, width=1, ec="k", lw=2)

ax2 = ax1.twinx()
ax2.plot(np.arange(len(dist)), dist["相対累積度数"], "--o", color="k")
ax2.set_ylabel("累積相対度数")
ax2.legend()


# ## ローレンツ曲線

# In[24]:


df2["年俸"].mean()


# In[25]:


df2["年俸"].mode()


# ## 共分散

# In[37]:


df1.cov()

