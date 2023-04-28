import csv
import statistics


def abrir_archivo():
    edad = []
    with open('datos.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            edad.append(int(row[0]))
    return edad


def promedio(edad):  # promedio
    return int(statistics.mean(edad))


def mediana(edad):  # mediana
    return statistics.median(edad)


def moda(edad):  # moda
    return statistics.mode(edad)


def desviacion(edad):  # desviacion estandar
    return statistics.pstdev(edad)


def varianza(edad):  # varianza
    return statistics.pvariance(edad)


def main():
    edad = abrir_archivo()

    print(f"promedio: {promedio(edad)}")
    print(f"mediana: {mediana(edad)}")
    print(f"moda: {moda(edad)}")

    print(f"desviacion: {desviacion(edad)}")
    print(f"varianza: {varianza(edad)}")


main()
