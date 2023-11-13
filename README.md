### Ejercicio para trabajar con diccionarios.

Autora: Toñi Reina

Este es un proyecto introductorio para trabajar con diccionarios. Se trata de una serie de ejercicios sencillos para trabajar con los esquemas que utilizaremos para trabajar con diccionarios.

En primer lugar vamos a trabajar con una lista de tuplas que representan títulos de álbumes y el año de publicación de ese álbum.

```python
    l_bso = {("Thriller",1982), 
             ("Back in Black",1980), 
             ("The Dark Side of the Moon", 1973), 
             ("The Bodyguard",1992), 
             ("Bat Out of Hell",1977), 
             ("Their Greatest Hits (1971-1975)", 1976), 
             ("Saturday Night Fever",1977), 
             ("Rumours",1977)}
```

Resuelve los siguientes ejercicios:

1. Implementa una función que cree un diccionario que tenga como claves los títulos de los álbumes y como valores los años.
2. Implementa una función que cree un diccionario que tenga como claves los años y como valores el número de títulos de ese año.
3. Implementa una función que cree un diccionario que tenga como claves los años y como valores una lista con los títulos de ese año.
4. Implementa una función que dado un diccionario de titulos y años, devuelva el título mayor.
5. Implementa una función que dado un diccionario de titulos y años, devuelva el año mayor.
6. Dado un diccionario de titulos y años, devuelva el título con más caracteres.


En segundo lugar vamos a trabajar con una `namedtuple` que representa una carta de la baraja española, y tiene dos campos: palo,de tipo `str`,  que puede tomar los valores "Oros", "Copas","Espadas" y "Bastos"; y valor, de tipo `int`, que representa un número del 1 al 12 con el valor numérico de la carta.

```python
Carta = NamedTuple("Carta", [("palo",str),("valor",int)])
```
En el módulo de test se generan dos mazos de cartas, uno (MAZO1) con 2000 cartas generadas de forma aleatoria, y otro (MAZO2) con 20 cartas:

```python
if __name__ == '__main__':
    mazo1 = generar_cartas_aleatorias(2000)
    mazo2 = generar_cartas_aleatorias(20)
```
Implementa las funciones del módulo `cartas.py`, sustituyendo `pass` por el código necesario para resolver el método.

