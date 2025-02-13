## Criar Dataframe

data = {'Produto': ['A', 'B'], 'Preço': [100, 200]}
data_frame = pd.DataFrame(data)
 
### Tratamento de dados

#### Retirar nulos
dropna()

#### Preencher valores ausentes
fillna(valor que vai preencher)

#### Verificar duplicatas
duplicated()
df[~duplicatas]

#### Retirando duplicatas
drop_duplicates()

## Ler arquivos json

pd.read_json("nome do arquivo.extensão")

### Transforma de json para dataframe
pd.json_normalize(data['pessoas'], meta=['nome', 'idade', 'profissao'])

## Selecionar dados especificos

loc
df.loc[linhas, colunas]
df.loc[[0,1]]

iloc
df.iloc[linhas, colunas]


Método	Acessa por	Inclui último valor no slicing?	Exemplo
.loc[]	Rótulo do índice/coluna	✅ Sim	df.loc["a":"c", "Nome"]
.iloc[]	Posição (número inteiro)	❌ Não	df.iloc[0:2, 0]

## Mudar para excel

df.to_excel("arquivo.xlsx")

