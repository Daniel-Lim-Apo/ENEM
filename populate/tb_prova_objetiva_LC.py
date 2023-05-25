import pandas as pd
import time
from sqlalchemy import create_engine
import time
import asyncio


async def populate_table_tb_prova_objetiva_LC(conn_string, originDataFrame, tableName):

    dfParticipante = originDataFrame[[
        "NU_INSCRICAO", 'TP_PRESENCA_LC', 'CO_PROVA_LC', 'NU_NOTA_LC']]

    dfParticipante.insert(1, 'cd_disciplina', 3)

    dfParticipante.columns = ['nu_inscricao_participante',
                              'cd_disciplina',
                              'cd_tipo_presenca',
                              'cd_tipo_prova',
                              'nu_nota',
                              ]

# CO_PROVA_CN
# CO_PROVA_CH
# CO_PROVA_LC
# CO_PROVA_MT
    # (1,'Ciências da Natureza'),
    # (2,'Ciências Humanas'),
    # (3,'Linguagens e Códigos'),
    # (4,'Matemática');

#   (0,'Faltou à prova'),
# 	(1,'Presente na prova'),
# 	(2,'Eliminado na prova');

# nu_inscricao_participante,
#   cd_disciplina,
#   cd_tipo_presenca,
#   cd_tipo_prova,
#   nu_nota,

    # dfParticipante['bl_acesso_internet'] = dfParticipante['bl_acesso_internet'].astype(
    #     bool)

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
