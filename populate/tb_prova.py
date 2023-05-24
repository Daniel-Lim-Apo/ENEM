import pandas as pd
import time
from sqlalchemy import create_engine
import time


def populate_table_tb_prova(conn_string, originDataFrame, tableName):

    # originDataFrame.insert(1, 'cd_disciplina', 1)

    dfParticipante = originDataFrame[[
        "NU_INSCRICAO", 'CO_MUNICIPIO_PROVA']]

    dfParticipante.columns = ['nu_inscricao_participante',
                              'cd_municipio'
                              ]

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
