# import packages
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

# establish connections
conn_string = 'postgresql://postgres:z77zpoqq@127.0.0.1/enem'

db = create_engine(conn_string)
conn = db.connect()
# conn1 = psycopg2.connect(
#     database="Airlines_Database",
#     user='postgres',
#     password='pass',
#     host='127.0.0.1',
#     port='5432'
# )

# conn1.autocommit = True
# cursor = conn1.cursor()
# cursor = conn.cursor()

# drop table if it already exists
# cursor.execute('drop table if exists airlines_final')

# sql = '''CREATE TABLE airlines_final(id int ,
# day int ,airline char(20),destination char(20));'''

# cursor.execute(sql)

# import the csv file to create a dataframe
# data = pd.read_csv("airlines_final.csv")
print(os.getcwd())
os.chdir('..\..')
print(os.getcwd())
os.chdir('..\..\dados\microdados_enem_2022\DADOS')
print(os.listdir('..\..\dados\microdados_enem_2022\DADOS'))

enem_2021 = pd.read_csv('..\..\dados\microdados_enem_2022\DADOS\MICRODADOS_ENEM_2022.csv',
                        nrows=10000, encoding='iso-8859-1', sep=';')

print(enem_2021.columns)

data = enem_2021[["id", "day", "airline", "destination"]]
# Create DataFrame
print(data)

# converting data to sql
data.to_sql('airlines_final', conn, if_exists='replace')

# fetching all rows
sql1 = '''select * from airlines_final;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)

conn1.commit()
conn1.close()
