def run():    
    entrada = input('Ingrese la letra de las vacunas aplicas: ')
    vacunas = entrada.strip()
    vacunas = vacunas.upper()
    vacunas = vacunas.replace(' ','')
    
    letra_vacuna_anterior = ''
    letra_vacunas_aplicadas = []
    numero_vacunas = []
    cont = -1

    for letra in vacunas:
        if letra != letra_vacuna_anterior:
            letra_vacunas_aplicadas.append(letra)
            numero_vacunas.append(1)
            cont += 1                      
        
        else:            
            numero_vacunas[cont] += 1

        letra_vacuna_anterior = letra

    print(*letra_vacunas_aplicadas)
    print(*numero_vacunas)  


if __name__ == '__main__':
    run()