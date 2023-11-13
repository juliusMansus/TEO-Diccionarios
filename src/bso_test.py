'''
@author: reinaqu
'''
from bso import *

def test_crear_dicc_titulos_anyos (bso:List[Tuple[str, int]])->None:
    print("1. Cree un diccionario que tenga como claves los títulos y como valores los años")
    dicc = crear_dicc_titulos_anyos (bso)
    print(dicc)

def test_crear_dicc_anyos_conteo_titulos (bso:List[Tuple[str, int]])->None:
    print("2. Cree un diccionario que tenga como claves los años y como valores el número de títulos de ese año")
    dicc = crear_dicc_anyos_conteo_titulos (bso)
    print(dicc)

def test_crear_dicc_anyos_lista_titulos (bso:List[Tuple[str, int]])->None:
    print("3. Cree un diccionario que tenga como claves los años y como valores una lista con los títulos de ese año")
    dicc = crear_dicc_anyos_lista_titulos (bso)
    print(dicc)
    
def test_obtener_clave_mayor(bso:List[Tuple[str, int]])->None:
    print("4. Dado un diccionario de titulos y años, devuelva el título mayor")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_clave_mayor(dicc)
    print(mayor)    
              
def test_obtener_valor_mayor(bso:List[Tuple[str, int]])->None:
    print("5. Dado un diccionario de titulos y años, devuelva el año mayor")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_valor_mayor(dicc)
    print(mayor)    

def test_obtener_titulo_mas_largo(bso:List[Tuple[str, int]])->None:
    print("6. Dado un diccionario de titulos y años, devuelva el título con más caracteres")
    dicc = crear_dicc_titulos_anyos (bso)
    mayor = obtener_nombre_mas_largo(dicc)
    print(mayor)
        
if __name__ == '__main__':
    l_bso = {("Thriller",1982), 
             ("Back in Black",1980), 
             ("The Dark Side of the Moon", 1973), 
             ("The Bodyguard",1992), 
             ("Bat Out of Hell",1977), 
             ("Their Greatest Hits (1971-1975)", 1976), 
             ("Saturday Night Fever",1977), 
             ("Rumours",1977)}
    print(l_bso)
    test_crear_dicc_titulos_anyos(l_bso)
    test_crear_dicc_anyos_conteo_titulos (l_bso)
    test_crear_dicc_anyos_lista_titulos (l_bso)
    test_obtener_clave_mayor(l_bso)
    test_obtener_valor_mayor(l_bso)
    test_obtener_titulo_mas_largo(l_bso)