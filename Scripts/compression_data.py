# Autoral de joaoxvitor18@poli.ufrj.br

import os, glob



def compression_ratio(uncompImgPath,compImgPath):

    # Retira o tamanho das imagens antes e depois da compressão

    uncompImgSize = round(((os.stat(f'{uncompImgPath}').st_size)/1000) , 1)
    compImgSize = round(((os.stat(f'{compImgPath}').st_size)/1000) , 1)

    # Cria o valor de compressão/complexibilidade


    compressRatio = round( ((1- (compImgSize/uncompImgSize))*100), 1)

    print(f"Valor sem compressão : {uncompImgSize} kb")
    print(f"Valor com compressão : {compImgSize} kb")
    print(f"Taxa de compressão   : {compressRatio} %")

    return (compressRatio)