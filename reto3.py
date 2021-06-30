def run():

    vacunas = input('Ingrese la letras de la vacunas aplicadas: ')
    vacunas = vacunas.strip()
    vacunas = vacunas.upper()
    vacunas = vacunas.replace(' ', '')

    letra_anterior = ''
    lista_letras = []
    numero_letras = []


    for letras in vacunas:
        if len(lista_letras) == 0 or letras != lista_letras[-1]:
            lista_letras.append(letras)
            numero_letras.append(1)

        
        if letra_anterior != '' and letra_anterior ==  letras:
            numero_letras[-1] += 1

        letra_anterior = letras

    print(*lista_letras)
    print(*numero_letras)      
            

if __name__ ==  '__main__':
    run()


