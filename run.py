
import random


def NuevoDiaYValorAlpine(ultimoValor,cambio24Horas):
    cambioGenerado = ultimoValor * cambio24Horas / 100
    return ultimoValor + cambioGenerado



def CalcularCrecimientoEstimadoReal(inversionInicial:float, valorInicialCriptomoneda:float,rango24Cambio:tuple, diasACalcular:int):
    
    print(f"Empezamos en el dia 0 con ${round(inversionInicial*valorInicialCriptomoneda,2)} Dolares.")
    subio=False
    ultimoValor=valorInicialCriptomoneda
    valorActualCriptomoneda=0
    for dia in range(diasACalcular):
        cambio24Actual= round(random.uniform(rango24Cambio[0],rango24Cambio[1]),2)
        valorActualCriptomoneda=NuevoDiaYValorAlpine(ultimoValor,cambio24Actual)
        subio = valorActualCriptomoneda > ultimoValor
        ultimoValor = valorActualCriptomoneda
        print(f"Dia {dia+1}: Valor ALPINE -> ${round(valorActualCriptomoneda,2)} --- ","Aumentó" if subio else "Disminuyó",f"un %{abs(cambio24Actual)}.")
        print(f"Valor de la inversión actual= ${round(valorActualCriptomoneda*inversionInicial,2)}.")
        print()




    return round(valorActualCriptomoneda*inversionInicial,2)
        
def CalcularGananciasEstimado(valorInicial, gananciaPromedioPorcent, diasACalcular):
    
    print(f"Empezamos en el dia 0 con ${valorInicial} Dolares.")
    gananciasTotales= valorInicial
    for dia in range(diasACalcular):
        porcentajeGananciaREAL= gananciaPromedioPorcent * random.uniform(0.01,1.3) 
        porcentajeDelDia=round(porcentajeGananciaREAL,2)
        valor_Ganancia=(gananciasTotales * porcentajeDelDia) / 100
        gananciasTotales+=valor_Ganancia
        print(f"En el dia {dia+1} huno un %{porcentajeDelDia} de ganancia y recibimos ${round(valor_Ganancia)} extra. - Saldo actual= ${round(gananciasTotales)}.")


    return round(gananciasTotales,2)


def main():
    # cryptosActuales=float(input("Ingrese su inversion actual de criptomonedas! ->>  "))
    # valorCryptoActual =float(input("Cuál es el precio en dolares de la criptomoneda en este momento? ->> "))
    # print("---------------------------------------------------------------------------")
    # ganancias=CalcularCrecimientoEstimadoReal(cryptosActuales,valorCryptoActual,(-7,15),7)
    ganancias=CalcularGananciasEstimado(38.59,7,14)

    print(f"Tus dolares generados fueron de ${ganancias}!!")


    







if __name__ == "__main__":
    main()
