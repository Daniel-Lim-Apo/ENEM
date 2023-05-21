import pandas as pd
import matplotlib

microDadosENEM = pd.read_csv('./dados/microdados_enem_2021/DADOS/MICRODADOS_ENEM_2021.csv', sep=";", encoding="ISO-8859-1")

print(microDadosENEM.head())

