import requests
from bs4 import BeautifulSoup
import pandas as pd
td_data = list()
th_data = list()
#1997
print('1997')
print('Setembro')
URL = f'http://www.nuforc.org/webreports/ndxe199709.html'
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
table = soup.findAll('table')[0]
tr = table.findAll(['tr'])
try:   
        for cell in tr:
            th = cell.find_all('th')
            th_data.append([col.text.strip('\n') for col in th])
            td = cell.find_all('td')
            row = [i.text.replace('\n','') for i in td]
            td_data.append(row)
finally:   
    print('Completado')
#1998 de 1999 entre mês de janeiro até Setembro
for i in range(8,10):
  print('199{}'.format(i))
  for p in range(1,10):
    print('Mês ',p)
    URL = f'http://www.nuforc.org/webreports/ndxe199{i}0{p}.html'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.findAll('table')[0]
    tr = table.findAll(['tr'])
    try:   
            for cell in tr:
                th = cell.find_all('th')
                th_data.append([col.text.strip('\n') for col in th])
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                td_data.append(row)
    finally:   
        print('Completado')
# 1997 de 1999, entre mês outubro até dezembro
for i in range(7,10):
  print('199{}'.format(i))
  for p in range(0,3):
    print(' 1{}'.format(p))
    URL = f'http://www.nuforc.org/webreports/ndxe199{i}1{p}.html'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.findAll('table')[0]
    tr = table.findAll(['tr'])
    try:   
            for cell in tr:
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                td_data.append(row)
    finally:   
        print('Completado')
  #2000 de 2009 entre mês de janeiro até setembro
for i in range(0,10):
  print('{}'.format(i))
  for p in range(1,10):
    print('{}'.format(p))
    URL = f'http://www.nuforc.org/webreports/ndxe200{i}0{p}.html'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.findAll('table')[0]
    tr = table.findAll(['tr'])
    try:   
            for cell in tr:
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                td_data.append(row)
    finally:   
        print('Completado')
  #2010 de 2016, entre o mês de janeiro até setembro
for i in range(0,7):
  print('201{}'.format(i))
  for p in range(1,10):
    print('{}'.format(p))
    URL = f'http://www.nuforc.org/webreports/ndxe201{i}0{p}.html'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.findAll('table')[0]
    tr = table.findAll(['tr'])
    try:   
            for cell in tr:
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                td_data.append(row)
    finally:   
        print('Completado')
#2010 até 2016, entre o mês de outubro até dezembro
for i in range(0,7):
  print('201{}'.format(i))
  for p in range(0,3):
    print('1{}'.format(p))
    URL = f'http://www.nuforc.org/webreports/ndxe201{i}1{p}.html'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.findAll('table')[0]
    tr = table.findAll(['tr'])
    try:   
            for cell in tr:
                td = cell.find_all('td')
                row = [i.text.replace('\n','') for i in td]
                td_data.append(row)
    finally:   
        print('Completado')
#2017 mês de agosto
print('Ano 2017')
for p in range(1,9):
  print(' ',p)
  URL = f'http://www.nuforc.org/webreports/ndxe20170{p}.html'
  headers={
      'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
  }
  page = requests.get(URL,headers=headers)
  soup = BeautifulSoup(page.content,'html.parser')
  table = soup.findAll('table')[0]
  tr = table.findAll(['tr'])
  try:   
          for cell in tr:
              td = cell.find_all('td')
              row = [i.text.replace('\n','') for i in td]
              td_data.append(row)
  finally:   
      print('Completado')
del th_data[1:-1]
th_data.pop(-1)
th_data
df = pd.DataFrame(td_data)
df1 = df.dropna()
colum = []
for i in th_data:
  colum = i
df1.columns = colum
df1
df1.to_csv('OVNIS.csv',index=False)
total = pd.read_csv('OVNIS.csv')
total