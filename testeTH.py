import sys
import numpy as np 

entrada = [[1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0],
           [1, 1, 0, 0, 1, 1,
            1, 1, 0, 0, 1, 1,
            1, 1, 1, 1, 1 ,1,
            1, 1, 1, 1, 1, 1,
            1, 1, 0, 0, 1, 1,
            1, 1, 0, 0, 1, 1,]]
saida_desejada = [[1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 1, 0, 0],
           [1, 1, 0, 0, 1, 1,
            1, 1, 0, 0, 1, 1,
            1, 1, 1, 1, 1 ,1,
            1, 1, 1, 1, 1, 1,
            1, 1, 0, 0, 1, 1,
            1, 1, 0, 0, 1, 1,]]
peso =     [0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]
taxa_aprendizado = 0.01

def ativar_neuronio(entrada, peso):
    soma = 0
    for i in range(len(peso)):
        soma += entrada[i] * peso [i]
        print("Soma da posicao:", i, "=", soma)
    return 1 if soma >= 1 else 0

def treinar():
    erro_total = 1
    count = 0
    while erro_total != 0:
        erro_total = 0
        for i in range(len(saida_desejada)):
            for n in range(len(saida_desejada)):
                saida = ativar_neuronio(entrada[i], peso)      
                print("Saida da posicao:", i, "=", saida) 
                erro = saida_desejada[i][n]-saida
                print("Erro da posicao:", i, "=", erro) 
                erro_total += erro
                print("Erro total:", erro_total) 
                for j in range(len(peso)):
                    print("Peso anterior:", peso[j]) 
                    peso[j] =+ peso[j]+(taxa_aprendizado * erro * entrada[i][j])
                    print("Peso atualizado:", peso[j]) 
        count += 1
    print("Peso final", str(peso))
    print("Ciclos", count)
    
            
if __name__ == "__main__":
    treinar()