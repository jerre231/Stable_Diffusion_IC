from PIL import Image
import os, glob
from compression_data import compression_ratio


def imageCompressor(dataFrame,final_format,compressed_adress="Comprimida",compression_quality = 95):

    # Variáveis auxiliares e contadores

    class1_total = 0
    class1_size = 0
    class2_total = 0
    class2_size = 0


    # Variáveis utilizadas

    pilImages = {}       # Lista de images no formato da biblioteca PIL
    image_class=[]       # Define a classe da imagem
    compressRatio=[]     # Lista de Taxas de Compressão
    compressMeanUnple=[] # Auxiliar cálculo da média da taxa de compressão de imagens classe 1
    compressMeanUnple=[] # Auxiliar cálculo da média da taxa de compressão de imagens classe 2
    final_data=[]        # Lista com (Imagem, Taxa de compressão)


    # Extraindo imagens .PNG do diretório

    all_imgs = dataFrame[dataFrame.columns[0]].values.tolist() # Lista com todas as imagens
    number_of_imgs = len(all_imgs)                             # Número total de imagens

    # Loop de compressão das imagens:

    for i in range(number_of_imgs):

        pilImages[i]=Image.open(all_imgs[i])  # Abre a imagem com a biblioteca PIL
        img_dimension = pilImages[i].size     # Dimensão da imagem

        # Definindo endereços das imagens pré e pós compressão

        compressed_img_adress = f"{compressed_adress}/Comp_{final_format.upper()}_{i}.{final_format.lower()}"
        img_adress = all_imgs[i]


        # Realiza a compressão da imagem dado o formato final desejado


        # Comprime imagens no formato PNG

        if(final_format.lower() == "png"):

            pilImages[i].save(compressed_img_adress,optimize=True)

        # Comprime imagens no formato JPG

        elif(final_format.lower() == "jpg"):

            pilImages[i].save(compressed_img_adress,optimize=True,quality = compression_quality)

        else:

            print(f"Formato final '{final_format}' não suportado.")


        # Análise dos resultados da compressão

        compressRatio.append(compression_ratio(all_imgs[i],compressed_img_adress))

        image_class = dataFrame[dataFrame.columns[1]].values.tolist()

        if (image_class[i][0]=="p"):
            print("\nDetectei Classe 1 - Pleasant")
            class1_total = compressRatio[i] + class1_total
            class1_size = class1_size + 1
        else:
            print("\nDetectei Classe 2 - Unpleasant")
            class2_total = compressRatio[i] + class2_total
            class2_size = class2_size + 1

        print("\nCompressão de imagem do tipo "+ image_class[i]+":\n")

        class1_mean = round((class1_total/class1_size),1)
        class2_mean = round((class2_total/class2_size),1)

        print(f"A média da classe 1 foi : {class1_mean} %")
        print(f"A média da classe 2 foi : {class2_mean} %\n")


    for i in range(number_of_imgs):
       #print(imageInput[i],compressRatio[i])
       final_data.append([compressRatio[i],image_class[i]])

    print(final_data)

    return(compressRatio)
