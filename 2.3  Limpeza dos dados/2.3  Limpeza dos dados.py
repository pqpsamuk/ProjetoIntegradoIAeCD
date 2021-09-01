#importantando Bibliotecas
!pip install -U pandasql
import pandas as pd
import numpy as np
import pandasql
#Carregando o csv OVNIS.csv em um dataframe
ovnis = pd.read_csv('OVNIS.csv')
ovnis
#Removendo registros vazios
ovnis.drop(ovnis.index[ovnis['City'] == 'None'], inplace = True)
ovnis.drop(ovnis.index[ovnis['City'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['State'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['Shape'] == None], inplace = True)
ovnis.drop(ovnis.index[ovnis['Shape'] == "Unknown"], inplace = True)
ovnis['State'].dropna()
ovnis['Shape'].dropna()
ovnis['City'].dropna()

ovnis

sql = """
  SELECT * FROM ovnis WHERE 
  STATE LIKE 'AL'
  OR STATE LIKE 'AK' 
  OR STATE LIKE 'AZ'
  OR STATE LIKE 'AR'
  OR STATE LIKE 'CA'
  OR STATE LIKE 'CO' 
  OR STATE LIKE 'CT' 
  OR STATE LIKE 'DE'
  OR STATE LIKE 'DC'
  OR STATE LIKE 'FL'
  OR STATE LIKE 'GA'
  OR STATE LIKE 'HI'
  OR STATE LIKE 'ID'
  OR STATE LIKE 'IL'
  OR STATE LIKE 'IN'
  OR STATE LIKE 'IA'
  OR STATE LIKE 'KS'
  OR STATE LIKE 'KY'
  OR STATE LIKE 'LA'
  OR STATE LIKE 'ME'
  OR STATE LIKE 'MT'
  OR STATE LIKE 'NE'
  OR STATE LIKE 'NV'
  OR STATE LIKE 'NH'
  OR STATE LIKE 'NJ'
  OR STATE LIKE 'NM'
  OR STATE LIKE 'NY'
  OR STATE LIKE 'NC'
  OR STATE LIKE 'ND'
  OR STATE LIKE 'OH'
  OR STATE LIKE 'OK'
  OR STATE LIKE 'OR'
  OR STATE LIKE 'MD'
  OR STATE LIKE 'MA'
  OR STATE LIKE 'MI'
  OR STATE LIKE 'MN'
  OR STATE LIKE 'MS'
  OR STATE LIKE 'MO'
  OR STATE LIKE 'PA'
  OR STATE LIKE 'RI'
  OR STATE LIKE 'SC'
  OR STATE LIKE 'SD'
  OR STATE LIKE 'TN'
  OR STATE LIKE 'TX'
  OR STATE LIKE 'UT'
  OR STATE LIKE 'VT'
  OR STATE LIKE 'VA'
  OR STATE LIKE 'WA'
  OR STATE LIKE 'WV'
  OR STATE LIKE 'WI'
  OR STATE LIKE 'WY' 
  
"""

eua_registros = pandasql.sqldf(sql.lower(), locals())
eua_registros

#Removendo variaveis não imporantantes
eua_registros.rename(columns = lambda x: x.replace(' ', '_'), inplace=True)

#mudando o nome da coluna
eua_registros['DateTime'] = eua_registros['Date_/_Time']
#ovnis

#Filtrando dados
q = """
SELECT DateTime, City,	State,	Shape	
FROM eua_registros
"""

df1 = pandasql.sqldf(q, locals())
df1

#Registros com mais de 1000 ocorrencias

n_shape = df1['Shape'].value_counts()
maioresque1000 = n_shape[n_shape > 1000]
maioresque1000

#Filtrando dados e agrupando
q = """
SELECT *
FROM df1
WHERE Shape in ('Light', 'Circle', 'Triangle', 'Fireball', 'Sphere', 'Other', 'Oval', 'Disk', 'Formation', 'Changing', 'Cigar', 'Flash', 'Rectangle')

"""


df2 = pandasql.sqldf(q, locals())
df2

#Gerarando um arquivo csv limpo
df2.to_csv('df_OVNIS_limpo.csv')
