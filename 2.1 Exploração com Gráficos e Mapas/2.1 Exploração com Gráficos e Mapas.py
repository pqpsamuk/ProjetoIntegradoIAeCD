#importações para o código
!pip install -U pandasql
!pip install folium
import pandas as pd
import seaborn as sns
import pandasql
import numpy as np
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

#os quatros estados com a maior frequencia de relatos

baseOvnis = pd.read_csv("OVNIS.csv")

#Estados
estados = baseOvnis['State'].value_counts().head(4)

#Criando um dataFrame
df_relatos = pd.DataFrame(estados)

#Criando a coluna dos estado da indice
df_relatos['stateName'] = df_relatos.index

#retornando o indice
df_relatos.reset_index(drop=True, inplace=True)

df_relatos

#Ovnis mais populares dos relatos

tipos = baseOvnis['Shape'].value_counts().head(4)

#Criando um dataFrame
df_ovnis = pd.DataFrame(tipos)

#Criando a coluna dos Ovnis com a indice
df_ovnis['shapesName'] = df_ovnis.index

#mudando o nome
df_ovnis.columns =  ['Qtd', 'shapesName']

#retornando o indice
df_ovnis.reset_index(drop=True, inplace=True)

df_ovnis


#filtrando por estados x Tipos
import pandas
!pip install -U pandasql
import pandasql

baseOvnis = pd.read_csv("OVNIS.csv")


q= """
SELECT State, Shape, COUNT(*) AS VIEWS 
FROM baseOvnis
WHERE State IN('CA','FL','WA','TX') AND Shape IN('Light','Circle','Triangle','Fireball')
GROUP BY State, Shape
ORDER BY VIEWS DESC
"""

Tabela1 = pandasql.sqldf(q, locals())
pd.DataFrame(Tabela1)

# Gerando o primeiro Gráfico 

import numpy as np
import matplotlib.pyplot as plt

Light = [1701, 826, 780, 579]
Circle = [881, 551, 330, 290]
Fireball  = [703, 541, 296, 183]
Triangle  = [640, 344, 301, 245]
 
barWidth = 0.15
plt.figure(figsize=(7,5))


r1 = np.arange(len(Light))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, Light, color='gold', width=barWidth, label='Light')
plt.bar(r2, Circle, color='grey', width=barWidth, label='Circle')
plt.bar(r3, Triangle	, color='saddlebrown', width=barWidth, label='Fireball')
plt.bar(r4, Fireball, color='blue', width=barWidth, label='Triangle')
 
# inserindo legendas
plt.xlabel('State')
plt.xticks([r + barWidth for r in range(len(Light))], ['CA', 'WA', 'FL', 'TX'])
plt.ylabel('Views')
plt.title('Group of Bars')
 
# gerando a legenda e criando o grafico
plt.legend()
plt.show()

# Gerando o Segundo Gráfico 
Light  = np.array((1701, 826, 780, 579))
Circle = np.array((881, 551, 330, 290))
Fireball  = np.array((703, 541, 296, 183))
Triangle  = np.array((640, 344, 301, 245))

shape = ['Light','Circle','Fireball', 'Triangle']

states = ['CA','WA','FL', 'TX']


plt.figure(figsize=(7,5))


plt.bar(states, Light, color = 'gold')
plt.bar(states, Circle, color = 'grey', bottom = Light)
plt.bar(states, Fireball, color = 'saddlebrown', bottom = Light + Circle)
plt.bar(states, Triangle, color = 'blue', bottom = Light + Circle + Fireball)

# inserindo legendas
plt.xlabel('State')
plt.ylabel('Views')
plt.title('Stacket Bar')
plt.legend(('Light', 'Circle', 'Fireball', 'Triangle'))

plt.show()

#Gerando os Mapas
!pip install folium
import folium

#Tipos diferentes de mapas

folium.Map(
    location=[-19.916667,-43.933333],
    tiles='Stamen Toner',
)
folium.Map(
    location=[-19.916667,-43.933333],
    tiles='Stamen Terrain',
)

#Gerando o Mapa CA
CAlat = 37.2502200
CAlon = -119.7512600

WAlat = 38.904
WAlon = -77.0171

FLlat = 28.4159
FLlon = -81.2988

TXlat = 29.3838500
TXlon = -94.9027000

#mapa = folium.Map(location=[CAlat, CAlon])
#mapa = folium.Map(location=[WAlat, WAlon])
#mapa = folium.Map(location=[FLlat, FLlon])
mapa = folium.Map(location=[TXlat, TXlon])

mapa

#ZIPCODES ou cep

!pip install zipcodes
importando a biblioteca zipcode
import zipcodes
zipcodes_json = zipcodes.list_all()
df_zipcodes = pd.DataFrame(zipcodes_json)
df_zipcodes