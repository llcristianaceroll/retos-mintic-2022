def prueba(n):
    nombre_vacunas = ""
    vacuna_anterior = ""
    contador = -1
    numero_vacunas = []

    for vacunas in n:
        if vacuna_anterior != vacunas: 
            nombre_vacunas += vacunas + " "
            vacuna_anterior = vacunas
            contador += 1
            numero_vacunas.append(1)

        else:
            numero_vacunas[contador] += 1

    print(nombre_vacunas)
    print(*numero_vacunas)
    

if __name__ == "__main__":
    entrada = input("Ingrese Vacunas: ")
    vacunas = entrada.split(" ")
    prueba(vacunas)