import pandas as pd 
import json
# Use como teste
# data = {'Produto': ['A', 'B'], 'Preço': [100, 200]}
# df = pd.DataFrame(data)
# df['Disponibilidade'] = ['Indisp', 'Disp']
# print(df)

with open('pandas/pessoas.json', encoding='utf-8') as values:
    data = json.load(values)

df = pd.json_normalize(data['pessoas'], meta=['nome','idade', 'profissao' ])
df.columns = ['Nome', 'Idade', 'Profissão']
df_tratado = df.dropna(subset=['Nome'])
df_tratado['Profissão'] = df_tratado['Profissão'].fillna('Desempregado')
df_tratado['Idade'] =  df_tratado['Idade'].fillna(0).astype(int)

print(df_tratado[df_tratado['Profissão'] == 'Designer'])
# with open('pandas/pessoas.json', encoding='utf-8') as f:
#     data = json.load(f)

# df = pd.json_normalize(data['pessoas'], meta=['nome', 'idade', 'profissao'])
# df.columns = ['Nome', 'Idade', 'Profissão']
# df2 = df.dropna(subset=['Nome'])
# df2['Profissão'] = df2['Profissão'].fillna('Desempregado')
# df2['Idade'] = df2['Idade'].fillna('0').astype(int)
# print(df2.loc[0])
