import random

def Nrandom():
    return random.randint(1,101)

def Juego(Njuegos):
    NumeroApuestas=[0 for i in range(Njuegos)]
    Probabilidad=[1 for i in range(Njuegos)]
    Resultado=[1 for i in range(Njuegos)]
    a=2 #Valor de la apuesta
    WC=8    #Codicion de victoria
    
    for i in range(Njuegos):    #Se repetira el juego las n veces
        Creditos=2 #Valor con que inicio
        
        while Creditos!=0 and Creditos<WC:  #El juego se realizara hasta que no tengamos 0 o superemos la condcion de victoria
            print("Tus creditos actualmente son:",Creditos)
                
            if Nrandom()<=50:
                print("GANASTE")
                Creditos=Creditos+a
            else:
                print("Perdiste")
                Creditos=Creditos-a
            Probabilidad[i]=Probabilidad[i]*0.5
            NumeroApuestas[i]=NumeroApuestas[i]+1
            if Creditos==0:
                 Probabilidad[i]=  1-Probabilidad[i]
                 Resultado[i]=0
                 
    print("Programa terminado")
    #print("Las probabilidades observadas fueron de ",Probabilidad)
    print("La probabilidad promedio de ganar fue de:",promediarLista(Probabilidad))

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum/len(lista)

####Aqui se inicia el codigo
Juego(100) #Numero de juegos