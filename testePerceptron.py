import numpy as np
'''
Resolução para probelma das operações booleanas
multiplicação (AND) e adição (OR)
'''



entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) #Operador AND
saidas = np.array([0,0,0,1])

#entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) #Operado OR
#saidas = np.array([0,1,1,1])


pesos = np.array([0.0,0.0])
txAprend = 0.1

def stepFunction(entrada):
    if entrada >=1: return 1
    return 0

def calcSaida(registro):
    soma = registro.dot(pesos)
    return stepFunction(soma)

def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal=0
        for i in range(len(saidas)):
            saidaCalculada = calcSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                # Fomula para correção dos pesos:
                # W(t+1) = W(t) + e(t) * n * X(t)
        
                pesos[j] = pesos[j] + (txAprend*entradas[i][j]* erro)

                print("Peso att: "+ str(pesos[j]))
        print("Total erros:" + str(erroTotal))
treinar()
print(str(pesos))

print('Testes (AND):')
print('-------')
print('0 AND 0 = ',calcSaida(np.array([0,0])))
print('1 AND 0 = ',calcSaida(np.array([1,0])))
print('0 AND 1 = ',calcSaida(np.array([0,1])))
print('1 AND 1 = ',calcSaida(np.array([1,1])))