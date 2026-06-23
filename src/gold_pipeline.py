from pathlib import Path
import pandas as pd
import logging
import json

def ler_silver(path):
    data = []
    p = Path(str(path))
    files = [i for i in p.glob('*.json')]
    for i in files:
        with open(i, encoding='utf-8') as file:
            data_json = json.load(file)
            data.extend(data_json)
    return data

def transformar_em_df(path):
    data = ler_silver(path)
    df = pd.json_normalize(
        data,
        record_path='recipe',
        meta=['data', 'id_cliente']
    )
    return df

def aplicacao_por_cultura(df, path):
    p = Path(path)
    path_json = p / 'dosagem_por_cultura.json'
    df_cultura = df.groupby('cultura')['dosagem'].agg('sum').sort_values(ascending=False)
    df_cultura.to_json(path_json, force_ascii=False ,indent=2)
    return df_cultura

df = transformar_em_df('medallion/silver')
df_cultura = aplicacao_por_cultura(df, 'medallion/gold')
# print(df_cultura)