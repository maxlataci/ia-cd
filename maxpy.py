import pandas as pd
import matplotlib.pyplot as plt

def show_df(df):
    print("O dataframe agora possui", df.shape[0], "linhas e", df.shape[1], "colunas.")
    print(df.info())
    print(df.count())
    print(df.columns)
    print(df.dtypes)
    print(df.describe())
    print(df.hist(bins=50, figsize=(20, 15)))
    return

def correlacao(df, campo1, campo2):
    print(df[campo1].corr(df[campo2]))
    plt.scatter(df[campo1], df[campo2])

def agrupa_estados_regiao(df, campo_estado, campo_regiao):
    regiao_norte = ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO']
    regiao_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
    regiao_centrooeste = ['DF', 'GO', 'MS', 'MT']
    regiao_sudeste =['ES', 'MG', 'RJ', 'SP']
    regiao_sul = ('PR', 'RS', 'SC')

    df[campo_regiao] = 'NaN'
    for index, row in df.iterrows():
        if df.loc[index, campo_estado] in regiao_sul:
            df.loc[index, campo_regiao] = "S"
        elif df.loc[index, campo_estado] in regiao_centrooeste:
            df.loc[index, campo_regiao] = "CO"
        elif df.loc[index, campo_estado] in regiao_sudeste:
            df.loc[index, campo_regiao] = "SE"
        elif df.loc[index, campo_estado] in regiao_norte:
            df.loc[index, campo_regiao] = "N"
        else:
            df.loc[index, campo_regiao] = "NE"
    unique_values(df, campo_regiao)

def unique_values(df, coluna):
    print("Valores distintos de", coluna, df[coluna].unique())
    print(pd.value_counts(df[coluna].values, sort=True), "\n")
    return

def drop_columns(df, colunas):
    for coluna in colunas:
        df.drop(coluna, axis=1, inplace=True)
    return

def create_subset(arquivo_origem, limite):
    # cria arquivo destino com 'limite' linhas a partir do arquivo origem
    arquivo_destino = arquivo_origem.replace(".", "_" + str(limite) + ".")
    i = 0

    origem = open(arquivo_origem, "r")
    destino = open(arquivo_destino, "w")

    for linha in origem:
        destino.write(linha)
        i += 1
        if (i > limite):
            break

    origem.close()
    destino.close()
    return arquivo_destino

