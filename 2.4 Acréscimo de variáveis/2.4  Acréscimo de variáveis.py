#Importando Bibliotecas
import pandas as pd

#Carregando o arquivo csv
df_OVNI_limpo = pd.read_csv('df_OVNI_limpo.csv')
df_OVNI_limpo

#Gerando a coluna Date/time para o formato datetime 
df_OVNI_limpo['Date / Time'] = pd.to_datetime(df_OVNIS_limpo['Date / Time'])
df_OVNI_limpo

#Chamando o tipo
df_OVNI_limpo.dtypes

#Dia
df_OVNI_limpo['Sight_day'] =df_OVNI_limpo['Date / Time'].dt.day
df_OVNI_limpo

#Mes
df_OVNI_limpo['Sight_month'] =df_OVNI_limpo['Date / Time'].dt.month
df_OVNI_limpo

#Tempo
 df_OVNI_limpo['Sight_time'] =df_OVNI_limpo['Date / Time'].dt.time
 df_OVNI_limpo

#Data
 df_OVNI_limpo['Sight_date'] =df_OVNI_limpo['Date / Time'].dt.date
 df_OVNI_limpo

#Fim de semana
df_OVNI_limpo['Sight_weekday'] =df_OVNI_limpo['Date / Time'].dt.weekday
df_OVNI_limpo

#Dias da semana
 dayOfWeek={0:'Segunda-feira', 1:'Terça-feira', 2:'Quarta-feira', 3:'Quinta-feira', 4:'Sexta-feira', 5:'Sábado', 6:'Domingo'}
df_OVNI_limpo['Sight_weekday'] =df_OVNI_limpo['Date / Time'].dt.dayofweek.map(dayOfWeek)
df_OVNI_limpo

df_OVNI_limpo['Sight_weekday'].value_counts()
df_OVNI_limpo.drop(['Date / Time'],axis=1,inplace=True)
df_OVNI_limpo

#Armazenando no novo CSV 'df_OVNIS_preparado'

df_OVNI_limpo.to_csv('df_OVNI_preparado.csv',index=False)
df_OVNI_preparado= pd.read_csv('df_OVNI_preparado.csv')
df_OVNI_preparado