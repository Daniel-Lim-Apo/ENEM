import pandas as pd
import time
from sqlalchemy import create_engine
import time


def populate_table_tb_escola_participante(conn_string, originDataFrame, tableName):

    dfParticipante = originDataFrame[["NU_INSCRICAO", "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
                                      "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "IN_TREINEIRO"]]

    dfParticipante.columns = ['nu_inscricao_participante', 'sg_tipo_escola', 'sg_tipo_ensino',
                              'cd_dependencia_administrativa', 'sg_localizacao', 'cd_situacao_funcionamento', 'cd_municipio']


# nu_inscricao_participante
# sg_tipo_escola
# sg_tipo_ensino
# cd_dependencia_administrativa
# sg_localizacao
# cd_situacao_funcionamento
# cd_municipio

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
