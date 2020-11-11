# En este ejercicio vamos a trabajar los semáforos (from threading import Semaphore)
# Para declarar un semáforo: sem = Semaphore(WIDTH). WIDTH indica la cantidad de hilos que pueden ejecutar la sección crítica (1..N)
# Realizar un programa que genere 20 hilos a partir del programa principal.
# Cada hilo ejecutará una función en la que se accede a un túnel de uno en uno, tomando un tiempo determinado (3s)
# en la que en primer lugar se imprimirá el número de cada hilo,
# esperaremos 3s para adquirir el semáforo (.acquire()),
# imprimimos que ha entrado al túnel, esperaremos 1s para liberar el semaforo (.release())
# e imprimimos que ese hilo ha salido del túnel.
# Finalmente, desde el programa principal, esperamos a que finalicen para juntarlos y mostramos un mensaje final indicando que el programa ha finalizado.
import threading
import time


def task():
    sem = threading.Semaphore(1)
    print('Inicio tarea.-  {}'.format(threading.current_thread().name))
    time.sleep(2)
    sem.acquire()
    print('inicio tunel.-  {}'.format(threading.current_thread().name))
    time.sleep(1)
    sem.release()
    print('salida tunel.-  {}'.format(threading.current_thread().name))


if __name__ == "__main__":
    num_hilos = 20
    hilos = list()

    for i in range(num_hilos):
        hilo = threading.Thread(target=task, name="hilo %s" % (i+1))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print('finish')


