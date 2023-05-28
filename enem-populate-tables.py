import time
import pandas as pd
from sqlalchemy import create_engine
import os
import asyncio
# import psycopg2
from populate.tb_participante import populate_table_tb_participante
from populate.tb_escola_participante import populate_table_tb_escola_participante
from populate.tb_questionario_socioeconomico import populate_table_tb_questionario_socioeconomico
from populate.tb_municipio import populate_table_tb_municipio
from populate.tb_prova import populate_table_tb_prova
from populate.tb_prova_objetiva_CN import populate_table_tb_prova_objetiva_CN
from populate.tb_prova_objetiva_CH import populate_table_tb_prova_objetiva_CH
from populate.tb_prova_objetiva_LC import populate_table_tb_prova_objetiva_LC
from populate.tb_prova_objetiva_MT import populate_table_tb_prova_objetiva_MT
from populate.tb_redacao import populate_table_tb_redacao


async def main():
    # INPUT YOUR OWN CONNECTION STRING HERE
    conn_string = 'postgresql://postgres:yourpass@localhost:5432/enem'
    # print(os.getcwd())
    # enem_2021 = pd.read_csv('dados\microdados_enem_2021\DADOS\DadosByUF\MICRODADOS_ENEM_2021_AC.csv',
    #                         nrows=10000, encoding='iso-8859-1', sep=',')
    # enem_2021 = pd.read_csv('dados\microdados_enem_2021\DADOS\DadosByUF\MICRODADOS_ENEM_2021_AC.csv',
    #                         nrows=10000, encoding='utf-8', sep=',')
    enem_2021 = pd.read_csv(
        'dados\microdados_enem_2021\DADOS\MICRODADOS_ENEM_2021.csv', encoding='latin-1', sep=';')

    await asyncio.gather(
        # populate_table_tb_municipio(
        #     conn_string, enem_2021, 'tb_municipio'),

        # populate_table_tb_participante(
        #     conn_string, enem_2021, 'tb_participante'),

        populate_table_tb_escola_participante(
            conn_string, enem_2021, 'tb_escola_participante'),

        # populate_table_tb_questionario_socioeconomico(
        #     conn_string, enem_2021, 'tb_questionario_socioeconomico'),

        # populate_table_tb_prova(
        #     conn_string, enem_2021, 'tb_prova'),

        # populate_table_tb_prova_objetiva_CN(
        #     conn_string, enem_2021, 'tb_prova_objetiva'),

        # populate_table_tb_prova_objetiva_CH(
        #     conn_string, enem_2021, 'tb_prova_objetiva'),

        # populate_table_tb_prova_objetiva_LC(
        #     conn_string, enem_2021, 'tb_prova_objetiva'),

        # populate_table_tb_prova_objetiva_MT(
        #     conn_string, enem_2021, 'tb_prova_objetiva'),

        # populate_table_tb_redacao(
        #     conn_string, enem_2021, 'tb_redacao'),
    ),
    print("End of popluating tables"),
asyncio.run(main())
