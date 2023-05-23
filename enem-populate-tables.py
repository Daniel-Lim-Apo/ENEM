import time
import pandas as pd
from sqlalchemy import create_engine
import os
# import psycopg2
# from populate.tb_participante import populate_table_tb_participante
from populate.tb_questionario_socioeconomico import populate_table_tb_questionario_socioeconomico

from populate.tb_prova import populate_table_tb_prova
from populate.tb_prova_objetiva_CN import populate_table_tb_prova_objetiva_CN
from populate.tb_prova_objetiva_CH import populate_table_tb_prova_objetiva_CH
from populate.tb_prova_objetiva_LC import populate_table_tb_prova_objetiva_LC
from populate.tb_prova_objetiva_MT import populate_table_tb_prova_objetiva_MT

# INPUT YOUR OWN CONNECTION STRING HERE
conn_string = 'postgresql://postgres:z77zpoqq@localhost:5432/enem'
# print(os.getcwd())
enem_2021 = pd.read_csv('dados\microdados_enem_2021\DADOS\DadosByUF\MICRODADOS_ENEM_2021_AC.csv',
                        nrows=10000, encoding='iso-8859-1', sep=',')

# populate_table_tb_participante(conn_string, enem_2021, 'tb_participante')
# populate_table_tb_escola_participante(conn_string, enem_2021, 'tb_escola_participante')
# populate_table_tb_questionario_socioeconomico(
#     conn_string, enem_2021, 'tb_questionario_socioeconomico')

populate_table_tb_prova(
    conn_string, enem_2021, 'tb_prova')

populate_table_tb_prova_objetiva_CN(
    conn_string, enem_2021, 'tb_prova_objetiva')

populate_table_tb_prova_objetiva_CH(
    conn_string, enem_2021, 'tb_prova_objetiva')

populate_table_tb_prova_objetiva_LC(
    conn_string, enem_2021, 'tb_prova_objetiva')

populate_table_tb_prova_objetiva_MT(
    conn_string, enem_2021, 'tb_prova_objetiva')

print("End of popluating tables")
