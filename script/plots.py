import pandas as pd
import numpy as np
import statsmodels.api as sm


########################################################
#################### Preliminary #######################
########################################################

crises = [pd.to_datetime('1991-01-01'), pd.to_datetime('1997-10-01'), 
            pd.to_datetime('2002-10-01'), pd.to_datetime('2008-07-01')]
fc_peaks = [pd.to_datetime('1991-01-01'), pd.to_datetime('1998-01-01'), 
            pd.to_datetime('2003-01-01'), pd.to_datetime('2009-01-01')]


rec = pd.read_csv('python2021/input/recessions.csv', header=0, index_col=0)
rec.index = pd.to_datetime(rec.index)
rec = rec.resample('QS').first()


########################################################
#################### Function definition ###############
########################################################

for i in rec.index:
    if rec.loc[i, 'rec'] == 1:
        rec.loc[i, 'cat'] = 'r' + rec.loc[i, 'lab'].astype(str)
    else:
        rec.loc[i, 'cat'] = 'e' + rec.loc[i, 'lab'].astype(str)


def bp_cycle(df, p0, p1, normalization=True):
    '''Returns: cycle, which is normalized by default'''
    cycles = df.copy()
    for co in df.columns:
        cycle, trend = sm.tsa.filters.cffilter(df.loc[:, co].dropna(), low = p0, high = p1, drift=True)
        if normalization == True:
            cycle = cycle / cycle.std()
        cycles.loc[:, co] = cycle
    return cycles


def hp_cycle(df, lam): 
    cycle, trend = sm.tsa.filters.hpfilter(df.dropna(), lam)
    return cycle


def one_sided_hpfilter(ts, lam):
    trend = ts.copy()
    for i in ts.index:
        if ts.loc[:i].shape[0] > 2:
            cy, tr = sm.tsa.filters.hpfilter(ts.loc[:i], lam)
            trend.loc[i] = tr.loc[i]
    trend.iloc[0:2] = ts.iloc[0:2]
    cycle = ts - trend
    return cycle, trend


def plot_crisis(ax, periods):
    try:
        for axe in ax.ravel():
            for xc in fc_peaks:
                if  pd.Timestamp(periods[0]) <= xc <= pd.Timestamp(periods[-1]):
                    axe.axvline(x=xc, color='k', linestyle=':', lw=2, alpha=0.4)
            for xc in crises:
                if  pd.Timestamp(periods[0]) <= xc <= pd.Timestamp(periods[-1]):
                    axe.axvline(x=xc, color='k', linestyle='-', lw=2, alpha=0.4)
    except:
        for xc in fc_peaks:
            if  pd.Timestamp(periods[0]) <= xc <= pd.Timestamp(periods[-1]):
                ax.axvline(x=xc, color='k', linestyle=':', lw=2, alpha=0.4)
        for xc in crises:
            if  pd.Timestamp(periods[0]) <= xc <= pd.Timestamp(periods[-1]):
                ax.axvline(x=xc, color='k', linestyle='-', lw=2, alpha=0.4)


def plot_rec(ax, periods):
    rec0 = rec.loc[periods[0]: periods[-1]]
    try:
        for a in ax.ravel():
            a.fill_between(rec0.index, a.get_ylim()[0], a.get_ylim()[1], rec0['rec'], alpha=0.1)
    except:
        ax.fill_between(rec0.index, ax.get_ylim()[0], ax.get_ylim()[1], rec0['rec'], alpha=0.1)

