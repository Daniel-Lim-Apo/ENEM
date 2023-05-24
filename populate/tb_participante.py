import pandas as pd
import time
from sqlalchemy import create_engine
import time


def populate_table_tb_participante(conn_string, originDataFrame, tableName):

    dfParticipante = originDataFrame[["NU_INSCRICAO", "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
                                      "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "IN_TREINEIRO"]]

    dfParticipante.columns = ['nu_inscricao_participante', 'cd_faixa_etaria', 'sg_sexo', 'cd_estado_civil',
                              'cd_cor_raca', 'cd_nacionalidade', 'cd_situacao_conclusao', 'cd_ano_conclusao_ensino_medio', 'bl_treineiro']

    dfParticipante['bl_treineiro'] = dfParticipante['bl_treineiro'].astype(
        bool)

    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
