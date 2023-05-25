import pandas as pd
import time
from sqlalchemy import create_engine
import time
import asyncio


async def populate_table_tb_municipio(conn_string, originDataFrame, tableName):

    # .encode('utf-8')
    # originDataFrame.insert(1, 'cd_disciplina', 1)

    # Removing NAN values from the originDataFrame

    dfParticipante = originDataFrame[[
        "CO_MUNICIPIO_ESC", u'NO_MUNICIPIO_ESC', u'SG_UF_ESC']].dropna(subset=["CO_MUNICIPIO_ESC", 'NO_MUNICIPIO_ESC', 'SG_UF_ESC']).drop_duplicates()

    dfParticipante.columns = ['id_municipio',
                              'no_municipio',
                              'sg_uf'
                              ]

    dfParticipante['id_municipio'] = dfParticipante['id_municipio'].astype(int)
    print(dfParticipante.head(30))

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
