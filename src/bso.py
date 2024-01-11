'''
@author: reinaqu
'''
from typing import List, Tuple, Dict
def crear_dicc_titulos_anyos(bsos:List[Tuple[str,int]])->Dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    return dict(bsos)

def crear_dicc_titulos_anyos2(bsos:List[Tuple[str,int]])->Dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    return {x:y for x,y in bsos}

from collections import Counter, defaultdict
def crear_dicc_anyos_conteo_titulos (bsos:List[Tuple[str,int]])->Dict[int, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores el número de títulos
          de ese año
    :rtype: {int:int}
    '''
    return Counter(anyo for _, anyo in bsos)

def crear_dicc_anyos_lista_titulos (bsos:List[Tuple[str,int]])->Dict[int, List[str]]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores una lista con los títulos
          de ese año
    :rtype:{int:[str]}
    '''
    lista_titulos_por_anyo = defaultdict(list)
    for titulo,anyo in bsos:
        lista_titulos_por_anyo[anyo].append(titulo)
    return lista_titulos_por_anyo

def obtener_clave_mayor(dicc_bso:Dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: La clave con valor mayor, segun el orden natural
    :rtype: str
    '''
    return max(dicc_bso.keys())

def obtener_valor_mayor(dicc_bso:Dict[str,int])->int:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El valor mayor, que en este caso es el año más reciente.
    :rtype: int
    '''
    return max(dicc_bso.values())

def obtener_nombre_mas_largo(dicc_bso:Dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El nombre de la canción con más caracteres
    :rtype: str
    '''
    return max(dicc_bso.keys(), key=lambda n: len(n))