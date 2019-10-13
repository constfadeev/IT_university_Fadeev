# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:36:39 2019

@author: 21363
"""
import pandas as pd
from rutermextract import TermExtractor #https://pypi.org/project/rutermextract/
import codecs

term_extractor = TermExtractor()
df = pd.DataFrame(columns=['keyword', 'frequency'])

path = input('Введите путь к файлу: ')
with codecs.open(path, 'r', 'utf_8_sig') as file:
    text = file.read().replace('\n', '')

i = 0
for term in term_extractor(text, nested=True):
    df.loc[i] = [term.normalized, term.count]
    i += 1

top_percent = 0.1

df_top = df.loc[df.frequency > df.loc[int(df.shape[0]*top_percent)].frequency]
df_top.to_excel(f'{path[:path.rfind(".")] + "_"}keywords.xlsx', index=False)
