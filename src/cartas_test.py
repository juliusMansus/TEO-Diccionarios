"""
@author: reinaqu
"""
import random
from cartas import *

from typing import TypeVar, Dict, List

K=TypeVar("K")
V=TypeVar("V")
#Lista con los nombres de los palos
PALOS = ["Oros", "Copas","Espadas", "Bastos"]

def mostrar_dicc_por_linea(dicc:Dict[K,V])->None:
    for clave, valor in dicc.items():
        print(clave, "==>", valor)

def generar_cartas_aleatorias(num:int=10)->List[Carta]:
    lista = [ ]
    for _ in range(num):
        palo = random.choice(PALOS)
        valor = random.randint(1,12)
        lista.append(Carta(palo, valor))
    return lista

#Versión con definición por compresión
def generar_cartas_aleatorias_2(num:int=10)->List[Carta]:
    return [Carta(random.choice(PALOS), random.randint(1,12))
               for _ in range(num)]
    
def test_crear_dicc_conteo_valores(cartas:List[Carta])->None:
    print("test_crear_dicc_conteo_valores", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(dicc)

def test_crear_dicc_valores_por_palos(cartas:List[Carta])->None:
    print("test_obtener_valor_mayor_frecuencia", "="*20)
    dicc = crear_dicc_valores_por_palos(cartas)
    mostrar_dicc_por_linea(dicc)
    
def test_obtener_clave_mayor(cartas:List[Carta])->None:
    print("test_obtener_clave_mayor", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(obtener_clave_mayor(dicc))
    
def test_obtener_valor_mayor_frecuencia(cartas:List[Carta])->None:
    print("test_obtener_valor_mayor_frecuencia", "="*20)
    dicc = crear_dicc_conteo_valores(cartas)
    print(obtener_valor_mayor_frecuencia(dicc))
    
def test_obtener_media_valores_por_palos(cartas:List[Carta])->None:
    print("test_obtener_media_valores_por_palos", "="*20)
    print(obtener_media_valores_por_palos(cartas))

def test_obtener_max_valores_por_palos(cartas:List[Carta])->None:
    print("test_obtener_media_valores_por_palos", "="*20)
    print(obtener_max_valores_por_palos(cartas))
    
if __name__ == '__main__':
    mazo1 = generar_cartas_aleatorias(2000)
    mazo2 = generar_cartas_aleatorias(20)
    print(mazo1)
    print(mazo2)
    
    test_crear_dicc_conteo_valores (mazo1)
    test_crear_dicc_conteo_valores (mazo2)
    
    test_crear_dicc_valores_por_palos(mazo1)
    test_crear_dicc_valores_por_palos(mazo2)
    
    test_obtener_clave_mayor(mazo1)
    test_obtener_clave_mayor(mazo2)
    
    test_obtener_valor_mayor_frecuencia(mazo1)
    test_obtener_valor_mayor_frecuencia(mazo2)
    
    test_obtener_media_valores_por_palos(mazo1)
    test_obtener_media_valores_por_palos(mazo2)
    
    test_obtener_max_valores_por_palos(mazo1)
    test_obtener_max_valores_por_palos(mazo2)