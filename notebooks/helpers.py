import numpy as np


def jitter(df, col, amt=.5):
    return df[col] + np.random.random(len(df))*amt - amt/2


def debug(df, extra=''):
    print(f'{extra} {df.shape=}')
    return df


def limit_n(df, col, n=20, other='Other'):
    top = (df
           [col]
           .value_counts()
           )

    topn = top.index[:n]
    return df[col].where(df[col].isin(topn), other)

