import pandas as pd
import numpy as np

import webbrowser
import json
from urllib.request import urlopen

from IPython.display import HTML, IFrame, Image, display, display_html
from pandas.tseries.offsets import YearEnd, QuarterEnd, MonthEnd, YearBegin, QuarterBegin, MonthBegin

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties

import platform

idx = pd.IndexSlice

# matplotlib 한글 폰트 지정
if platform.system() == 'Darwin':
    flocation = "//Library//Fonts//NanumGothic.otf" # 맥
else:
    flocation = "C://Windows//Fonts//malgun.ttf" # 윈도우

fname = FontProperties(fname=flocation).get_name()
matplotlib.rc('font', family=fname)


# 금융안정보고서 스타일 그래프 색 지정(RGB)
lcolors = [(85/256, 142/256, 213/256), (110/256, 110/256, 110/256), 
           (175/256, 175/256, 105/256), (250/256, 192/256, 145/256), 
           (150/256, 115/256, 170/256)]

bcolors =  [(185/256, 214/256, 245/256), (191/256, 191/256, 191/256), 
            (190/256, 205/256, 150/256), (250/256, 220/256, 190/256), 
            (203/256, 185/256, 213/256)]

dcolors = lcolors + ['brown', 'orange', 'green', 'purple', 'pink', 'red', 'cyan', 'olive', 'blue']


def set_titles(ax, titles, fontsize=18, y=1.03):
    try:
        [axe.set_title(titles[i], fontsize=fontsize, y=y) for i, axe in enumerate(ax.ravel())]
    except:
        ax.set_title(titles, fontsize=fontsize, y=y)


def yaxis_format(ax, i = 1):
    string = '{:,.' + str(i) + 'f}'
    try:
        [a.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: string.format(x))) for a in ax.ravel()]
    except:
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: string.format(x)))


def xaxis_format(ax, i = 1):
    string = '{:,.' + str(i) + 'f}'
    try:
        [a.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: string.format(x))) for a in ax.ravel()]
    except:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: string.format(x)))


def get_ticklabels(index, i, fmt='%Y'):
    # fmt = '%y', '%Q\n%Y', ...
    ticklabels = [''] * len(index)
    ticklabels[::i] = [item.strftime(fmt) for item in index[::i]]
    return ticklabels