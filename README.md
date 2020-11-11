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
