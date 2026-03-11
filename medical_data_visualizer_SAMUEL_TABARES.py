import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

    # 1
df = pd.read_csv('C:/DISEÑO/Analisis de datos/Data/medical_examination.csv')

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2) > 25

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).size().rename(columns = {'size': 'count'})
    
    # 7
    fig = sns.catplot(x = 'variable', y = 'count', hue = 'value', col = 'cardio', data = df_cat, kind = 'bar')

    # 8
    fig = fig
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14
    fig, ax = plt.subplots(figsize = (12,12))
    
    # 15
    sns.heatmap(corr, annot = True, fmt = '.1f', mask = mask, square = True, linewidths = 0.5, cbar_kws = {'shrink': 0.5, 'ticks': [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]})


    # 16
    fig.savefig('heatmap.png')
    plt.close(fig)
    return fig

draw_cat_plot()
draw_heat_map()