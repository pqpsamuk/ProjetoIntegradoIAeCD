!pip install pandasql
import pandasql
import pandas as 
import numpy as np
ovnis = pd.read_csv('OVNIS.csv')
ovnis

#Removendo os valores vazios
ovnis.drop(ovnis.index[ovnis['City'] == 'None'], inplace = True)
ovnis.drop(ovnis.index[ovnis['City'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['State'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['Shape'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['Shape'] == "Unknown"], inplace = True)

#Removendo os NaN
ovnis['State'].dropna()
ovnis['Shape'].dropna()
ovnis['City'].dropna()

ovnis

q = """
   SELECT * from total where State LIKE '%AK%' OR State LIKE '%AL%'
OR State LIKE '%AR%'
OR State LIKE '%AZ%'
OR State LIKE '%CA%'
OR State LIKE '%CO%'
OR State LIKE '%CT%'
OR State LIKE '%DE%'
OR State LIKE '%FL%'
OR State LIKE '%GA%'
OR State LIKE '%HI%'
OR State LIKE '%IA%'
OR State LIKE '%ID%'
OR State LIKE '%IL%'
OR State LIKE '%IN%'
OR State LIKE '%KS%'
OR State LIKE '%KY%'
OR State LIKE '%LA%'
OR State LIKE '%MA%'
OR State LIKE '%MD%'
OR State LIKE '%ME%'
OR State LIKE '%MI%'
OR State LIKE '%MN%'
OR State LIKE '%MO%'
OR State LIKE '%MS%'
OR State LIKE '%MT%' 
OR State LIKE '%NC%' 
OR State LIKE '%ND%' 
OR State LIKE '%NE%' 
OR State LIKE '%NH%' 
OR State LIKE '%NJ%' 
OR State LIKE '%NM%' 
OR State LIKE '%NV%' 
OR State LIKE '%NY%' 
OR State LIKE '%OH%' 
OR State LIKE '%OK%' 
OR State LIKE '%OR%' 
OR State LIKE '%PA%' 
OR State LIKE '%RI%' 
OR State LIKE '%SC%' 
OR State LIKE '%SD%' 
OR State LIKE '%TN%' 
OR State LIKE '%TX%' 
OR State LIKE '%UT%' 
OR State LIKE '%VA%' 
OR State LIKE '%VT%' 
OR State LIKE '%WA%' 
OR State LIKE '%WI%' 
OR State LIKE '%WV%' 
OR State LIKE '%WY%'
  """

just_us = pandasql.sqldf(q.lower(), locals())
just_us

#just_us
#ajuste de colunas sem espaço
just_us.rename(columns = lambda x: x.replace('', '_'), inplace=True)

#Trocar o nome da coluna
just_us['DateTime'] = just_us['Date_/_Time']

#Filtro de dados
q = """
SELECT DateTime, City, State, Shape
FROM just_us
"""

df1 = pandasql.sqldf(q, locals())
df1

n_shape = df1['Shape'].value_counts()
maisQueMil = n_shape[n_shape > 1000]
maisQueMil

#Filtro de dados, agrupar depois filtrar
q = """
  SELECT * 
  FROM df1
  WHERE Shape in ('Light', 'Circle', 'Triangle', 'Fireball', 'Sphere', 'Other', 'Oval', 'Disk', 'Formation', 'Changing', 'Cigar, 'Flash', 'Rectangle')
  """

df2 = pandasql.sqldf(q, locals())
df2

#Gerar arquivo .csv
df2.to_csv('df_OVNI_limpo.csv')

ovnis = pd.read_csv('df_OVNI_limpo.csv')
ovnis

#Dividir o conteúdo 
ovnis['Sifht_Date'], ovnis['Sight_Time'] = ovnis['DateTime'].str.split('', 1).str

#Deletar coluna 
ovnis.drop(columns=['DateTime'], inplace=True)
ovnis

#Separar por dias da semana
time = pd.to_datetime(ovnis['Sight_Date'])
time = time.dt.dayofweek

dia_semana={0:'Segunda-feira', 1:'Terça-feira', 2:'Quarta-feira', 3:'Quinta-feira', 4:'Sexta-feira', 5:'Sábado', 6:'Domingo'}
ovnis['Sight_Weekday'] = time.map(dia_semana)
ovnis

#Separar meses e dias
ovnis['Sight_Day'] = ovnis['Sight_Date'].str.split('/', expand = True)[1]
ovnis['Sight_Month'] = ovnis['Sight_Date'].str.split('/', expand = True)[0]

#Gerar um arquivo .csv
ovnis.to_csv('df_OVNI_preparado.csv')
