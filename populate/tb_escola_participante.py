import pandas as pd
import time
from sqlalchemy import create_engine
import time
import asyncio


async def populate_table_tb_escola_participante(conn_string, originDataFrame, tableName):

    dfParticipante = originDataFrame[["NU_INSCRICAO",
                                      "TP_ESCOLA",
                                      "TP_ENSINO",
                                      "TP_DEPENDENCIA_ADM_ESC",
                                      "TP_LOCALIZACAO_ESC",
                                      "TP_SIT_FUNC_ESC",
                                      "CO_MUNICIPIO_ESC"]].dropna()

    dfParticipante.columns = ['nu_inscricao_participante',
                              'sg_tipo_escola',
                              'sg_tipo_ensino',
                              'cd_dependencia_administrativa',
                              'sg_localizacao',
                              'cd_situacao_funcionamento',
                              'cd_municipio']

    dfParticipante['sg_tipo_escola'] = dfParticipante['sg_tipo_escola'].astype(
        int)
    dfParticipante['sg_tipo_ensino'] = dfParticipante['sg_tipo_ensino'].astype(
        int)
    dfParticipante['cd_dependencia_administrativa'] = dfParticipante['cd_dependencia_administrativa'].astype(
        int)
    dfParticipante['sg_localizacao'] = dfParticipante['sg_localizacao'].astype(
        int)
    dfParticipante['cd_situacao_funcionamento'] = dfParticipante['cd_situacao_funcionamento'].astype(
        int)
    dfParticipante['cd_municipio'] = dfParticipante['cd_municipio'].astype(int)

    dfParticipante['sg_localizacao'] = dfParticipante['sg_localizacao'].replace({
                                                                                1: 'U', 2: 'R'})
    dfParticipante['sg_tipo_ensino'] = dfParticipante['sg_tipo_ensino'].replace({
                                                                                1: 'REG', 2: 'ESP'})
    dfParticipante['sg_tipo_escola'] = dfParticipante['sg_tipo_escola'].replace({
                                                                                1: 'NR', 2: 'PUB', 3: 'PRI'})

    # print(dfParticipante[['nu_inscricao_participante',
    #       'sg_localizacao']].head(20))
# nu_inscricao_participante

# sg_tipo_escola

# sg_tipo_ensino

# cd_dependencia_administrativa

# sg_localizacao

# cd_situacao_funcionamento

# cd_municipio
    db = create_engine(conn_string)
    conn = db.connect()
    start_time = time.time()
    dfParticipante.to_sql(tableName, con=conn,
                          if_exists='append', index=False)
    print("to_sql " + tableName +
          " duration: {} seconds".format(time.time() - start_time))
    conn.close()
