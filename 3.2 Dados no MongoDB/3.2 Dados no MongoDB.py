#Instalando o dnspython 
!curl ipecho.net/plain 
!pip install pymongo
Importando o pymongo
import pymongo
import pandas as pd
#Conexão do MongoDB com  o Atlas
client = pymongo.MongoClient("mongodb+srv://icdia:<password>@cluster0.u5bvh.mongodb.net/OVNI?retryWrites=true&w=majority")
#criando um Banco de dados 
db = client.ovni 
#Criando uma nova coleção 
ovnis = db.ovnis 
print(db.name)
print(client.list_database_names())
# Inserindo coleção criada em todos os registros do csv
OVNI_preparado = pd.read_csv('df_OVNI_preparado.csv') 
ovnis.insert_many(OVNI_preparado.to_dict('records'))
print(OVNI_preparado.count())
#Resgatar todos os registros da coleção
sort_shape = ovnis.find().sort('Shape',1)
for x in sort_shape:
  print(x)
  groupby_views = ovnis.aggregate([
... {"$group":{'_id':"$State",'Views':{'$sum':1}}}]);
for x in groupby_views:
  print(x)
find_phoenix = ovnis.find({'City':"Phoenix"},{ "_id": 1, "City": 1, "Shape": 1,
                                              "State":1,"Sight_day":1,"Sight_month":1,"Sight_time":1,"Sight_date":1, "Sight_weekday":1 })
for x in find_phoenix:
  print(x)
find_ca = ovnis.find({'State':"CA"},{ "_id": 0, "City": 1, "Shape": 1, "State":1,
                                     "Sight_day":1,"Sight_month":1,"Sight_time":1,"Sight_date":1, "Sight_weekday":1 })
for x in find_ca:
  print(x)