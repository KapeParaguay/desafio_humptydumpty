'''+++ PROBLEMA DE HUMPTY DUMPTY +++
Escribe una funcion que reciba un numero n, que indica el limite superior de una lista de los números del 1 a n.

La función debe retornar dicha lista con sus elementos en forma de cadena, pero por cada múltiplo de 3 debe ser sustituido por 'Humpty' en vez del número, y para los múltiplos de 5, debe ser sustituido por 'Dumpty' en vez del número. 

Para los números que son múltiplos tanto de 3 como de 5 debe ser sustituido por 'HumptyDumpty'.'''

def humpty_dumpty(n):
    lista =[]
    try:
        n = int(n)
        for h in range(1, n + 1):
            if h % 3 == 0 and h % 5 == 0:
                lista.append("Humpty Dumpty")
            elif h % 3 == 0:
                lista.append("Humpty")
            elif h % 5 == 0:
                lista.append("Humpty")
            else:
                lista.append(str(h))
        return lista
    except ValueError:
        return "Pusiste una letra y solo funciona con numeros"
print(humpty_dumpty('a'))