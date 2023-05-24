import pandas as pd
import time
from sqlalchemy import create_engine
import time


def populate_table_tb_redacao(conn_string, originDataFrame, tableName):

    # originDataFrame.insert(1, 'cd_disciplina', 1)

    dfParticipante = originDataFrame[[
        "NU_INSCRICAO",
        'TP_STATUS_REDACAO',
        'NU_NOTA_COMP1',
        'NU_NOTA_COMP2',
        'NU_NOTA_COMP3',
        'NU_NOTA_COMP4',
        'NU_NOTA_COMP5',
        'NU_NOTA_REDACAO']]

    dfParticipante.columns = ['nu_inscricao_participante',
                              'cd_status_redacao',
                              'nu_nota_comp1',
                              'nu_nota_comp2',
                              'nu_nota_comp3',
                              'nu_nota_comp4',
                              'nu_nota_comp5',
                              'nu_nota_redacao'
                              ]

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
