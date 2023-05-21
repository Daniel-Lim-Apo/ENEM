import pandas as pd

import os

# print (os.listdir(os.curdir))

# enem_2021 = pd.read_csv('.\dados\microdados_enem_2021\DADOS\MICRODADOS_ENEM_2021.csv', nrows=10000, encoding='iso-8859-1', sep=';')
enem_2021 = pd.read_csv(
    '.\dados\microdados_enem_2021\DADOS\MICRODADOS_ENEM_2021.csv', encoding='iso-8859-1', sep=';')

# print(enem_2021.columns)

states = pd.unique(enem_2021["SG_UF_PROVA"])

# print(states.size)
# print(states)

dictDataByStateRegistries = {}
dictDataByStateAllCollumns = {}

dictDataByStateRegistries["Total"] = [len(enem_2021)]
dictDataByStateAllCollumns["Total"] = enem_2021.count()

for state in states:
    # print(type(state))
    # filter = "SG_UF_PROVA" + state +
    arquivo = ".\dados\microdados_enem_2021\DADOS\DadosByUF\MICRODADOS_ENEM_2021_" + state + ".csv"
    # print(arquivo)

    dfEnem = enem_2021[enem_2021["SG_UF_PROVA"] == state]

    dictDataByStateRegistries[state] = [len(dfEnem)]
    # print(dfEnem.columns)
    dictDataByStateAllCollumns[state] = dfEnem.count()

    dfEnem.to_csv(arquivo, mode='w', index=False)
    # pd.DataFrame(columns=["SG_UF_PROVA"], index=[state]).to_csv(arquivo)
    # pd.DataFrame(columns=["SG_UF_PROVA"], index=[state]) >> arquivo

    # print(porEstado.head(10))


dfDictDataByStateAllCollumns = pd.DataFrame.from_dict(
    dictDataByStateAllCollumns)
dfDictDataByStateAllCollumns.to_csv(
    r'.\dados\microdados_enem_2021\DADOS\DadosByUF\Stats\RegistriesByUFAllCollumns.csv', index=False, header=True, line_terminator='\r\n')

dfDictDataByStateRegistries = pd.DataFrame.from_dict(dictDataByStateRegistries)
dfDictDataByStateRegistries.to_csv(
    r'.\dados\microdados_enem_2021\DADOS\DadosByUF\Stats\RegistriesByUF.csv', index=False, header=True, line_terminator='\r\n')
