"""
:author: reinaqu_2
"""

from typing import NamedTuple, List, Dict

Carta = NamedTuple("Carta", [("palo",str),("valor",int)])

def crear_dicc_conteo_valores (cartas:List[Carta])->Dict[int, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas (frecuencia) con ese valor
    :rtype: {int:int}
    '''
    pass

def crear_dicc_valores_por_palos (cartas:List[Carta])->Dict[str, List[int]]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los palos y como valores una lista con los valores de las cartas de ese palo
    :rtype: {str:[int]}
    '''
    pass


def obtener_clave_mayor(dicc:Dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}       
    Devuelve:
    :return: La clave con valor mayor, según el orden natural
    :rtype: int
    '''
    pass

def obtener_valor_mayor_frecuencia(dicc:Dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}
    Devuelve:
    :return: El valor mayor, que en ese caso es el valor de carta con una frecuencia mayor
    :rtype: int
    '''
    pass

def obtener_media_valores_por_palos(cartas:List[Carta])->Dict[str, float]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, la media de los valores de las cartas de ese palo
    :rtype: {str:float} 
    '''
    pass

def obtener_max_valores_por_palos(cartas:List[Carta])->Dict[str, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]       
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    :rtype: {str: int}
    '''
    pass