import pandas as pd
import time
from sqlalchemy import create_engine
import time


def populate_table_tb_questionario_socioeconomico(conn_string, originDataFrame, tableName):

    dfParticipante = originDataFrame[[
        "NU_INSCRICAO", 'Q001', 'Q002', 'Q003', 'Q004', 'Q006', 'Q025']]

    dfParticipante.columns = ['nu_inscricao_participante', 'cd_nivel_escolaridade_pai', 'cd_nivel_escolaridade_mae',
                              'cd_grupo_ocupacao_pai', 'cd_grupo_ocupacao_mae', 'cd_faixa_renda_familiar', 'bl_acesso_internet']

# nu_inscricao_participante
# cd_nivel_escolaridade_pai
# cd_nivel_escolaridade_mae
# cd_grupo_ocupacao_pai
# cd_grupo_ocupacao_mae
# cd_faixa_renda_familiar
# bl_acesso_internet

    dfParticipante['bl_acesso_internet'] = dfParticipante['bl_acesso_internet'].astype(
        bool)

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
