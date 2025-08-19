def calcular_media_boletim(notas:list[float]) -> float:

   #Validando se a entrada é uma lista
    if not isinstance(notas, list):
        raise TypeError("Nota invalida")
   
    for notinhas in notas:
        if isinstance(notinhas, str):
            raise ValueError("Nota invalida")
   


   



    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")
   

     #Validando se a lista possui menos de 4 notas
    if len(notas) < 4:
        raise ValueError("Notas insuficientes")
   

   
    for nota in notas:
        if nota >= 7:
            raise ValueError("Aprovado")
        if nota < 0 or nota > 10:
            raise ValueError("Nota invalida")
   
    if any(nota >= 7 for nota in notas):
        raise ValueError("Aprovado")
   
    if any(nota < 7 and nota >= 5 for nota in notas):
        raise ValueError("Recuperação")
   
    if (nota < 5 for nota in notas):
        raise ValueError("Reprovado")
    #Tem que ser return