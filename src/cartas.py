"""
:author: reinaqu_2
"""

from typing import NamedTuple, List, Dict

Carta = NamedTuple("Carta", [("palo",str),("valor",int)])

from collections import Counter, defaultdict
def crear_dicc_conteo_valores (cartas:List[Carta])->Dict[int, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas (frecuencia) con ese valor
    :rtype: {int:int}
    '''
    return Counter(x. valor for x in cartas)

def crear_dicc_valores_por_palos (cartas:List[Carta])->Dict[str, List[int]]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los palos y como valores una lista con los valores de las cartas de ese palo
    :rtype: {str:[int]}
    '''
    lista_valores_por_palos = defaultdict(list)
    for x in cartas:
        lista_valores_por_palos[x.palo].append(x.valor)
    return lista_valores_por_palos


def obtener_clave_mayor(dicc:Dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}       
    Devuelve:
    :return: La clave con valor mayor, según el orden natural
    :rtype: int
    '''
    return max(dicc.keys())

def obtener_valor_mayor_frecuencia(dicc:Dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}
    Devuelve:
    :return: El valor mayor, que en ese caso es el valor de carta con una frecuencia mayor
    :rtype: int
    '''
    return max(dicc.items(), key=lambda n: n[1])[0]

from statistics import mean
def obtener_media_valores_por_palos(cartas:List[Carta])->Dict[str, float]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, la media de los valores de las cartas de ese palo
    :rtype: {str:float} 
    '''
    return {palo:mean(valores) for palo, valores in crear_dicc_valores_por_palos(cartas).items()}

def obtener_max_valores_por_palos(cartas:List[Carta])->Dict[str, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]       
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    :rtype: {str: int}
    '''
    return {palo:max(valores) for palo, valores in crear_dicc_valores_por_palos(cartas).items()}