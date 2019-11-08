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