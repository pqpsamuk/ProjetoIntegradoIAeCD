# Importação do panda
import pandas as pd
# Carrega seu arquivo csv
ovnis_preparado = pd.read_csv('df_OVNI_preparado.csv')
ovnis_preparado
#filtra a cidade dentro do csv
cidade_phoenix = ovnis_preparado[ovnis_preparado['City']=='Phoenix']
cidade_phoenix.sort_values(by='Sight_date')
import pandasql
# Roda o seu comando SQL e retorna um dataframe
query = '''
 SELECT Sight_date ,Count(*) as Views FROM cidade_phoenix  group by Sight_day,  Sight_month order by Sight_date 
'''
views_phoenix= pandasql.sqldf(query.lower(), locals())
views_phoenix
#filtra a data e o ano
views_phoenix['Sight_date'] = pd.to_datetime(views_phoenix['Sight_date'])
views_phoenix.dtypes
views_phoenix['Sight_year'] = views_phoenix['Sight_date'].dt.year
views_phoenix
# Roda o seu comando SQL e retorna um dataframe
query = '''
 SELECT Count(*) as views, Sight_year FROM views_phoenix  group by Sight_year 
'''
views_phoenix_per_year= pandasql.sqldf(query.lower(), locals())
views_phoenix_per_year
views_phoenix_per_year.plot.line(x='Sight_year',y='views')