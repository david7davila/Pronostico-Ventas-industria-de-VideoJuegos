def NaiveBayes(A,B):
    NUBLADO=[1,1,1,1]
    LLUVIA=[1,1,0,0,0]
    SOLEADO=[1,1,1,0,0]
    Total={"SI":NUBLADO.count(1)+LLUVIA.count(1)+SOLEADO.count(1),"NO":NUBLADO.count(0)+LLUVIA.count(0)+SOLEADO.count(0)}
    NPartidos=sum(Total.values()) #Suma de partidos
    Probabilid={"NUBLADO":((NUBLADO.count(1)+NUBLADO.count(0))/NPartidos),"LLUVIA":(LLUVIA.count(1)+LLUVIA.count(0))/NPartidos,"SOLEADO":(SOLEADO.count(1)+SOLEADO.count(0))/NPartidos,}
    #B="LLUVIA"
    #A="SI"
    Cuenta={"NUBLADO":[NUBLADO.count(1),NUBLADO.count(0)],"LLUVIA":[LLUVIA.count(1),LLUVIA.count(0)],"SOLEADO":[SOLEADO.count(1),SOLEADO.count(0)]}
    
    if (A=="SI"):
        Resultado=Cuenta[B][0]/NPartidos/Probabilid[B]
    else:
        Resultado=Cuenta[B][1]/NPartidos/Probabilid[B]
    print(Resultado)
    


NaiveBayes("NO","SOLEADO") #Probabilidad de evento A dado B