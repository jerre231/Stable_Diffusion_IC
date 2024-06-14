import numpy as np
import matplotlib.pyplot as plt
import os


'''
#Função usada para comprimir as imagens: (caso necessário)

def compress(original, compressed):
    imagem_original = Image.open(original)
    imagem_original.save(compressed, optimize=True)

'''

def plt_graph(file_path, weight):

    file_size = []

    for i in range(file_path):
        image_size = os.path.getsize(file_path[i])
        file_size[i].append(image_size)

    plt.figure(figsize=10, weight)
    for i in range(weight):
        plt.plot(range(1, weight+1), ()file_size[i][0]/(512*512*3)), marker='o', label=f'Image{i+1}')

    plt.title('Peso x Complexidade')
    plt.xlabel('Peso')
    plt.ylabel('Complexidade')
    plt.xticks(range(1, weight+1))
    plt.legend()
    plt.grid(True)
    plt.show()
