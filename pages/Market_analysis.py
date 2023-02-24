import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import re
from pandasql import sqldf
from matplotlib import pyplot as plt
import plotly.figure_factory as ff



df_visualize = pd.read_csv("data/df_visualize.csv", encoding= 'unicode_escape').apply(lambda x: x.astype(str).str.lower())

type_dict = {'gaming laptop': 1,
 'thin and light laptop': 2,
 '2 in 1 laptop': 3,
 'notebook': 4,
 'laptop': 5,
 '2 in 1 gaming laptop': 6,
 'business laptop': 7,
 'chromebook': 8,
 'creator laptop': 9}

company_dict = {'asus': 1,
 'hp': 2,
 'lenovo': 3,
 'dell': 4,
 'msi': 5,
 'realme': 6,
 'avita': 7,
 'acer': 8,
 'samsung': 9,
 'infinix': 10,
 'lg': 11,
 'apple': 12,
 'nokia': 13,
 'redmibook': 14,
 'mi': 15,
 'vaio': 16}

gpu_brand_dict = {'nvidia': 1, 'none': 2, 'amd': 3, 'qualcomm': 4}

gpu_dict = {'nvidia geforce rtx 3070 ti': 1,
 'nvidia geforce rtx 3050': 2,
 'intel hd': 3,
 'iris xe': 4,
 'amd radeon': 5,
 'nvidia geforce gtx 1650': 6,
 'intel uhd': 7,
 'intel iris xe': 8,
 'nvidia geforce rtx 3070': 9,
 'nvidia geforce rtx 3050 ti': 10,
 'amd radeon vega 8': 11,
 'nvidia geforce rtx 3060': 12,
 'nvidia geforce mx 450': 13,
 'intel uhd 600': 14,
 'amd radeon rx vega 10': 15,
 'qualcomm adreno 618 gpu': 16,
 'amd radeon vega ': 17,
 'amd radeon rx 6600m': 18,
 'qualcomm adreno': 19,
 'nvidia geforce rtx 3050ti': 20,
 'nvidia geforce rtx 3080 ti': 21,
 'intel iris plus': 22,
 'nvidia geforce gtx': 23,
 'intel uhd 605': 24,
 'nvidia geforce rtx': 25,
 'intel iris': 26,
 'nvidia geforce mx 350': 27,
 'nvidia geforce mx 330': 28,
 'amd radeon rx 6700m': 29,
 'nvidia geforce': 30,
 'nvidia geforce gtx 1650 ti': 31,
 'm1': 32,
 'amd radeon vega': 33,
 'intel hd 520': 34,
 'amd radeon rx6600m': 35,
 'amd radeon rx 6800m': 36,
 'amd radeon 5500u': 37,
 'amd radeon 5500m': 38,
 'nvidia geforce mx 130': 39,
 'amd radeon r4': 40,
 'mediatek': 41,
 'intel hd 500': 42,
 'amd radeon r5': 43,
 'amd radeon r4 (stoney ridge)': 44,
 'nvidia geforce gtx 1650 max q': 45,
 'nvidia geforce mx 250': 46,
 'nvidia geforce gtx 1660 ti': 47,
 'nvidia geforce rtx 2060': 48,
 'intel uhd 620': 49,
 'intel hd 5500': 50,
 'nvidia geforce rtx 2080 super max-q': 51,
 'amd radeon vega 6': 52,
 'intel iris xe max': 53,
 'nvidia geforce gtx 1650 ti max-q': 54,
 'amd radeon 520': 55,
 'nvidia geforce rtx 2070 max-q': 56,
 'nvidia geforce gtx mx 330': 57,
 'nvidia geforce mx 230': 58,
 'intel hd 620': 59,
 'nvidia quadro p520': 60,
 'nvidia quadro t2000': 61,
 'nvidia geforce mx 110': 62}

processor_name_dict = {'core i9': 1,
 'ryzen 7 octa core': 2,
 'core i5': 3,
 'core i7': 4,
 'celeron dual core': 5,
 'pentium silver': 6,
 'athlon dual core': 7,
 'ryzen 7 dual core': 8,
 'ryzen 3 quad core': 9,
 'ryzen 9 octa core': 10,
 'core i3': 11,
 'ryzen 5 hexa core': 12,
 'ryzen 5 quad core': 13,
 'ryzen 7 hexa core': 14,
 'ryzen 7 quad core': 15,
 'pentium quad core': 16,
 'celeron quad core': 17,
 'snapdragon 7c gen 2': 18,
 'ryzen 5 dual core': 19,
 'ryzen 3 dual core': 20,
 'dual core': 21,
 'ryzen 5 octa core': 22,
 'm1 pro': 23,
 'ryzen 3 hexa core': 24,
 'apu dual core a6': 25,
 'mediatek kompanio 500': 26,
 'm1': 27,
 'apu dual core a9': 28,
 'hexa core i5': 29,
 'octa core i7': 30}

processor_brand_dict = {'intel': 1, 'amd': 2, 'qualcomm': 3, 'apple': 4, 'mediatek': 5}

os_dict = {'windows': 1, 'chrome': 2, 'dos': 3, 'mac': 4, 'ubuntu': 5}

inv_type_dict = {v: k for k, v in type_dict.items()}
inv_company_dict = {v: k for k, v in company_dict.items()}
inv_gpu_brand_dict = {v: k for k, v in gpu_brand_dict.items()}
inv_processor_brand_dict = {v: k for k, v in processor_brand_dict.items()}
inv_processor_name_dict = {v: k for k, v in processor_name_dict.items()}
inv_os_dict = {v: k for k, v in os_dict.items()}
inv_gpu_dict = {v: k for k, v in gpu_dict.items()}

# def funcc1(s):
#     return inv_type_dict[s]

# df_visualize["Type"] = df_visualize["Type"].apply(funcc1)

# def funcc2(s):
#     return inv_company_dict[s]

# df_visualize["company"] = df_visualize["company"].apply(funcc2)

# def funcc3(s):
#     return inv_gpu_brand_dict[s]
# df_visualize["gpu_brand"] = df_visualize["gpu_brand"].apply(funcc3)

# def funcc4(s):
#     return inv_processor_brand_dict[s]
# df_visualize["Processor Brand"] = df_visualize["Processor Brand"].apply(funcc4)

# def funcc5(s):
#     return inv_processor_name_dict[s]
# df_visualize["Processor Name"] = df_visualize["Processor Name"].apply(funcc5)

# def funcc6(s):
#     return inv_os_dict[s]
# df_visualize["Operating System"] = df_visualize["Operating System"].apply(funcc6)

# def funcc7(s):
#     return inv_gpu_dict[s]
# df_visualize["gpu_processor"] = df_visualize["gpu_processor"].apply(funcc7)


fig = plt.figure(figsize = (15,5))
sns.boxplot(x = df_visualize["company"], y = df_visualize["Price"])
plt.title("Price variation of the comapanies")

st.pyplot(fig)


