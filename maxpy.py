def show_df(df):
    print("O dataframe agora possui", df.shape[0], "linhas e", df.shape[1], "colunas.")
    print(df.info())
    print(df.count())
    print(df.columns)
    print(df.dtypes)
    print(df.describe())
    print(df.hist(bins=50, figsize=(20, 15)))
    return

def unique_values(df, coluna):
    print("Valores distintos de", coluna, df[coluna].unique())
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

