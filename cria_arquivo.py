# cria arquivo destino com 'limite' linhas a partir do arquivo origem
limite = 15000
arquivo_origem = "D:/Google Drive/IA&CD/Projetos/20191128 - Projeto 1/enem-2016/microdados_enem_2016_coma.csv" # disponível em https://www.kaggle.com/gbonesso/enem-2016. Possui 8.627.368 linhas
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
print("FIM")