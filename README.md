# Practica 3 Multihilos

Ejercicios en Python

![Screenshot](Python.png)

## Ejercicio 1

Realizar un programa que genere 20 hilos a partir del programa principal.
Cada hilo ejecutará una función en la que en primer lugar se imprimirá el número de cada hilo empezando desde el 1 hasta el 20.
Esta función realizará una espera de 3 segundos y a continuación imprimirá el número del hilo y cuando ha finalizado.
Finalmente, desde el programa principal, esperamos a que finalicen para juntarlos y mostramos un mensaje final indicando que el programa ha finalizado.
La salida que tenemos que observar es una lista de inicio de procesos ordenada y sin embargo una lista de procesos finalizados desordenada.

### Version 1

Prototipo para 5 hilos puestos a piñon

![Screenshot](/capturas/2020-11-11.png)

### Version 2

Hilos creados con un for (hay que hacer un for para cada estado del hilo; sino no funciona bien)

![Screenshot](/capturas/2020-11-11%20(1).png)

## Ejercicio 2

En este ejercicio vamos a trabajar los semáforos (from threading import Semaphore)

Para declarar un semáforo: sem = Semaphore(WIDTH). WIDTH indica la cantidad de hilos que pueden ejecutar la sección crítica (1..N)

Realizar un programa que genere 20 hilos a partir del programa principal.

Cada hilo ejecutará una función en la que se accede a un túnel de uno en uno, tomando un tiempo determinado (3s) en la que en primer lugar se imprimirá el número de cada hilo, esperaremos 3s para adquirir el semáforo (.acquire()), imprimimos que ha entrado al túnel, esperaremos 1s para liberar el semaforo (.release()) e imprimimos que ese hilo ha salido del túnel.
Finalmente, desde el programa principal, esperamos a que finalicen para juntarlos y mostramos un mensaje final indicando que el programa ha finalizado.

La salida que tenemos que observar es una lista de inicio de procesos ordenada y sin embargo una lista de procesos finalizados desordenada.

Resultado para 5 hilos (se ve mejor)
![Screenshot](/capturas/2020-11-11%20(2).png)

Si acortamos los tiempos del tunel, podremos observar que algunos hilos salen del tunel antes de que otros entren al tunel.

